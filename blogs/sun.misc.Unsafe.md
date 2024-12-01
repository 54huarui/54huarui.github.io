# sun.misc.Unsaf

<br>

## 简介

<br>

sun.misc.Unsafe是Java底层API(仅限Java内部使用,反射可调用)提供的一个神奇的Java类，Unsafe提供了非常底层的内存、CAS、线程调度、类、对象等操作、Unsafe正如它的名字一样它提供的几乎所有的方法都是不安全的。

>人如其名，这是一个很危险的类，偶然看到一篇文章，觉得很有趣，就顺手记录了下来

## 特点

<br>

Unsafe类是一个不能被继承的类且不能直接通过new的方式创建Unsafe类实例，如果通过getUnsafe方法获取Unsafe实例还会检查类加载器，默认只允许Bootstrap Classloader调用。

既然无法直接通过Unsafe.getUnsafe()的方式调用，那么可以使用反射的方式去获取Unsafe类实例。

<br>

## 获取Unsafe对象

<br>

反射获取。老朋友了,不多叙述

````
// 反射获取Unsafe的theUnsafe成员变量
Field theUnsafeField = Unsafe.class.getDeclaredField("theUnsafe");

// 反射设置theUnsafe访问权限
theUnsafeField.setAccessible(true);

// 反射获取theUnsafe成员变量值
Unsafe unsafe = (Unsafe) theUnsafeField.get(null);
````

或者

````
// 获取Unsafe无参构造方法
Constructor constructor = Unsafe.class.getDeclaredConstructor();

// 修改构造方法访问权限
constructor.setAccessible(true);

// 反射创建Unsafe类实例，等价于 Unsafe unsafe1 = new Unsafe();
Unsafe unsafe1 = (Unsafe) constructor.newInstance();
````

<br>

## allocateInstance无视构造方法创建类

<br>

假设我们有一个类xxx，因为某种原因我们不能直接通过反射的方式去创建UnSafeTest类实例，那么这个时候使用Unsafe的allocateInstance方法就可以绕过这个限制了。

````
public class xxx {

   private xxx() {
      // 假设RASP在这个构造方法中插入了Hook代码，我们可以利用Unsafe来创建类实例
      System.out.println("init...");
   }

}

````
<br>

使用Unsafe创建UnSafeTest对象：

````
// 使用Unsafe创建UnSafeTest类实例
xxx test = (xxx) unsafe1.allocateInstance(xxx.class);
````

## 本文部分代码摘自网络文章