# Servlet

<br><br>

## web.xml

<br>

<img src="https://54huarui.github.io/blogs/servlet/1.png" width="880" height="480">

<br>

在 web.xml 中，Servlet 的配置在 Servlet 标签中，Servlet 标签是由 Servlet 和
Servlet-mapping 标签组成，两者通过在 Servlet 和 Servlet-mapping 标签中相同的
Servlet-name 名称实现关联，在图 4-3 中的标签含义如下。

● <servlet>：声明 Servlet 配置入口。

● <description>：声明 Servlet 描述信息。

● <display-name>：定义 Web 应用的名字。

● <servlet-name>：声明 Servlet 名称以便在后面的映射时使用。

● <servlet-class>：指定当前 servlet 对应的类的路径。

● <servlet-mapping>：注册组件访问配置的路径入口。

● <servlet-name>：指定上文配置的 Servlet 的名称。

● <url-pattern>：指定配置这个组件的访问路径。

## Servlet 注解

<br>

<img src="https://54huarui.github.io/blogs/servlet/2.png" width="880" height="480">

<br>


Servlet 3.0 以上的版本中，开发者无须在 web.xml 里面配置 Servlet，只需要添加
@WebServlet 注解即可修改 Servlet 的属性



## Servlet 的生命周期

<br>

当用户第一次向服务器发起请求时，服务器会解析用户的请求，此时容器会加载 Servlet，然后创建 Servet 实例，再调用 init() 方法初始化 Servlet，紧接着调用服务的 service() 方法去处理用户 GET、POST 或者其他类型的请求。当执行完 Servlet 中对应 class 文件的逻辑后，将结果返回给服务器，服务器再响应用户请求。当服务器不再需要 Servlet 实例或重新载入 Servlet 时，会调用 destroy() 方法，借助该方法，Servlet 可以释放掉所有在 init()方法中申请的资源。
