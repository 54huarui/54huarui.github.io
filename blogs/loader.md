# JAVA类加载器

<br><br><br>



Java 的类加载器（ClassLoader）是 Java 中的核心机制之一，它负责将 Java 字节码（class 文件）加载到 JVM 中，并定义类的运行时行为。

<br>

## Java程序的执行流程

<br>

![这是图片](/blogs/loader/0.png "Magic Gardens")

<br>

## classloader类中的方法

<br>

| 方法                                                    | 描述                                                                                                    |
|-------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| loadClass(String name)                                | 	加载指定名称的类，并返回对应的Class对象。这个方法使用双亲委派模型，从上至下依次尝试加载类。如果找不到类，则会抛出ClassNotFoundException异常。                 |
| findClass(String name)	                               | 查找并加载指定名称的类，并返回对应的Class对象。这个方法一般在自定义ClassLoader中重写，以实现自定义的类查找逻辑。如果找不到类，则需要抛出ClassNotFoundException异常。 |
| defineClass(String name, byte[] b, int off, int len)  | 	将字节数组转换为Java类的定义，并返回对应的Class对象。这个方法通常在自定义ClassLoader中被调用，用于加载已经获得的类字节码。                              |
|getParent()	| 获取当前ClassLoader的父级ClassLoader。ClassLoader在加载类时会首先委托给父级ClassLoader去加载。如果没有父级ClassLoader，则返回null。       |
|getSystemClassLoader()	|返回系统默认的ClassLoader。这是应用程序的默认ClassLoader，用于加载类路径上的类。|
|getClassLoader()	| 获取给定类的ClassLoader。这个方法可以用来获取任意类的ClassLoader，例如通过Class对象的getClassLoader()方法来获取该类的ClassLoader。|
|setDefaultAssertionStatus(boolean enabled)	| 设置类加载器的默认断言状态。断言状态决定由ClassLoader加载的类是否默认启用或禁用断言。|
|setPackageAssertionStatus(String packageName, boolean enabled)	| 设置指定包的断言状态。可以通过这个方法来控制指定包及其子包下的类是否启用或禁用断言。|
|setClassAssertionStatus(String className, boolean enabled)	| 设置指定类的断言状态。可以通过这个方法来控制指定类是否启用或禁用断言。|
|clearAssertionStatus()	| 清除类加载器的断言状态，将其重置为默认值。这会清除所有已设置的包和类的断言状态设置。|

  
<br>

如果需要加载自定义位置的类，例如从网络、加密文件中加载。此时可以通过继承 ClassLoader 类来自定义类加载器。

## 加载器们

<br>

| 加载器                   | 描述                                                                                                    |
|-----------------------|-------------------------------------------------------------------------------------------------------|
| Bootstrap Classloader |由原生代码（如C语言）编写，不继承自java.lang.ClassLoader。负责加载核心Java库，存储在<JAVA_HOME>/jre/lib目录中。|
| ExtClassLoader        |用来在<JAVA_HOME>/jre/lib/ext,或java.ext.dirs中指明的目录中加载 Java的扩展库。Java 虚拟机的实现会提供一个扩展库目录。该类加载器在此目录里面查找并加载 Java 类。该类由sun.misc.Launcher$ExtClassLoader实现。|
| AppClassLoader        |根据 Java应用程序的类路径（java.class.path或CLASSPATH环境变量）来加载 Java 类。一般来说，Java 应用的类都是由它来完成加载的。可以通过 ClassLoader.getSystemClassLoader()来获取它。该类由sun.misc.Launcher$AppClassLoader实现。|

<br>

## 双亲委派模型

<br>

当一个类加载器需要加载类时，首先将请求委托给父加载器处理。

如果父加载器无法找到该类，则由当前类加载器尝试加载。

这样做可以避免类的重复加载，并确保核心类（如 java.lang.String）不会被自定义类加载器覆盖。

![这是图片](/blogs/loader/1.png "Magic Gardens")


就我的理解而言，它是一层一层地将类传递上去的。首先类先进入UserClasssloader，UserClasssloader调用AppClassLoader加载，然后AppClassLoader将类传递给ExtClassLoader，ExtClassLoader通过方法findBootstrapClass()将请求委托给Bootstrap Classloader。如果Bootstrap Classloader无法加载类，则parent==null，Bootstrap Classloader就会向下传递给ExtClassLoader，同理再传递给AppClassLoader，如果AppClassLoader未能加载，就会将请求发回UserClasssloader 

事实上各个加载器之间并非父子的继承关系，而是组合的关系，只是加载委托的时候需要逐级传递，所以被翻译成了"双亲委派"的说法

<br>

## 类加载器的特性

<br>

* 用来确定类的唯一性。java通过一个二元组<N,L>来确定类的唯一性：
    * N:类的全限定名
    * L:加载定义这个类的类加载器ClassLoader

* 传递性
    * 类如果是由某加载器加载，那么它的依赖类也会由同一个加载器进行加载 
* 可见性
    * 当前类加载器可以直接或通过委派间接加载到父加载器，而父加载器不能直接或通过委派间接加载到当前加载器



