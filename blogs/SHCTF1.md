# 山河CTF--yzmcms7.0

<br>

## 利用

<br>

打开进去是yzmcms，随意输入一个错误的页面，得知cms的版本号。

<br>

<img src="https://54huarui.github.io/blogs/SHCTF1/1.png" width="880" height="480">

<br>

按照网上的poc试了一下，出错了

<br>

<img src="https://54huarui.github.io/blogs/SHCTF1/2.png" width="880" height="480">

<br>

看来是不行了，查了资料知道漏洞点也在admin_add存在同样的功能点

<br>

## POC

<br>

<img src="https://54huarui.github.io/blogs/SHCTF1/3.png" width="880" height="480">

<br>

成功执行命令，算是利用成功了

<br>

<img src="https://54huarui.github.io/blogs/SHCTF1/4.png" width="880" height="480">