# SST

<br>

## Flask模板注入

ssti服务端模板注入，ssti主要为python的一些框架 jinja2 mako tornado django，PHP框架smarty twig，java框架jade velocity等等使用了渲染函数时，由于代码不规范或信任了用户输入而导致了服务端模板注入，模板渲染其实并没有漏洞，主要是程序员对代码不规范不严谨造成了模板注入漏洞，造成模板可控。本文着重对flask模板注入进行浅析。

<br>

### 模板渲染

让我们用例子来简析模板渲染。

````
<html>
<div>{$what}</div>
</html>
````

我们想要呈现在每个用户面前自己的名字。但是{$what}我们不知道用户名字是什么，用一些url或者cookie包含的信息，渲染到what变量里，呈现给用户的为

````
<html>
<div>张三</div>
</html>
````

当然这只是最简单的示例，一般来说，至少会提供分支，迭代。还有一些内置函数。

<br>

### 重要函数

#### render_template函数

<img src="https://54huarui.github.io/blogs/falsk/p1.png" class="floatpic" width="880" height="480">

#### regquest.arg.get('a')函数

通过get的方式获得请求

#### render_template_string函数

多用于ctf赛题里，用于渲染字符串，可以直接定义网页内容
<img src="https://54huarui.github.io/blogs/falsk/p3.png" class="floatpic" width="880" height="480">

#### url_for()函数

用来构建url

#### redirect()函数

用来重定向网站


<br>


### 成因

例子：

````
<html>
  <head>
    <title>{{title}} - 小猪佩奇</title>
  </head>
 <body>
      <h1>Hello, {{user.name}}!</h1>
  </body>
</html>
````

里面有两个参数需要我们渲染，user.name，以及title

我们在app.py文件里进行渲染。


````
@app.route('/')
@app.route('/index')#我们访问/或者/index都会跳转
def index():
   return render_template("index.html",title='Home',user=request.args.get("key"))
````
