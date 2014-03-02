同步 Twitter 到新浪微博及人人网
====================

部署在Google Appengine上，自动同步twitter到新浪微博及人人网，自动转换短链接以防止被屏蔽。

Twitter-to-weibo by [yfli](https://github.com/yfli/twitter-to-weibo-appengine)

添加了Renren API 2.0 python SDK by [rellik6](https://github.com/rellik6/renrenpy/)
以及同步人人网状态的功能 


安装
---

首先下载本项目代码。使用git或直接下载[zip包](https://github.com/mrseaman/twitter-to-weibo-renren/zipball/master)

安装需要以下几步。

* 申请一个[tiny.cc](http://tiny.cc)的帐号。从api页面 http://tiny.cc/api-docs 取得你的API Key

* 编辑myid.py文件，把用户名、密码、验证码和申请到的App keys填入。

```console
     my_twitter_id=""
     my_weibo_bot=""
     my_weibo_bot_verify_code=""
     my_tinycc_login=""
     my_tinycc_apikey=""
```
* 上传代码到你的appengine(见部署）
* 部署后打开 yourappid.appspot.com 进行设置，加入账户认证信息
部署
---

更改app.yaml中的application id，上传到Google App Engine上。

部署到Google App Engine就是通常的app engine流程，可参看下面两个教程。

* [Google App Engine 入门:上传应用程序](http://blog.xuming.net/2008/05/google-app-engine-toturial-9.html)
* [Google App Engine 6步上手教程](http://www.cnblogs.com/2011sydney/archive/2009/07/23/1529637.html)


示例
---

这是[yfli](https://twitter.com/yfli)创建的一个Lady Gaga的同步。Lady Gaga [twitter](https://twitter.com/ladygaga), Lady Gaga [微博](http://weibo.com/u/2841791740)

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

* [yfli](https://twitter.com/yfli)@twitter
* [warehou](http://www.weibo.com/u/1410749162)@微博
* [mrseaman](https://twitter.com/_mrseaman)@twitter

Changelog
---------

- ver 0.3 2013/12/31
    
    Add Support Renren sync 

- ver 0.29 2012/7/31

     Enmergency update. Sina blocked Basic Auth since 7/24. Use gtalk robot instead.

- ver 0.2 2012/7/17

    Support image sync

- ver 0.1 2012/4/27

    First implement.

[gplv3]: http://www.gnu.org/licenses/gpl.html
