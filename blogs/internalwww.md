# ctfshow内网渗透复现

<br>

## 复现过程

<br>

先放一下ssh常用命令:

````
ssh ctfshow@pwn.challenge.ctf.show -p 28169       #用于ssh连接题目shell
scp -r 1.php ctfshow@pwn.challenge.ctf.show:28169 /tmp  #用于上传东西
````

### 1.根据提示寻找有用的工具

<br>

题目提示我们攻击机有工具，利用find命令可以找到

````
find / -name metasploit-framework
````

<img src="https://54huarui.github.io/blogs/internalwww/1.png" width="880" height="480">

<br>

### 2.扫描

<br>

因为是内网渗透，所以还是要做一些扫描。

上传fscan并扫描内网
````
scp -r 1.php ctfshow@pwn.challenge.ctf.show:28169 /tmp
ifconfig           #查看ip
./fscan -h 172.2.162.4/24 -o fscan.log #扫描

````


<img src="https://54huarui.github.io/blogs/internalwww/2.png" width="880" height="480">



<br>






















<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>



## 写在前面

有些东西不好明说，但是那种感觉又回来了。再不调整自己就得落得不好的下场
