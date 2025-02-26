# Log4j

<br>

## 写在前面

<br>

没想到不到一年我已经进步到能看得懂分析文章，再自己写文章的水平了。希望今年再接再厉吧，

<br>

## 利用

<br>

这里我用vulhub的容器搭建的，靶机地址为172.27.118.120

<br>

<img src="https://54huarui.github.io/blogs/fastjson2/2.png" width="880" height="480">

<br>

有个传入参数的点

````
http://172.27.118.120:8983/solr/admin/cores?action=
````

我还是刚刚用JNDI-Injection-Exploit起一个恶意服务器。

<br>

<img src="https://54huarui.github.io/blogs/fastjson2/3.png" width="880" height="480">

<br>


直接打poc即可

<br>

<img src="https://54huarui.github.io/blogs/fastjson2/1.png" width="880" height="480">

<br>

## 关于链子

