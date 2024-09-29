# Nginx权限提升漏洞(CVE-2016-1247)

<br><br>

## 原题：ctfshow内部赛 “除了菜刀还会个啥”

<br>

### 菜刀

先用菜刀连上，然后上传哥斯拉的shell

<br>

### 提权

<br>

<img src="https://54huarui.github.io/blogs/dingshi/1.png" width="880" height="480">

<br>

根据这个nginx的任务，这里有一个nginx的提权漏洞 CVE-2016-1247

<br>

这里要注意的点是漏洞利用的POC不能在windows制作然后上传，否则运行时会报错“/bin/bash^M: bad interpreter: No such file or directory”

这是因为linux却是只能执行格式为unix格式的脚本。如果在windows下创建则会变成dos格式

<br>

<img src="https://54huarui.github.io/blogs/dingshi/2.png" width="880" height="480">

<br>

试了一下

<br>

````
chomd +x xxx.sh
./xxx.sh
````

<br>

到这里还是成功的，然后执行: /xxx.sh /var/log/nginx/error.log

，，，，


没有回显

没成功，先留在这里一下，以后回来了再看看