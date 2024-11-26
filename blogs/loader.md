# JAVA类加载器

<br><br><br>



Java 的类加载器（ClassLoader）是 Java 中的核心机制之一，它负责将 Java 字节码（class 文件）加载到 JVM 中，并定义类的运行时行为。

<br>

## Java程序的执行流程

<br>

<img src="https://54huarui.github.io/blogs/loader/0.png" width="880" height="480">

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
