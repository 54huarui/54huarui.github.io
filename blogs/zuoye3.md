# qq9同一子网内文件传输

<br>

## 作业步骤

<br>

使得手机和电脑qq处于同一局域网下

<br>

pc端的wireshark开启监听

<br>

<img src="https://54huarui.github.io/blogs/zuoye3/6.png" width="880" height="480">

<br>

手机发送图片给电脑端接收

<br>

<img src="https://54huarui.github.io/blogs/zuoye3/7.jpg" width="880" height="480">

<br>


监听结束，抓包后搜索jpg特征头FF D8

<br>

<img src="https://54huarui.github.io/blogs/zuoye3/1.png" width="880" height="480">

<br>

右键追踪字节流，另存为1.jpg



<br>

<img src="https://54huarui.github.io/blogs/zuoye3/2.png" width="880" height="480">

<br>


打开HEX Editor，找到应提取出来的jpg图片

<br>

<img src="https://54huarui.github.io/blogs/zuoye3/3.png" width="880" height="480">

<br>

将其他无关部分直接删除

<br>

<img src="https://54huarui.github.io/blogs/zuoye3/4.png" width="880" height="480">

<br>

另存为并且打开，和手机上发送的图片一致。

<br>

<img src="https://54huarui.github.io/blogs/zuoye3/5.png" width="880" height="480">

<br>