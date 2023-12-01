## Somebody-内存取证



<br><br>

**下载文件得到一个vmem后缀，用内存取证工具volatility-master打开**

**先使用python2 vol.py -f body.vmem imageinfo获得profile信息**

<br><br>


<img src="https://54huarui.github.io/blogs/somebody jpg/1.png" width="880" height="480">

<br><br>


**根据提示，知道桌面放东西，然后使用 python2 vol.py -f body.vmem --profile=Win7SP1x64 filescan | grep "Desktop" 查找和桌面有关的东西**

<br><br>

<img src="https://54huarui.github.io/blogs/somebody jpg/2.png" width="880" height="480">

<br><br>

**找到可以的flag.zip和anything.zip，直接使用python2 vol.py -f body.vmem --profile=Win7SP1x64 dumpfiles -Q 0x000000007fa7b9c0 -D ./    指令提取，得到的flag.zip是没用的，而anything.zip文件是加密的，在winrar可以看到提示**

<br><br>

<img src="https://54huarui.github.io/blogs/somebody jpg/3.png" width="880" height="480">

<br><br>

**根据提示查找这台机子的密码**

<br><br>

<img src="https://54huarui.github.io/blogs/somebody jpg/4.png" width="880" height="480">

<br><br>

**根据提示：哈希即可，把这四个哈希密码放到zip尝试，最后一个哈希密码正确了。**

<br><br>

<img src="https://54huarui.github.io/blogs/somebody jpg/5.png" width="880" height="480">