from pyquery import PyQuery as pq

#.parents就可以找到祖先节点的内容
html = '''<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>'''
doc = pq(html)
items = doc('.list')
parents = items.parents()
print(type(parents))
print(parents)

#兄弟元素
li = doc('.list .item-0.active')
print(li.siblings())

#遍历单个元素
doc = pq(html)
li = doc('.item-0.active')
print(li)
lis = doc('li').items()
print(type(lis))
for li in lis:
    print(type(li))
    print(li)

#获取属性
a = doc('.item-0.active a')
print(a)
print(a.attr('href'))
print(a.attr.href)

#获取文本
a = doc('.item-0.active a')
print(a.text())

#获取html
li = doc('.item-0.active')
print(li)
print(li.html())