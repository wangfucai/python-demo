import re

#re.match()尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match（）就会返回None
#语法格式：re.match(pattern,string,flags=0)
#result.group()获取匹配的结果
#result.span()获取匹配字符串的长度范围
content = "hello 123 4567 World_This is a regex Demo"
result = re.match('^hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$', content)
print(result)
print(result.group())
print(result.span())

#泛匹配
content= "hello 123 4567 World_This is a regex Demo"
result = re.match("^hello.*Demo$",content)
print(result)
print(result.group())
print(result.span())

#匹配目标
#re.group(1)获取的就是第一个括号中匹配的结果
content = "hello 1234567 World_This is a regex Demo"
result = re.match('^hello\s(\d+)\sWorld.*Demo$',content)
print(result)
print(result.group())
print(result.group(1))
print(result.span())

#贪婪匹配
#结果中可以看出只匹配到了7，并没有匹配到1234567，出现这种情况的原因是前面的.* 给匹配掉了， .*在这里会尽可能的匹配多的内容
content = "hello 1234567 World_This is a regex Demo"
result = re.match('^hello.*(\d+).*Demo', content)
print(result)
print(result.group(1))

#想要匹配到1234567则需要将正则表达式改为
result = re.match('^he.*?(\d+).*Demo', content)
print(result)

#匹配的内容是存在换行的问题的，这个时候的就需要用到匹配模式re.S来匹配换行的内容
content = """hello 123456 world_this
my name is zhaofan
"""
result =re.match('^he.*?(\d+).*?zhaofan$',content, re.S)
print(result)
print(result.group())
print(result.group(1))

#转义,用到转移符号\
content = "price is $5.00"
result = re.match('price is \$5\.00', content)
print(result)
print(result.group())

#re.search,不需要在写^以及$，因为search是扫描整个字符串
content = "extra things hello 123455 world_this is a Re Extra things"
result = re.search("hello.*?(\d+).*?Re", content)
print(result)
print(result.group())
print(result.group(1))