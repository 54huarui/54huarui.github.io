---
layout: page
permalink: /blogs/paoku/index.html
title: 逆向某跑酷小游戏
---


## 一.寻找突破口

先进入游戏看一下。首先应该判断这个游戏有没有联网验证。

<img src="https://54huarui.github.io/blogs/paoku/tt.png" width="880" height="480">

断网后直接出现断网提示，我们接下来应该先从这里入手

 ## 二.关闭断网验证

使用mt管理器打开应用看看，应用没有加密

<img src="https://54huarui.github.io/blogs/paoku/t1.png" width="880" height="480">

在字符常量池中搜索断网提示，发现这段可疑代码

<img src="https://54huarui.github.io/blogs/paoku/t2.png" width="880" height="480">


这里可以看到一个在断网提示的跳转 if-nez p1,cond_6，想要跳过断网提示可以我们直接改成 if-nez p1,cond_6

打包保存退出签名，再次打开游戏，断开网络，可以看到断网提示没了。这也说明这款应用没有签名效验。接下来就是内购的破解

## 三.内购破解

这里我们点击支付，发现有支付宝和微信的支付方式，返回后提示支付失败

<img src="https://54huarui.github.io/blogs/paoku/t3.png" width="380" height="480">


那我们直接从这个提示下手。打开mt，搜索支付失败

<img src="https://54huarui.github.io/blogs/paoku/t4.png" width="880" height="480">

很糟糕的是这里没有任何要点，看上去就是个放字符串的地方。只好考虑破解常用的那几种关键词

最终搜索paysuccess这里找到了相关方法 onSuccess。

<img src="https://54huarui.github.io/blogs/paoku/t5.png" width="880" height="480">


同时还在这个地方找到了有关支付失败的方法 onFail 和onCancel

<img src="https://54huarui.github.io/blogs/paoku/t6.png" width="880" height="480">

<img src="https://54huarui.github.io/blogs/paoku/t7.png" width="880" height="480">

