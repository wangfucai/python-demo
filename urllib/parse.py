from urllib.parse import urlparse
from urllib.parse import urljoin
from urllib.parse import urlencode

#urlparse对传入的url地址进行拆分
result = urlparse("www.baidu.com/index.html;user?id=5#comment", scheme="https")
print(result)

#urlunpars用于拼接

#urljoin拼接
print(urljoin('http://www.baidu.com', 'FAQ.html'))
print(urljoin('http://www.baidu.com', 'https://pythonsite.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html', 'https://pythonsite.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html', 'https://pythonsite.com/FAQ.html?question=2'))
print(urljoin('http://www.baidu.com?wd=abc', 'https://pythonsite.com/index.php'))
print(urljoin('http://www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com#comment', '?category=2'))

params = {
    "name": "zhaofan",
    "age": 23,
}
base_url = "http://www.baidu.com?"

url = base_url + urlencode(params)
print(url)