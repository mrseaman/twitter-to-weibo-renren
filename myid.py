"""
IDs
"""
import os

MY_TINYCC_LOGIN="urfatu"
MY_TINYCC_APIKEY="c0fe7bc4-4fd8-4b56-970f-9489feaca677"

if os.environ.get('SERVER_SOFTWARE','').startswith('Devel'):
    CONSUMER_KEY = 'owRilZIiE0IMHtm6Zjgfg'
    CONSUMER_SECRET = 'ES7fSj3Tw5F6HF7BvouksJ9f9Pw5ZHYek4XBRsUcic'
    CALLBACK = 'http://127.0.0.1:8080/oauth/callback'
else:
    CONSUMER_KEY = 'ML9Ro96QDEdgCjcHgzJwVA'
    CONSUMER_SECRET = 'f80mZoOYQGsKRPHYnVWMjQzjiopdHlx10Ch21NrBswo'
    CALLBACK = 'http://twitter--weibo.appspot.com/oauth/callback'

