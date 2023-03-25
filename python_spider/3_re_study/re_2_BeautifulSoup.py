
from bs4 import BeautifulSoup


html_doc = """

<html><head><title>pythontest</title></head>
<body>
<p class="title"><b>yuysyl</b></p>

<p class="story">yuysyl
<a href="http://example.com/1" class="sister" id="link1">yuysyltest1</a>,
<a href="http://example.com/2" class="sister" id="link2">yuysyltest2</a> ,
test or test2?</p>

<p class="story">...</p>
</body>
</html>

"""

'''
大概可以理解为向操作 dom树一样操作元素。比起正则表达式简洁一些,当然也有缺点 对于复杂架构可能不太友好
中文文档参考：
https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/

'''


soup = BeautifulSoup(html_doc,'lxml')
print(soup.title.string)
print(soup.p.string)#仅一个
print(soup.title.parent.name)  #父标签name
print(soup.a)#仅一个
print(soup.a.attrs)#a标签属性
print(soup.find_all('a'))
print(soup.find(id="link2"))
print(soup.get_text())

print(soup.select("title"))
print(soup.select("body a"))
print(soup.select("p > #link1"))
