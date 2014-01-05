<<<<<<< HEAD
同步twitter到新浪微博及人人网
====================

部署在Google Appengine上，自动同步twitter到新浪微博及人人网，自动转换短链接以防止被屏蔽。

因Sina的oauth2分级政策意味着小应用根本无法使用oauth2。事实上大应用基本都是用它的Xauth方法。
=======
同步twitter到新浪微博&人人网
====================

Twitter-to-weibo by [yfli](https://github.com/yfli/twitter-to-weibo-appengine)

添加了Renren API 2.0 python SDK by [rellik6](https://github.com/rellik6/renrenpy/)
以及同步人人网状态的功能 

部署在Google Appengine上，自动同步twitter到新浪微博，自动转换短链接以防止被屏蔽。
>>>>>>> 46ecc5f0e1d622544b55c2423d194f0cebd69ef9


安装
---

<<<<<<< HEAD
首先下载本项目代码。使用git或直接下载[zip包](https://github.com/mrseaman/twitter-to-weibo-renren/zipball/master)

安装需要以下几步。

=======
首先下载本项目代码。使用git或直接下载[zip包](https://github.com/yfli/twitter-to-weibo-appengine/zipball/master)

安装需要以下几步。

* 申请一个[tiny.cc](http://tiny.cc)的帐号。从api页面 http://tiny.cc/api-docs 取得你的API Key
* 到微博聊天机器人绑定页面http://app.weibo.com/tool/imbot ，绑定gtalk聊天机器人。绑定帐号为[yourappid]@appspot.com。
注意[yourappid]为你将要使用的app engine id。新浪会告诉你聊天机器人的帐号（一般为sinat064@gmail.com的形式）和验证码。

>>>>>>> 46ecc5f0e1d622544b55c2423d194f0cebd69ef9
* 编辑myid.py文件，把用户名、密码、验证码和申请到的App keys填入。

```console
     my_twitter_id=""
     my_weibo_bot=""
     my_weibo_bot_verify_code=""
     my_tinycc_login=""
     my_tinycc_apikey=""
```
* 上传代码到你的appengine
* 用浏览器访问http://yourappid.appspot.com/initialize。
* 到新浪页面http://app.weibo.com/tool/imbot 查看是否绑定成功，如不成功，重复上一步。

部署
---

更改app.yaml中的application id，上传到Google App Engine上。

部署到Google App Engine就是通常的app engine流程，可参看下面两个教程。

* [Google App Engine 入门:上传应用程序](http://blog.xuming.net/2008/05/google-app-engine-toturial-9.html)
* [Google App Engine 6步上手教程](http://www.cnblogs.com/2011sydney/archive/2009/07/23/1529637.html)


示例
---

<<<<<<< HEAD
这是[yfli](https://twitter.com/yfli)创建的一个Lady Gaga的同步。Lady Gaga [twitter](https://twitter.com/ladygaga), 
=======
这是[yfli]建的一个Lady Gaga的同步。Lady Gaga [twitter](https://twitter.com/ladygaga), 
>>>>>>> 46ecc5f0e1d622544b55c2423d194f0cebd69ef9
Lady Gaga [微博](http://weibo.com/u/2841791740)

License
-------
[GPLv3][gplv3]

参考
----
本项目参考/使用了以下项目

* http://code.google.com/p/twitter-feed/
* http://atlee.ca/software/poster/
* http://code.google.com/p/twitter2weiboviagtalk/

联系
----

<<<<<<< HEAD
=======
* [yfli](https://twitter.com/yfli)@twitter
* [warehou](http://www.weibo.com/u/1410749162)@微博

>>>>>>> 46ecc5f0e1d622544b55c2423d194f0cebd69ef9
* [mrseaman](https://twitter.com/_mrseaman)@twitter

Changelog
---------

<<<<<<< HEAD
- ver 0.3 2013/12/31
    
    Add Support Renren sync 
=======
- ver 0.29 2012/7/31

     Enmergency update. Sina blocked Basic Auth since 7/24. Use gtalk robot instead.
>>>>>>> 46ecc5f0e1d622544b55c2423d194f0cebd69ef9

- ver 0.2 2012/7/17

    Support image sync

- ver 0.1 2012/4/27

    First implement.

[gplv3]: http://www.gnu.org/licenses/gpl.html
