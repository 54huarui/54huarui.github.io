# basectf数学大师脚本

<br>

# 脚本：
````
import requests
from bs4 import BeautifulSoup
import re
from requests.cookies import RequestsCookieJar

result = 1
session_cookie = 1
for i in range(50):

    url = "http://challenge.basectf.fun:35901/"
    headers = {
        "Cache-Control": "max-age=0",
        "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "Upgrade-Insecure-Requests": "1",
        "Origin": "http://127.0.0.1:63738",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Cookie": 'PHPSESSID='+f"{session_cookie}",
        "Referer": "http://127.0.0.1:63738/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "close"
    }
    data = {
        "answer": f"{result}",
    }

    response = requests.post(url, headers=headers, data=data)

    print(response.text)


    match = re.search(r'me in 3 second (.+?)\?', response.text)
    if match:
        expression = match.group(1)
        expression = expression.replace('×', '*').replace('÷', '/')
        result = eval(expression)
        result = round(float(result))
        print(result)

    cookies_text = str(response.cookies)

    print(cookies_text)

    # 示例 CookiesJar
    match = re.search(r'PHPSESSID=([a-zA-Z0-9]+)', cookies_text)

    if match:
        phpsessid_value = match.group(1)
        print(phpsessid_value)  # 输出: r6vfuu1vs0ij7sf6saa8576lk8
        session_cookie = phpsessid_value


````