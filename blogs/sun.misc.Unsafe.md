# sun.misc.Unsaf

<br>

## 简介

<br>

sun.misc.Unsafe是Java底层API(仅限Java内部使用,反射可调用)提供的一个神奇的Java类，Unsafe提供了非常底层的内存、CAS、线程调度、类、对象等操作、Unsafe正如它的名字一样它提供的几乎所有的方法都是不安全的，本节只讲解如何使用Unsafe定义Java类、创建类实例。

>人如其名，这是一个很危险的类，偶然看到一篇文章，觉得很有趣，就顺手记录了下来

