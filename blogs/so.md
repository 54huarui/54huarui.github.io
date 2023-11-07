## 攻防世界 RE-666

<br><br>

**这里用极客大联盟的安卓题为示例**

<br>

**打开程序，这道题主要是让我们砍树，砍了很多遍才允许我们验证flag**

<img src="https://54huarui.github.io/blogs/so jpg/7.png" width="880" height="480">


**开局直入主题，打开MainActivity，发现按钮事件**

<img src="https://54huarui.github.io/blogs/so jpg/1.png" width="880" height="480">

**当我们砍树了777次之后，就会将我们传入的text和"Sycloveforerver"一起传入一个叫MainActivity.l0o0l的函数**

<br>

**我们点入MainActivity.l0o0l这个函数看一下**

<br>

<img src="https://54huarui.github.io/blogs/so jpg/2c.png" width="880" height="480">

<br>

**这里明显有一个调用so的特征。这里科普一下so**

*开发Android应用时，有时候Java层的编码不能满足实现需求，就需要到C/C++实现后生成SO文件，再用System.loadLibrary()加载进行调用，成为JNI层的实现。常见的场景如：加解密算法，音视频编解码等。在生成SO文件时，需要考虑适配市面上不同手机CPU架构，而生成支持不同平台的SO文件进行兼容。目前Android共支持七种不同类型的CPU架构，分别是：ARMv5，ARMv7 (从2010年起)，x86 (从2011年起)，MIPS (从2012年起)，ARMv8，MIPS64和x86_64 (从2014年起)

so库一般是程序里面核心代码块，通过Android提供的NDK技术将核心代码用安全性更高的C/C++语言实现并提供给Java层调用来保证程序核心代码的安全。*

<br>


**so层的特征就是System.loadLibrary()，类似于其他语言中的文件包含，第三方库这种**

<br>

**解压这个安卓apk，用压缩软件解压apk，在相应的地方用ida打开so文件**

<br>

<img src="https://54huarui.github.io/blogs/so jpg/13.png" width="880" height="480">

<br>


**点开之后搜索可以看到一个关键函数**

<br>

<img src="https://54huarui.github.io/blogs/so jpg/4c.png" width="880" height="480">

<br>

**因为看不到我们到底是传入这个函数的哪个参数，大胆推测我们传入的flag为图中的a1,"Sycloveforerver"为图中的a2**


**根据常规逆向的思路去构造这道题的解题脚本，完成后讲结果转字符串**


<br>



<br>

**总结：so层的考法明显特征**