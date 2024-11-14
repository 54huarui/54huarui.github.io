# java反射

<br>


## 写在前面

<br>

最近花了很长的时间去学习java，前后把Java se ，Java web，spring boot都搞了一遍(还搞了个springboot项目当练手)：
[Bilibili-Film-Area-top-webcrawler](https://github.com/54huarui/Bilibili-Film-Area-top-webcrawler)。现在终于有心回来搞安全了

<br>

最近打算开始学链子的内容，从反射开始一步一步走。反正考完数电无事可做，就当是消磨时间了

<br>

## 举例

<br>

例子:

````
public class testForName {
    public static void main(String args[]) throws ClassNotFoundException, NoSuchMethodException {
        Class c = Class.forName("student");
        Class c1 = new student(2,"wm").getClass();
        Class c2 = student.class;
        //c,c1,c2指向同一个Class对象
        System.out.println(c2.getMethod("getName"));
 
        Class c3 = c.getSuperclass();
        System.out.println(c3.getMethod("getJob"));
    }
}
 
class person{
    private String job = "工人";
 
    public String getJob() {
        return job;
    }
 
    public void setJob(String job) {
        this.job = job;
    }
}
class student extends person{
    private int id = 0;
    private String name = "mak";
 
    public int getId() {
        return id;
    }
 
    public String getName() {
        return name;
    }
 
    public student(int id, String name) {
        this.id = id;
        this.name = name;
    }
 
    public void setId(int id) {
        this.id = id;
    }
 
    @Override
    public String toString() {
        return "student{" +
                "id=" + id +
                ", name='" + name + '\'' +
                '}';
    }
}

````

---------------------------------------

<br>

## **获取Class对象:**

<br>

### 1.通过类名

````
Class c = Class.forName("student");
````

Class.forName("类名") 即后文的student类

<br>

### 2.通过实例

````
Class c1 = new student(2,"wm").getClass();
````

这里是通过Object的getClass方法获得一个对象对应的类的Class对象。大概意思就是通过一个实例化之后的对象找到对应的class对象，有点绕

<br>

### 3.通过类名.class

````
Class c2 = student.class;
````

和第一种方法差不多，如果有新的理解我再补充

<br>

## **获取对象中的方法:**

<br>

````
System.out.println(c2.getMethod("getName"))
````

通过getMethod方法获取 student 类中的 getName 方法。

<br>

获取父类的方法
````
Class c3 = c.getSuperclass();
System.out.println(c3.getMethod("getJob"));

````

c.getSuperclass()意思是获取 student 的父类 Class 对象，这里是 person 类。
通过getMethod方法在 person 类中获得 getJob 方法。

<br>

## 操作对象

<br>

接下来以这个类来举例

````
class student {
    private int id = 0;
    private String name = "mak";
 
    public int getId() {
        return id;
    }
 
    public String getName() {
        return name;
    }
 
    public student(int id, String name) {
        this.id = id;
        this.name = name;
    }
 
    public void setName(String name) {
        this.name = name;
    }
 
    public void setId(int id) {
        this.id = id;
    }
 
    void test(String name){
        System.out.println("hello,"+this.name+" and "+name);
    }
 
    @Override
    public String toString() {
        return "student{" +
                "id=" + id +
                ", name='" + name + '\'' +
                '}';
    }
}
````

<br>

## 通过反射创造对象：

<br>

````
Class stuclass = Class.forName("student");
student stu = (student)stuclass.newInstance();
````

首先是获取 student 类的 Class 对象，这个在前面有讲，不在叙述。
student stu = (student)stuclass.newInstance(); 这句话的目的其实是创建一个student类的一个名叫stu实例。
stuclass.newInstance()会通过 student 类的无参构造函数来创建一个 student 类的对象。这里要求 student 类必须有一个无参构造函数。而newInstance() 返回一个 Object 类型，所以需要进行类型转换 (student)，将返回的对象强制转换为 student 类型。

<br>

## 通过反射创造带参构造器的对象：

<br>

````
Constructor constr = stuclass.getConstructor(int.class,String.class); //获取类的构造器，参数：构造器参数类型的class
student stu1 = (student) constr.newInstance(12,"Tom");
````

stuclass.getConstructor(int.class, String.class) 用于获取 student 类中接受 int 和 String 两个参数的构造函数。

这里对应了例子中的:
````
    public student(int id, String name) {
        this.id = id;
        this.name = name;
    }
````
关于Constructor 对象：

Constructor 对象是 Java 反射机制中的一部分，用于表示类的构造函数。它的存在是为了提供一种方式，允许程序在运行时动态地访问和使用构造函数创建对象实例。与 Method 对象（用于表示普通方法）类似，Constructor 对象专门负责构造函数的管理。

<br>

## 执行对象方法

<br>

````
Method stname = stuclass.getMethod("setName", String.class); //获取类的方法，参数：方法名,方法参数类型的Class
stname.invoke(stu1,"wm"); //invoke(激活):执行函数，参数：(用于执行函数的对象，函数参数)
Method hello = stuclass.getDeclaredMethod("test", String.class);
hello.invoke(stu1,"abc");
````

stuclass.getMethod("setName", String.class)：从 stuclass（即 student 类的 Class 对象）中获取 setName 方法。
getMethod() 的第一个参数是方法名，第二个参数是方法的参数类型

stname.invoke(stu1, "wm")：通过反射调用 stname 方法，即调用 stu1 对象的 setName 方法，并传入参数 "wm"。

hello方法同理，不在叙述


## 操作对象属性

<br>

````
Field stuid = stuclass.getDeclaredField("name");
stuid.setAccessible(true); //对于修改private属性，要先关闭程序安全检测（默认为true）
stuid.set(stu1,"wm1111"); //set修改，参数：要修改属性的对象,修改后的值
hello.invoke(stu1,"def");
````

通过反射来访问并修改 student 类的私有属性 name，然后再次调用 test 方法

stuclass.getDeclaredField("name")：从 stuclass（即 student 类的 Class 对象）中获取 name 字段（即属性）

关于set方法：

set() 方法不是 Class 类，而是 Field 类 的方法。Field 类在 java.lang.reflect 包中，用于表示类的属性（字段）。通过 Field 对象的 set() 方法，可以为特定对象的字段设置值。

<br>

## 写在后面

<br>

唉，体测