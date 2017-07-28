from bs4 import BeautifulSoup

html = '''<html><head><title>The Dormouse's story</title></head><body>
<p class="title"><b>The Dormouse's story</b></p><p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;and they lived at the bottom of a well.</p>
<p class="story">...</p>'''

#Beautiful Soup支持Python标准库中的HTML解析器,还支持一些第三方的解析器，如果我们不安装它，
# 则 Python 会使用 Python默认的解析器，lxml 解析器更加强大，速度更快，推荐安装。
soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p)
print(soup.p["class"])
print(soup.a)
print(soup.find_all('a'))
print(soup.find(id='link3'))

#获取所有的链接，以及文字内容：
for link in soup.find_all('a'):
   print(link.get('href'))
print(soup.get_text())

html = """<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
            and            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.        </p>
        <p class="story">...</p>"""

soup = BeautifulSoup(html, 'lxml')
print(soup.p.contents)

#soup.p.children是一个迭代对象，而不是列表，只能通过循环的方式获取素有的信息
print(soup.p.children)
for i,child in enumerate(soup.p.children):
    print(i,child)

#通过contents以及children都是获取子节点，如果想要获取子孙节点可以通过descendants
#print(soup.descendants)同时这种获取的结果也是一个迭代器