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

接下来以这个

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