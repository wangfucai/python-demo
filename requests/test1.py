import requests
import json

response = requests.get("https://www.baidu.com")
print(type(response))
print(response.status_code)
print(type(response.text))
#print(response.text)
print(response.cookies)
#print(response.content)
#print(response.content.decode("utf-8"))

#response = requests.get("http://www.baidu.com")
#response.encoding="utf-8"
#print(response.text)

requests.post("http://httpbin.org/post")
requests.put("http://httpbin.org/put")
requests.delete("http://httpbin.org/delete")
requests.head("http://httpbin.org/get")
requests.options("http://httpbin.org/get")

data = {
    "name":"zhaofan",
    "age":22
}
response = requests.get("http://httpbin.org/get",params=data)
print(response.url)
print(response.text)

#解析json
response = requests.get("http://httpbin.org/get")
print(type(response.text))
print(response.json())
print(json.loads(response.text))
print(type(response.json()))

