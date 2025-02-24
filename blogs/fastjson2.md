# Fastjson 1.2.24 RCE

<br>

-------------------------------

## 环境

<br>

**JDK&java**：1.8

**依赖**：fastjson1.2.24




## 写在前面

<br>

后续会更新相应的利用到[54huarui/fastjsonfileread-test-exp](https://github.com/54huarui/fastjsonfileread-test-exp)

参考/致谢 ：

[www.cnblogs.com/EddieMurphy-blogs](https://www.cnblogs.com/EddieMurphy-blogs/p/18064168)

<br>

---------------------------

## 关于Fastjson

<br>

Fastjson 的反序列化是指将 JSON 格式的字符串转换为 Java 对象的过程。它通过   JSON.parseObject()   方法实现，支持将 JSON 数据映射到 Java 的普通类、集合、映射等多种数据结构


解析Fastjson 内部使用一个解析器（ DefaultJSONParser ）将 JSON 字符串分解为一个个字段。解析器会逐字符读取 JSON 数据，识别出键值对、数组、嵌套对象等结构。

Fastjson 根据目标类的类型信息，通过反射机制加载对应的 Java 类。如果 JSON 数据中包含   @type   字段，Fastjson 会根据   @type   的值动态加载指定的类。例如：

````

{"@type": "com.example.User", "name": "John", "age": 30}

````

在反序列化时，Fastjson 会加载   com.example.User   类，并创建其实例。



fastjson在序列化以及反序列化的过程中并没有使用Java自带的序列化机制，而是自定义了一套机制。其实，对于JSON框架来说，想要把一个Java对象转换成字符串，可以有两种选择：

1.基于setter/getter

2.基于属性（AutoType）

基于setter/getter会带来什么问题呢，下面举个例子，假设有如下两个类：

````
class Apple implements Fruit {
    private Big_Decimal price;
    //省略 setter/getter、toString等
}
````

````
class iphone implements Fruit {
    private Big_Decimal price;
    //省略 setter/getter、toString等
}
````
实例化对象之后，假设苹果对象的price为0.5，Apple类对象序列化为json格式后为：
````
{"Fruit":{"price":0.5}}
````
假设iphone对象的price为5000,序列化为json格式后为：
````
{"Fruit":{"price":5000}}
````
当一个类只有一个接口的时候，将这个类的对象序列化的时候，就会将子类抹去（apple/iphone）只保留接口的类型(Fruit)，最后导致反序列化时无法得到原始类型。本例中，将两个json再反序列化生成java对象的时候，无法区分原始类是apple还是iphone。

为了解决上述问题： fastjson引入了基于属性（AutoType），即在序列化的时候，先把原始类型记录下来。使用@type的键记录原始类型，在本例中，引入AutoType后，Apple类对象序列化为json格式后为：
````
{ "fruit":{ "@type":"com.hollis.lab.fastjson.test.Apple", "price":0.5 } }
````
引入AutoType后，iphone类对象序列化为json格式后为：
````
{ "fruit":{ "@type":"com.hollis.lab.fastjson.test.iphone", "price":5000 } }
````
这样在反序列化的时候就可以区分原始的类了。


 

使用AutoType功能进行序列号的JSON字符会带有一个@type来标记其字符的原始类型，在反序列化的时候会读取这个@type，来试图把JSON内容反序列化到对象，并且会调用这个库的setter或者getter方法，然而，@type的类有可能被恶意构造，只需要合理构造一个JSON，使用@type指定一个想要的攻击类库就可以实现攻击。

常见的有sun官方提供的一个类com.sun.rowset.JdbcRowSetImpl，其中有个dataSourceName方法支持传入一个rmi的源，只要解析其中的url就会支持远程调用！因此整个漏洞复现的原理过程就是：

````
1、攻击者（我们）访问存在fastjson漏洞的目标靶机网站，通过burpsuite抓包改包，以json格式添加com.sun.rowset.JdbcRowSetImpl恶意类信息发送给目标机。
2、存在漏洞的靶机对json反序列化时候，会加载执行我们构造的恶意信息(访问rmi服务器)，靶机服务器就会向rmi服务器请求待执行的命令。也就是靶机服务器问rmi服务器，（靶机服务器）需要执行什么命令啊？
3、rmi 服务器请求加载远程机器的class（这个远程机器是我们搭建好的恶意站点，提前将漏洞利用的代码编译得到.class文件，并上传至恶意站点），得到攻击者（我们）构造好的命令（ping dnslog或者创建文件或者反弹shell啥的）
4、rmi将远程加载得到的class（恶意代码），作为响应返回给靶机服务器。
靶机服务器执行了恶意代码，被攻击者成功利用。
````

<br>

## 利用

<br>

