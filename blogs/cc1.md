# RMI

<br>

## 写在前面

<br>

RMI实现,缝缝补补一些知识

## 环境

<br>

jdk20 

java.rmi

## 简要

<br>

RMI 是 Java 提供的一个完善的简单易用的远程方法调用框架，采用客户/服务器通信方式，在服务器上部署了提供各种服务的远程对象，客户端请求访问服务器上远程对象的方法，它要求客户端与服务器端都是 Java 程序。

一般来说，RMI的实现需要三种角色:

* 客户端
* 服务端
* 注册中心

<br>

## 过程

<br>

#### 1.定义远程接口



首先需要定义一个远程接口,它必须继承自java.rmi.Remote接口，并且所有方法都必须声明抛出RemoteException。
这段代码发生在服务端
````

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface RemoteInterface extends Remote {
    String sayHello(String name) throws RemoteException;
}

````

<br>

#### 2. 实现远程接口



远程实现类需要实现远程接口，并且必须继承自  java.rmi.server.UnicastRemoteObject  类。  UnicastRemoteObject  类提供了远程对象的基本功能。

````

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class RemoteImplementation extends UnicastRemoteObject implements RemoteInterface {
    protected RemoteImplementation() throws RemoteException {
        super(); // 必须调用父类的构造方法
    }

    @Override
    public String sayHello(String name) throws RemoteException {
        return "Hello, " + name + "! This is a remote call.";
    }
}
````

<br>

#### 3. 创建RMI服务器



RMI服务器负责注册远程对象，并将其暴露给客户端。服务器需要使用java.rmi.registry.LocateRegistry和java.rmi.registry.Registry来注册远程对象。

````
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class RMIServer {
    public static void main(String[] args) {
        try {
            // 创建远程对象实例
            RemoteInterface remoteObject = new RemoteImplementation();

            // 注册远程对象到RMI注册表
            Registry registry = LocateRegistry.createRegistry(1099); // 默认端口为1099
            registry.rebind("HelloService", remoteObject); // 绑定远程对象到名称

            System.out.println("RMI Server is running...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
````

<br>

#### 4. 创建RMI客户端

客户端通过RMI注册表查找远程对象，并调用其方法。

````
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class RMIClient {
    public static void main(String[] args) {
        try {
            // 查找远程对象
            Registry registry = LocateRegistry.getRegistry("localhost", 1099); // 默认端口为1099
            RemoteInterface remoteObject = (RemoteInterface) registry.lookup("HelloService");

            // 调用远程方法
            String result = remoteObject.sayHello("huarui");
            System.out.println(result);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
````

#### 5.编译运行

将所有Java文件（  RemoteInterface.java  、  RemoteImplementation.java  、  RMIServer.java  、  RMIClient.java  ）放在同一个目录下，然后编译

````
javac *.java

java RMIServer

java RMIClient
````

如果代码正常就会输出

````
Hello, huarui! This is a remote call.
````