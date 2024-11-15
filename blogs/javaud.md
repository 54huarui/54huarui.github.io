# URLDNS链

<br>



## 序列化与反序列化

<br>

序列化：将对象变为一串字节码（一般hex的开头为AC ED 00 05），便于传输
反序列化：将序列化的字节码恢复为对象
序列化：

````
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
 
public class ser {
    public static void main(String[] args) throws IOException, IOException {
 
        student stu = new student();
        //将student类的序列化数据写入ser.txt
        ObjectOutputStream oos= new ObjectOutputStream(new FileOutputStream("ser.txt"));
        oos.writeObject(stu);
    }
}
````

反序列化：
````

import java.io.FileInputStream;
import java.io.IOException;
import java.io.ObjectInput;
import java.io.ObjectInputStream;
 
public class uns {
    public static void main(String a[]) throws IOException,ClassNotFoundException {
        ObjectInputStream ois = new ObjectInputStream(new FileInputStream(("ser.txt")));
        student o = (student) ois.readObject(); //readObject反序列化得到实例为Object类型
        System.out.println(o.getscore());
    }
}

````

## 安全问题

被序列化的对象的类中如果定义了readObject方法，则会使用类中的readObject方法来反序列化，readObject中只要有ois.defaultReadObject();(ois是传入的ObjectInputStream对象)就可以正常完成反序列化过程。

这时如果readObject方法中调用了其他类的危险函数，攻击者可以构造特殊的序列化数据，让readObject方法去执行这些类的函数。
比如反序列化这个unsafe类的对象后，就会执行弹计算机的命令

````
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.Serializable;
 
public class unsafe implements Serializable {
 
    private void readObject(ObjectInputStream ois) throws IOException, ClassNotFoundException{
        ois.defaultReadObject();
        new exec().calc();
    }
}
class exec {
    public void calc() throws IOException {
        Runtime.getRuntime().exec("calc");
    }
}
````

<br>

**为什么会有readobjectt方法？**

假设有个数组，他的长度为100，但是我们只填充了30个数掘，后面70个在进行序列化的时候仍然会被算进去，造成浪费。所以JDK给开发者提供了两种方法，能够让我们自定义序列化和反序列化的过程:writeboject()和readobject()

这两个方法是存放在传递类中的

那其实安全问题也就出来了，只要服务端反序列化数据，传递类中的readobject方法会自动执行，给予攻击者在服务器上运行代码的能力

即我们在类中自定义readobject方法，并在里面添加命令执行的代码如上。
