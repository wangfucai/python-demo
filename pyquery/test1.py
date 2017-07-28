from pyquery import PyQuery as pq

html = '''<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul></div>'''

#初始化的时候一般有三种传入方式：传入字符串，传入url,传入文件
doc = pq(html)
print(doc)
print(type(doc))
print(doc('li'))

#文件初始化，例如：pq(filename='index.html')

#基本的CSS选择器
print(doc('#container .list li'))

#查找元素子元素
items = doc('.list')
print(type(items))
print(items)
lis = items.find('li')
print(type(lis))
print(lis)

#通过children可以实现同样的效果,并且通过.children方法得到的结果也是一个pyquery对象
li = items.children()
print(type(li))
print(li)

#在children里也可以用CSS选择器
li2 = items.children('.active')
print(li2)

#父元素
items = doc('.list')
container = items.parent()
print(type(container))
print(container)

