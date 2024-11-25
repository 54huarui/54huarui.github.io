---
layout: page
---




# JAVA笔记

<br><br>


## 接口的声明
````
public interface Transformer {
    public Object transform(Object input);
}
````

这里的interface指的是接口，不是类

## 关于Object类型：


Object 的特点
通用类型：

一个变量或参数声明为 Object 类型时，它可以引用任何对象类型的实例，例如 String、Integer、List 等。
多态性：

由于 Object 是所有类的基类，使用 Object 类型可以编写通用代码，适用于任何对象类型。
但是，使用时需要将其 向下转型 成具体类型才能调用子类特有的方法。
不能表示原始数据类型：

原始数据类型（int、double 等）无法直接用 Object 表示，但可以通过它们的 包装类（如 Integer、Double 等）来间接使用。

示例用法
````
public class Main {
    public static void main(String[] args) {
        Object obj = "Hello, World!"; // Object 类型可以引用 String 对象
        System.out.println(obj);      // 调用 toString() 方法，输出: Hello, World!

        Object number = 42;           // Object 类型可以引用 Integer 对象
        System.out.println(number);   // 调用 toString() 方法，输出: 42
    }
}

````

向下转型
当 Object 引用一个具体类型的对象时，需要显式地将其 向下转型 到具体类型以访问该类特有的方法。

````
public class Main {
    public static void main(String[] args) {
        Object obj = "Hello, World!"; // Object 类型
        if (obj instanceof String) { // 检查类型
            String str = (String) obj; // 向下转型
            System.out.println(str.toUpperCase()); // 调用 String 特有方法
        }
    }
}
````

---