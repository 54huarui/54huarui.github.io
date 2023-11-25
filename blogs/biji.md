## 笔记

<br><br>

* 在逆向(星号)((BYTE*)的时候用宏定义#define BYTE unsigned char即可正常使用

<br>

* system("tac flag.php")用来读取文件内容;

<br>

* ?c=system("tac%20fla(星号)")意思是c=system("tac flag");


* 文件包含漏洞--命令绕过


<br>

````
一般使用方法：

php://filter/ [read|write =]过滤器|过滤器/resource=要过滤的数据流 conversion filter(转换过滤器) convert.base64-encode & convert.base64-decode(base64加密解密) 例如：php://filter/convert.base64-encode/resource=flag.php

过滤器可以设置多个

php://filter读取源代码并进行base64编码输出，例如一些敏感信息会保存在php文件中，如果我们直接利用文件包含去打开一个PHP文件，PHP代码是不会显示到页面上的，例如：

他只显示了一条语句，这时我们可以以base64编码的方式读取指定文件的源码：

php://input协议

input协议可以访问请求的原始数据的制度刘，将post请求中的数据作为PHP代码执行。当传入的参数作为文件名打开时，可以将参数设为php://input，同时post想设置的文件内容，php执行时会将post内容作为文件内容，从而导致任意代码的执行。

利用该方法，我们可以直接写入php文件，输入file=php://input，然后用burp抓包，写入PHP代码：

data://text/plain协议

同样类似php://input，可以让用户来控制输入流，当它与包含函数结合时，用户输入的data://流会被当做php文件执行，从而导致任意代码执行。

利用data://伪协议可以直接达到执行php代码的效果，例如执行phpinfo();

格式：data://text/plain,流

例如：

data://text/plain,<?php phpinfo();?>
//如果此处对特殊字符进行了过滤，我们还可以通过base64编码后再输入：
data://text/plain;base64,PD9waHAgcGhwaW5mbygpPz4=




