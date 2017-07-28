import requests
from requests.auth import HTTPBasicAuth
from requests.exceptions import ReadTimeout,ConnectionError,RequestException

#文件上传
#files= {"files":open("git.jpeg","rb")}
#response = requests.post("www.baidu.com")
#print(response.text)

#获取cookie
response = requests.get("http://www.baidu.com")
print(response.cookies)

for key, value in response.cookies.items():
    print(key + "=" + value)

#cookie的一个作用就是可以用于模拟登陆，做会话维持
s = requests.Session()
s.get("http://httpbin.org/cookies/set/number/123456")
response = s.get("http://httpbin.org/cookies")
print(response.text)

#证书验证

#认证设置
response = requests.get("http://cdc.server.nubia.cn/border",auth=HTTPBasicAuth("nubia","nubiacdc"))
print(response.status_code)

#异常处理
try:
    response = requests.get("http://httpbin.org/get",timeout=0.1)
    print(response.status_code)
except ReadTimeout:
    print("timeout")
except ConnectionError:
    print("connection Error")
except RequestException:
    print("error")