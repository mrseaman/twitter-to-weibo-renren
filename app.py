import logging
import webapp2
from google.appengine.ext.webapp import template
from google.appengine.api.app_identity import get_application_id 
from google.appengine.api import users

import tweepy

from models import OAuthToken, Account
from myid import *


class MainPage(webapp2.RequestHandler):

    def get(self):
        # Build a new oauth handler and display authorization url to user.
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET, CALLBACK)
        try:
            #import pdb; pdb.set_trace()
            url = auth.get_authorization_url()
            self.response.out.write(
                    template.render('templates/home.html', 
                        {"auth_url": url}))
        except tweepy.TweepError, e:
            # Failed to get a request token
            self.response.out.write(
                    template.render('templates/error.html', {'message': e}))
            return

        # We must store the request token for later use in the callback page.
        request_token = OAuthToken(
                token_key = auth.request_token.key,
                token_secret = auth.request_token.secret
        )
        request_token.put()

# Callback page (/oauth/callback)
class CallbackPage(webapp2.RequestHandler):

    def get(self):
        oauth_token = self.request.get("oauth_token", None)
        oauth_verifier = self.request.get("oauth_verifier", None)
        if oauth_token is None:
            # Invalid request!
            self.response.out.write(template.render('templates/error.html', {
                    'message': 'Missing required parameters!'
            }))
            return

        # Lookup the request token
        request_token = OAuthToken.gql("WHERE token_key=:key", key=oauth_token).get()
        if request_token is None:
            # We do not seem to have this request token, show an error.
            self.response.out.write(template.render('templates/error.html', {'message': 'Invalid token!'}))
            return

        # Rebuild the auth handler
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_request_token(request_token.token_key, request_token.token_secret)

        # Fetch the access token
        try:
            auth.get_access_token(oauth_verifier)
            username = auth.get_username();
        except tweepy.TweepError, e:
            # Failed to get access token
            self.response.out.write( template.render('templates/error.html', {'message': e}))
            return
        
        # Lookup the account
        account = Account.get_by_key_name(username)
        if account is None:
            # We do not seem to have this account. create one
            account = Account(key_name = username)

        account.tw_screenname = username
        account.tw_token_key = request_token.token_key
        account.tw_token_secret =  request_token.token_secret
        account.tw_access_key = auth.access_token.key
        account.tw_access_secret = auth.access_token.secret
        account.put();

        request_token.delete();

        self.response.out.write(
                template.render('templates/callback.html', {'account':account}))
      
# bindweibo 
class BindWeiboPage(webapp2.RequestHandler):

    def post(self):
        username = self.request.get("username")
        account = Account.get_by_key_name(username)
        account.wb_access_token = self.request.get("wb_access_token")
        account.rr_access_token = self.request.get("rr_access_token")
        account.put()

        self.redirect('/binding.html')

app = webapp2.WSGIApplication(routes=[
        (r'/', MainPage),
        (r'/bindweibo', BindWeiboPage),
        (r'/oauth/callback', CallbackPage),
], debug=True)
