#coding:utf-8

from bs4 import BeautifulSoup
import bs4
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<b>dido</b>
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup=BeautifulSoup(html)#创建 beautifulsoup 对象
# soup1=BeautifulSoup(open('index.html'))#还可以用本地 HTML 文件来创建对象

'''print soup.prettify()#格式化打印出了它的内容,不过已经是unicode了'''
#所有html对象都是4种
#tag,navigablestring.BeautifulSoup,COMMENT

'''1  tag就是标签，查找的是在所有内容中的第一个符合要求的标签'''
print soup.title
print soup.head#.title
print soup.a#居然只有一个.string#打印出它的text

print type(soup.a)#<class 'bs4.element.Tag'>
###tag最重要的两个属性是attrs 和标签名字name
#name标签名字
print soup.name#自身特殊是[document]
print soup.head.name#其余是输出其本身tag head

#attrs得到属性值和属性字典
print soup.p.attrs#获取所有属性字典{'class': ['title'], 'name': 'dromouse'}
print soup.p['class']#得到属性值[title]
soup.p['class']='diod'#改变属性值
print soup.p['class']
del soup.p['class']#删除属性
print soup.p.attrs
soup.p['class']='diod'#增加属性值
print soup.p.attrs

'''2   navigablestring     .string获取标签内部的文字'''
print soup.p.string
print type(soup.p.string)#<class 'bs4.element.NavigableString'>


'''3  BeautifulSoup 对象表示的是一个文档的全部内容,大部分时候当作tag对象
类型，名称，以及属性'''
print type(soup.name)
#<type 'unicode'>
print soup.name
# [document]
print soup.attrs
#{} 空字典

'''4   comment 是特殊的navigablestring，其实输出依旧不包含注释符'''
print soup.a.string
print type(soup.a.string)#<class 'bs4.element.Comment'>


# 因为无法分辨所以先做个判断是comment不,是才输出
if type(soup.a.string)==bs4.element.Comment:
    print soup.a.string


#遍历文本树1.contents 2.children返回的不是list，是个list生成器
#

print soup.head.contents[0]#将tag的子节点以list输出,然后输出第几个
# [<title>The Dormouse's story</title>]
# print soup.body.contents

#
print soup.head.children#<listiterator object at 0x0292DE90>
# 生成器循环取值即可
# # html所有的节点都被打印出来了
# for child in soup.descendants:
#     print child

#     # # h的节点都被打印出来了
# for child in soup.body.children:
#     print child

'''如果一个标签里面没有标签了，
那么 .string 就会返回标签里面的内容。
如果标签里面只有唯一的一个标签了，
那么 .string 也会返回最里面的内容,
如果包含多个子节点就无法确定了，返回None
'''
print soup.head.string
#The Dormouse's story
print soup.title.string
#The Dormouse's story

print soup.html.string
# None

'''多个内容'''
# 多个内容.strings
for string in soup.strings:
    print repr(string)
# u"The Dormouse's story"
# u'\n'
# u"The Dormouse's story"
# u'\n'
# u'Once upon a time there were three little sisters; and their names were\n'
# u',\n'
# u'Lacie'
# u' and\n'
# u'Tillie'
# u';\nand they lived at the bottom of a well.'
# u'\n'
# u'...'

# 多个内容.stripped_strings去除多余空白内容
for string in soup.stripped_strings:
    print(repr(string))
# u"The Dormouse's story"
# u"The Dormouse's story"
# u'Once upon a time there were three little sisters; and their names were'
# u'Elsie'
# u','
# u'Lacie'
# u'and'
# u'Tillie'
# u';\nand they lived at the bottom of a well.'
# u'...'

# 父节点parent
p=soup.p
print p.parent.name#body

content=soup.head.title.string
print content#The Dormouse's story
print content.parent.name#title，因为精确到了string，所以他的爸爸是title

