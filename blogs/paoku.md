---
layout: page
permalink: /blogs/paoku/index.html
title: 逆向某跑酷小游戏
---


## 一.寻找突破口

<br><br>

**先进入游戏看一下。首先应该判断这个游戏有没有联网验证。**

<br>

<img src="https://54huarui.github.io/blogs/paoku/tt.png" width="880" height="480">

<br>

**断网后直接出现断网提示，我们接下来应该先从这里入手**

<br><br>

## 二.关闭断网验证

<br><br>

**使用mt管理器打开应用看看，应用没有加密**

<br>

<img src="https://54huarui.github.io/blogs/paoku/t1.png" width="880" height="480">

<br>

**在字符常量池中搜索断网提示，发现这段可疑代码**

<br>

<img src="https://54huarui.github.io/blogs/paoku/t2.png" width="880" height="480">

<br>

**这里可以看到一个在断网提示的跳转 if-nez p1,cond_6，想要跳过断网提示可以我们直接改成 if-nez p1,cond_6**

**打包保存退出签名，再次打开游戏，断开网络，可以看到断网提示没了。这也说明这款应用没有签名效验。接下来就是内购的破解**

<br><br>

## 三.内购破解

<br><br>

**这里我们点击支付，发现有支付宝和微信的支付方式，返回后提示支付失败**

<img src="https://54huarui.github.io/blogs/paoku/t3.png" width="380" height="480">


**那我们直接从这个提示下手。打开mt，搜索支付失败**

<img src="https://54huarui.github.io/blogs/paoku/t4.png" width="880" height="480">

**很糟糕的是这里没有任何要点，看上去就是个放字符串的地方。只好考虑破解常用的那几种关键词**

**最终搜索paysuccess这里找到了相关方法 onSuccess。**

<br>

<img src="https://54huarui.github.io/blogs/paoku/t5.png" width="880" height="480">

<br>

**同时还在这个地方找到了有关支付失败的方法 onFail 和onCancel**

<br>

<img src="https://54huarui.github.io/blogs/paoku/t6.png" width="880" height="480">

<br>

<img src="https://54huarui.github.io/blogs/paoku/t7.png" width="880" height="480">

<br>

**根据经验，这里有两个思路**

**一是找到调用这两个方法的地方，修改相关的判断规则，让支付失败跳转到支付成功。然而我搜索到调用onSuccess的地方有很多，一个个排查很难。**

**二是直接将成功的代码复制到失败的地方。我这里直接采用这种方法。**

**修改保存签名，打开游戏，买东西返回，破解成功**

<br>

<img src="https://54huarui.github.io/blogs/paoku/t8.png" width="880" height="480">

<br><br><br>

[破解下载 密码f98e](https://pan.baidu.com/s/11GvbJCj4WueWvaClnD-jmQ)