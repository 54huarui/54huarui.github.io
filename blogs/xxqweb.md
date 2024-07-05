# 小学期web题

<br>


## ezz_rce

<br>

````
<?php
show_source(__FILE__);
error_reporting(0);
$a=$_GET['shell'];
$b=$_GET;
$c=$_POST['cmd'];
function waf($c){
    if(preg_match("/cat|flag/is",$c)) {
        exit('不是哥们');
    }}

if(isset($b) and isset($c)){
    waf($c);
    call_user_func($a,$b)($c);
}else{
exit('这是一个简单的传参?');} 这是一个简单的传参?
````
思路就是使得call_user_func($a,$b)变成system，最后的($c)就可以填入命令了

call_user_func($a,$b)($c);

用到一个特别的函数:

````
array_pop()

作用: 弹出数组最后一个元素。
用法:
php

$stack = ["orange", "banana", "apple", "raspberry"];
$fruit = array_pop($stack);
print_r($stack);
解释: array_pop() 函数删除数组的最后一个元素并返回该元素。

````

所以直接使得shell=system即可


<br>

## ez_rce

<img src="https://54huarui.github.io/blogs/xxq/1.png" width="880" height="480">