#它的祖上有很多个，所以要for
#parents 属性可以递归得到元素的所有父辈节点
content=soup.head.title.string
print content.parents#<generator object parents at 0x028A9288>
for i in content.parents:
    print i.name

# 兄弟节点 .next_sibling .previous_sibling
# 这两属性通常是字符串或空白，因为空白或者换行也可以被视作一个节点，
# 所以得到的结果可能是空白或者换行，节点不存在即返回None
# print soup.p.next_siblings#<generator object next_siblings at 0x02885288>
print soup.p.next_sibling
print soup.p.previous_sibling

# 全部兄弟节点 .next_siblings .previous_siblings
for sibling in soup.p.next_siblings:
    print repr(sibling)

#前后节点 .next_element .previous_element
#与 .next_sibling  .previous_sibling 不同，
#它并不是针对于兄弟节点，而是在所有节点，不分层次

print soup.head.next_element
print soup.head.next_sibling
#全部前后节点 .next_elements .previous_elements
# .next_elements 和 .previous_elements 的迭代器
# 就可以向前或向后访问文档的解析内容,
# 就好像文档正在被解析一样
for element in soup.head.next_elements:
    print repr(element)

'''# 搜索文档树
# find_all( name是tag , attrs , recursive , text , **kwargs )'''
# 1tag查找与字符串完整匹配的内容,下面的例子用于查找文档中所有的<a>标签
print soup.find_all('a')
#2传正则表达式
#如果传入正则表达式作为参数,
#Beautiful Soup会通过正则表达式的 match() 来匹配内容
import re
for tag in soup.find_all(re.compile('^b')):
    print tag.name
#3传列表
print soup.find_all(['a','b'])
# 4传True
for tag in soup.find_all(True):
    print tag.name
# 5传方法
def hasclassnoid(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
print soup.find_all(hasclassnoid)

# keyword参数，可以id，也可以属性，class不可以但是可以class_
print soup.find_all(id='link2')
print soup.find_all(href=re.compile('elsie'))#href包含了那几个字就可以了
print soup.find_all(id='link1',href=re.compile('elsie'))#可以多个属性

# find_all() 方法的 attrs 参数定义一个字典参数来搜索包含特殊属性的tag
data_soup = BeautifulSoup('<div data-foo="value">foo!</div>')
# data_soup.find_all(data-foo="value")
# SyntaxError: keyword can't be an expression
# data_soup.find_all(attrs={"data-foo": "value"})#返回的是一个list
# [<div data-foo="value">foo!</div>]


# text参数搜索文档中的字符串内容，与name参数一样接受字符串正则列表true
print soup.find_all(text=['Elsie','Lacie'])#可以查找多个list
print soup.find_all(text=re.compile("Dormouse"))
#limit参数
print soup.find_all('a',limit=2)

#tag的 find_all() 方法时,
#Beautiful Soup会检索当前tag的所有子孙节点,
#如果只想搜索tag的直接子节点,可以使用参数
#recursive=False .
print soup.find_all('title',recursive=False)

# 直接返回结果，不是list
# find find_all
# find_parents() find_parent
# find_next_siblings()  find_next_sibling()
# find_previous_siblings()  find_previous_sibling()
# find_all_next()  find_next()
# find_all_previous() 和 find_previous()

###############css选择器返回list
# select 方法返回的结果都是列表形式，
# 可以遍历形式输出，
# 然后用 get_text() 方法来获取它的内容。
soup.select('a')
#tag，class，id,属性以及组合查找子标签查找均可
#一个tag多个class属性
# soup.select('tagname.class1.class2')[0]
# soup.find('tagname', class_=['class1', 'class2'])

soup = BeautifulSoup(html, 'lxml')
print type(soup.select('title'))
print soup.select('title')[0].get_text()

for title in soup.select('title'):
    print title.get_text()

from bs4.diagnose import diagnose
data = open(bad.html).read()diagnose(data)