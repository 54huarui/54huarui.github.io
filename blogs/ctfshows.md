# ctfshow刷题
# 随便刷刷

<br>

## web2

<br>

简单的sql，无需多言

<img src="https://54huarui.github.io/blogs/ctfshows/1.png" width="880" height="480">

直接用sqlmap秒了

<img src="https://54huarui.github.io/blogs/ctfshows/2.png" width="880" height="480">


## web9

<br>

利用dirb扫描出robots.txt有内容，进去后得到并下载index.phps

<img src="https://54huarui.github.io/blogs/ctfshows/3.png" width="880" height="480">

<img src="https://54huarui.github.io/blogs/ctfshows/4.png" width="880" height="480">

因为题目是先md5然后才进入注入，这题只能碰撞了


第二个参数是ture的时候MD5之后是hex格式，转化到字符串时如果出现'or'xxxx的形式，就会导致注入

这里提供一个抄来的字符串：ffifdyop
md5(ffifdyop,32) = 276f722736c95d99e921722cf9ed621c
转成字符串为'or'6�]��!r,��b

<img src="https://54huarui.github.io/blogs/ctfshows/5.png" width="880" height="480">