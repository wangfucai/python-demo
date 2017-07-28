from bs4 import BeautifulSoup

#推荐使用lxml解析库，必要时使用html.parser
#标签选择筛选功能弱但是速度快
#建议使用find()、find_all() 查询匹配单个结果或者多个结果
#如果对CSS选择器熟悉建议使用select()
#记住常用的获取属性和文本值的方法
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all('ul'))
print(type(soup.find_all('ul')[0]))

for ul in soup.find_all('ul'):
    print(ul.find_all('li'))

print(soup.find_all(attrs={'id': 'list-1'}))
print(soup.find_all(attrs={'name': 'elements'}))

print(soup.find_all(text='Foo'))

print(soup.select('.panel .panel-heading'))
print(soup.select('ul li'))
print(soup.select('#list-2 .element'))
print(type(soup.select('ul')[0]))

#获取内容通过get_text()就可以获取文本内容
for li in soup.select('li'):
    print(li.get_text())

for ul in soup.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])