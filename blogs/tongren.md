# moectf铜人阵脚本

<br>

````
import requests
from bs4 import BeautifulSoup
import re
from requests.cookies import RequestsCookieJar


url = "http://127.0.0.1:49885/"
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
    "Referer": "http://127.0.0.1:63738/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "close"
}
data = {
    "player": "77",
    "direct": "弟子明白"
}

response = requests.post(url, headers=headers, data=data)

#print(response.status_code)
#print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
status_element = soup.find('h1', id='status')
status_text = status_element.get_text(strip=True)

# 从响应头中提取 Cookies
#cookies_text = response.cookies
cookies_text = str(response.cookies)

match = re.search(r'session=([a-zA-Z0-9._-]+)', cookies_text)
if match:
    session_cookie = match.group(1)
    print(f"{session_cookie}")
else:
    print("Session cookie not found")

print(f"{session_cookie}")

print(status_text)


def get_direction_description(directions):
    # 定义方位字典
    direction_map = {
        1: "北方",
        2: "东北方",
        3: "东方",
        4: "东南方",
        5: "南方",
        6: "西南方",
        7: "西方",
        8: "西北方"
    }

    # 去掉输入数据中的多余空白字符
    directions = directions.strip()

    try:
        # 处理单个数字的情况
        if ',' not in directions:
            direction = int(directions)
            return direction_map.get(direction, "无效输入")

        # 处理两个数字的情况
        direction_list = [int(d.strip()) for d in directions.split(',')]
        if len(direction_list) == 2:
            desc1 = direction_map.get(direction_list[0], "无效输入")
            desc2 = direction_map.get(direction_list[1], "无效输入")
            if desc1 == "无效输入" or desc2 == "无效输入":
                return "无效输入"
            return f"{desc1}一个，{desc2}一个"
        else:
            return "无效输入"
    except ValueError:
        return "无效输入"


# 测试代码
test_cases = [status_text]

for case in test_cases:
    print(f"{get_direction_description(case)}")


url = "http://127.0.0.1:49885/"
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
    "Referer": "http://127.0.0.1:63738/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": 'session='+f"{session_cookie}",
    "Connection": "close"
}
data = {
    "player": "77",
    "direct": get_direction_description(case)
}

response = requests.post(url, headers=headers, data=data)

#print(response.status_code)
#print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
status_element = soup.find('h1', id='status')
status_text = status_element.get_text(strip=True)

print(status_text)

#cookies_text = response.cookies
cookies_text = str(response.cookies)

match = re.search(r'session=([a-zA-Z0-9._-]+)', cookies_text)
if match:
    session_cookie = match.group(1)
    print(f"{session_cookie}")
else:
    print("Session cookie not found")

print(f"{session_cookie}")

print(status_text)



def get_direction_description(directions):
    # 定义方位字典
    direction_map = {
        1: "北方",
        2: "东北方",
        3: "东方",
        4: "东南方",
        5: "南方",
        6: "西南方",
        7: "西方",
        8: "西北方"
    }

    # 去掉输入数据中的多余空白字符
    directions = directions.strip()

    try:
        # 处理单个数字的情况
        if ',' not in directions:
            direction = int(directions)
            return direction_map.get(direction, "无效输入")

        # 处理两个数字的情况
        direction_list = [int(d.strip()) for d in directions.split(',')]
        if len(direction_list) == 2:
            desc1 = direction_map.get(direction_list[0], "无效输入")
            desc2 = direction_map.get(direction_list[1], "无效输入")
            if desc1 == "无效输入" or desc2 == "无效输入":
                return "无效输入"
            return f"{desc1}一个，{desc2}一个"
        else:
            return "无效输入"
    except ValueError:
        return "无效输入"


# 测试代码
test_cases = [status_text]

for case2 in test_cases:
    print(f"{get_direction_description(case2)}")

url = "http://127.0.0.1:49885/"
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
    "Referer": "http://127.0.0.1:63738/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": 'session='+f"{session_cookie}",
    "Connection": "close"
}
data = {
    "player": "77",
    "direct": get_direction_description(case2)
}

response = requests.post(url, headers=headers, data=data)


#print(response.status_code)
#print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
status_element = soup.find('h1', id='status')
status_text = status_element.get_text(strip=True)

print(status_text)

#cookies_text = response.cookies
cookies_text = str(response.cookies)

match = re.search(r'session=([a-zA-Z0-9._-]+)', cookies_text)
if match:
    session_cookie = match.group(1)
    print(f"{session_cookie}")
else:
    print("Session cookie not found")

print(f"{session_cookie}")

print(status_text)



