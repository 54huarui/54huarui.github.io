# msf木马


<br><br>

## 环境：

* 被攻击机：vm虚拟机下的windows7(已经被扫描拥有永恒之蓝漏洞)
* 攻击机：kali(vm虚拟机下的kali)

<br>

## 操作:

<br>

先在kali机上生成木马

<br>

<img src="https://54huarui.github.io/blogs/zuoye5/1.png" width="880" height="480">

<br>

这里的木马使用的是反向代理reverse_tcp，由木马来访问攻击机实现数据传输。如果被攻击机不能出网，则木马不能直接访问攻击机，此时可以使用正向代理。

lhost:攻击机ip

lport：本地与木马的通讯端口

然后使用msf攻击win7，并且上传刚刚生成的payload.exe木马

<br>

<img src="https://54huarui.github.io/blogs/zuoye5/3.png" width="880" height="480">

<br>

<img src="https://54huarui.github.io/blogs/zuoye5/2.png" width="880" height="480">

<br>

在被攻击机上运行刚刚的程序

<br>

<img src="https://54huarui.github.io/blogs/zuoye5/5.png" width="880" height="480">

<br>

攻击机上使用msf的监听模块，监听刚刚的ip和端口，即可通过木马直接获得shell

<img src="https://54huarui.github.io/blogs/zuoye5/6.png" width="880" height="480">

<br>