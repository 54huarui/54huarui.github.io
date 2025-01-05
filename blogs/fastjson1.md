# fastjson反序列化

<br>

## 版本1.2.80

<br>


## 题目源码

<br>

````
package demo.Controller;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class JsonController {
    @RequestMapping(value={"/json"}, method={RequestMethod.POST})
    public String json(String json) {
        JSONObject jsonObject = null;
        try {
            jsonObject = JSON.parseObject((String)json);
            return jsonObject.toJSONString();
        }
        catch (Exception e) {
            e.printStackTrace();
            return "error";
        }
    }
}
````

<br>

平平无奇的源码，值得注意的是因为用了 @RequestMapping注解，所以它是从表单里面获取一个名叫json的键，然后值才是json格式（逆天题目设计，害得我捣鼓了半天，最后在本地跑了才发现端倪）

## 1.2.80特性

<br>

先跳过，后面再补充

<br>


<br>

## 题目


<br>


这里拿到源码JsonController.class和pom.Xml
可知这里接收一个json，并被fastjson反序列化。Fastjson的版本为1.2.80,环境只有commons-io和org.javassist依赖



