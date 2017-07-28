from urllib import request, error
import socket

#urllb异常这里有两个个异常错误：
#URLError,HTTPError，HTTPError是URLError的子类

#URLError里只有一个属性：reason,即抓异常的时候只能打印错误信息
try:
    response = request.urlopen("http://pythonsite.com/1111.html")
except error.URLError as e:
    print(e.reason)

try:
    response = request.urlopen("http://pythonsite.com/1111.html")
except error.HTTPError as e:
    print(e.reason)
    print(e.code)
    print(e.headers)
except error.URLError as e:
    print(e.reason)

else:
    print("reqeust successfully")

try:
    response = request.urlopen("http://www.pythonsite.com/",timeout=0.001)
except error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason, socket.timeout):
        print("time out")