def get_direction_description(directions):
    # 定义方位字典
    direction_map = {
        1: "北方",
        2: "东北方",
        3: "东方",
        4: "东南方",
        5: "南方",
        6: "西南方",
        7: "西方",
        8: "西北方"
    }

    # 去掉输入数据中的多余空白字符
    directions = directions.strip()

    try:
        # 处理单个数字的情况
        if ',' not in directions:
            direction = int(directions)
            return direction_map.get(direction, "无效输入")

        # 处理两个数字的情况
        direction_list = [int(d.strip()) for d in directions.split(',')]
        if len(direction_list) == 2:
            desc1 = direction_map.get(direction_list[0], "无效输入")
            desc2 = direction_map.get(direction_list[1], "无效输入")
            if desc1 == "无效输入" or desc2 == "无效输入":
                return "无效输入"
            return f"{desc1}一个，{desc2}一个"
        else:
            return "无效输入"
    except ValueError:
        return "无效输入"


# 测试代码
test_cases = [status_text]

for case2 in test_cases:
    print(f"{get_direction_description(case2)}")

url = "http://127.0.0.1:49885/"
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
    "Referer": "http://127.0.0.1:63738/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": 'session='+f"{session_cookie}",
    "Connection": "close"
}
data = {
    "player": "77",
    "direct": get_direction_description(case2)
}

response = requests.post(url, headers=headers, data=data)


#print(response.status_code)
#print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
status_element = soup.find('h1', id='status')
status_text = status_element.get_text(strip=True)

print(status_text)

#cookies_text = response.cookies
cookies_text = str(response.cookies)

match = re.search(r'session=([a-zA-Z0-9._-]+)', cookies_text)
if match:
    session_cookie = match.group(1)
    print(f"{session_cookie}")
else:
    print("Session cookie not found")

print(f"{session_cookie}")

print(status_text)



def get_direction_description(directions):
    # 定义方位字典
    direction_map = {
        1: "北方",
        2: "东北方",
        3: "东方",
        4: "东南方",
        5: "南方",
        6: "西南方",
        7: "西方",
        8: "西北方"
    }

    # 去掉输入数据中的多余空白字符
    directions = directions.strip()

    try:
        # 处理单个数字的情况
        if ',' not in directions:
            direction = int(directions)
            return direction_map.get(direction, "无效输入")

        # 处理两个数字的情况
        direction_list = [int(d.strip()) for d in directions.split(',')]
        if len(direction_list) == 2:
            desc1 = direction_map.get(direction_list[0], "无效输入")
            desc2 = direction_map.get(direction_list[1], "无效输入")
            if desc1 == "无效输入" or desc2 == "无效输入":
                return "无效输入"
            return f"{desc1}一个，{desc2}一个"
        else:
            return "无效输入"
    except ValueError:
        return "无效输入"


# 测试代码
test_cases = [status_text]

for case2 in test_cases:
    print(f"{get_direction_description(case2)}")

url = "http://127.0.0.1:49885/"
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
    "Referer": "http://127.0.0.1:63738/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": 'session='+f"{session_cookie}",
    "Connection": "close"
}
data = {
    "player": "77",
    "direct": get_direction_description(case2)
}

response = requests.post(url, headers=headers, data=data)


#print(response.status_code)
#print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
status_element = soup.find('h1', id='status')
status_text = status_element.get_text(strip=True)

print(status_text)

#cookies_text = response.cookies
cookies_text = str(response.cookies)

match = re.search(r'session=([a-zA-Z0-9._-]+)', cookies_text)
if match:
    session_cookie = match.group(1)
    print(f"{session_cookie}")
else:
    print("Session cookie not found")

print(f"{session_cookie}")

print(status_text)



def get_direction_description(directions):
    # 定义方位字典
    direction_map = {
        1: "北方",
        2: "东北方",
        3: "东方",
        4: "东南方",
        5: "南方",
        6: "西南方",
        7: "西方",
        8: "西北方"
    }

    # 去掉输入数据中的多余空白字符
    directions = directions.strip()

    try:
        # 处理单个数字的情况
        if ',' not in directions:
            direction = int(directions)
            return direction_map.get(direction, "无效输入")

        # 处理两个数字的情况
        direction_list = [int(d.strip()) for d in directions.split(',')]
        if len(direction_list) == 2:
            desc1 = direction_map.get(direction_list[0], "无效输入")
            desc2 = direction_map.get(direction_list[1], "无效输入")
            if desc1 == "无效输入" or desc2 == "无效输入":
                return "无效输入"
            return f"{desc1}一个，{desc2}一个"
        else:
            return "无效输入"
    except ValueError:
        return "无效输入"


# 测试代码
test_cases = [status_text]

for case2 in test_cases:
    print(f"{get_direction_description(case2)}")

url = "http://127.0.0.1:49885/"
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
    "Referer": "http://127.0.0.1:63738/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": 'session='+f"{session_cookie}",
    "Connection": "close"
}
data = {
    "player": "77",
    "direct": get_direction_description(case2)
}

response = requests.post(url, headers=headers, data=data)


#print(response.status_code)
#print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
status_element = soup.find('h1', id='status')
status_text = status_element.get_text(strip=True)

print(status_text)

````