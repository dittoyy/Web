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

soup=BeautifulSoup(html)#���� beautifulsoup ����
# soup1=BeautifulSoup(open('index.html'))#�������ñ��� HTML �ļ�����������

'''print soup.prettify()#��ʽ����ӡ������������,�����Ѿ���unicode��'''
#����html������4��
#tag,navigablestring.BeautifulSoup,COMMENT

'''1  tag���Ǳ�ǩ�����ҵ��������������еĵ�һ������Ҫ��ı�ǩ'''
print soup.title
print soup.head#.title
print soup.a#��Ȼֻ��һ��.string#��ӡ������text

print type(soup.a)#<class 'bs4.element.Tag'>
###tag����Ҫ������������attrs �ͱ�ǩ����name
#name��ǩ����
print soup.name#����������[document]
print soup.head.name#����������䱾��tag head

#attrs�õ�����ֵ�������ֵ�
print soup.p.attrs#��ȡ���������ֵ�{'class': ['title'], 'name': 'dromouse'}
print soup.p['class']#�õ�����ֵ[title]
soup.p['class']='diod'#�ı�����ֵ
print soup.p['class']
del soup.p['class']#ɾ������
print soup.p.attrs
soup.p['class']='diod'#��������ֵ
print soup.p.attrs

'''2   navigablestring     .string��ȡ��ǩ�ڲ�������'''
print soup.p.string
print type(soup.p.string)#<class 'bs4.element.NavigableString'>


'''3  BeautifulSoup �����ʾ����һ���ĵ���ȫ������,�󲿷�ʱ����tag����
���ͣ����ƣ��Լ�����'''
print type(soup.name)
#<type 'unicode'>
print soup.name
# [document]
print soup.attrs
#{} ���ֵ�

'''4   comment �������navigablestring����ʵ������ɲ�����ע�ͷ�'''
print soup.a.string
print type(soup.a.string)#<class 'bs4.element.Comment'>


# ��Ϊ�޷��ֱ������������ж���comment��,�ǲ����
if type(soup.a.string)==bs4.element.Comment:
    print soup.a.string


#�����ı���1.contents 2.children���صĲ���list���Ǹ�list������
#

print soup.head.contents[0]#��tag���ӽڵ���list���,Ȼ������ڼ���
# [<title>The Dormouse's story</title>]
# print soup.body.contents

#
print soup.head.children#<listiterator object at 0x0292DE90>
# ������ѭ��ȡֵ����
# # html���еĽڵ㶼����ӡ������
# for child in soup.descendants:
#     print child

#     # # h�Ľڵ㶼����ӡ������
# for child in soup.body.children:
#     print child

'''���һ����ǩ����û�б�ǩ�ˣ�
��ô .string �ͻ᷵�ر�ǩ��������ݡ�
�����ǩ����ֻ��Ψһ��һ����ǩ�ˣ�
��ô .string Ҳ�᷵�������������,
�����������ӽڵ���޷�ȷ���ˣ�����None
'''
print soup.head.string
#The Dormouse's story
print soup.title.string
#The Dormouse's story

print soup.html.string
# None

'''�������'''
# �������.strings
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

# �������.stripped_stringsȥ������հ�����
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

# ���ڵ�parent
p=soup.p
print p.parent.name#body

content=soup.head.title.string
print content#The Dormouse's story
print content.parent.name#title����Ϊ��ȷ����string���������İְ���title

#���������кܶ��������Ҫfor
#parents ���Կ��Եݹ�õ�Ԫ�ص����и����ڵ�
content=soup.head.title.string
print content.parents#<generator object parents at 0x028A9288>
for i in content.parents:
    print i.name

# �ֵܽڵ� .next_sibling .previous_sibling
# ��������ͨ�����ַ�����հף���Ϊ�հ׻��߻���Ҳ���Ա�����һ���ڵ㣬
# ���Եõ��Ľ�������ǿհ׻��߻��У��ڵ㲻���ڼ�����None
# print soup.p.next_siblings#<generator object next_siblings at 0x02885288>
print soup.p.next_sibling
print soup.p.previous_sibling

# ȫ���ֵܽڵ� .next_siblings .previous_siblings
for sibling in soup.p.next_siblings:
    print repr(sibling)

#ǰ��ڵ� .next_element .previous_element
#�� .next_sibling  .previous_sibling ��ͬ��
#��������������ֵܽڵ㣬���������нڵ㣬���ֲ��

print soup.head.next_element
print soup.head.next_sibling
#ȫ��ǰ��ڵ� .next_elements .previous_elements
# .next_elements �� .previous_elements �ĵ�����
# �Ϳ�����ǰ���������ĵ��Ľ�������,
# �ͺ����ĵ����ڱ�����һ��
for element in soup.head.next_elements:
    print repr(element)

'''# �����ĵ���
# find_all( name��tag , attrs , recursive , text , **kwargs )'''
# 1tag�������ַ�������ƥ�������,������������ڲ����ĵ������е�<a>��ǩ
print soup.find_all('a')
#2��������ʽ
#�������������ʽ��Ϊ����,
#Beautiful Soup��ͨ��������ʽ�� match() ��ƥ������
import re
for tag in soup.find_all(re.compile('^b')):
    print tag.name
#3���б�
print soup.find_all(['a','b'])
# 4��True
for tag in soup.find_all(True):
    print tag.name
# 5������
def hasclassnoid(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
print soup.find_all(hasclassnoid)

# keyword����������id��Ҳ�������ԣ�class�����Ե��ǿ���class_
print soup.find_all(id='link2')
print soup.find_all(href=re.compile('elsie'))#href�������Ǽ����־Ϳ�����
print soup.find_all(id='link1',href=re.compile('elsie'))#���Զ������

# find_all() ������ attrs ��������һ���ֵ���������������������Ե�tag
data_soup = BeautifulSoup('<div data-foo="value">foo!</div>')
# data_soup.find_all(data-foo="value")
# SyntaxError: keyword can't be an expression
# data_soup.find_all(attrs={"data-foo": "value"})#���ص���һ��list
# [<div data-foo="value">foo!</div>]


# text���������ĵ��е��ַ������ݣ���name����һ�������ַ��������б�true
print soup.find_all(text=['Elsie','Lacie'])#���Բ��Ҷ��list
print soup.find_all(text=re.compile("Dormouse"))
#limit����
print soup.find_all('a',limit=2)

#tag�� find_all() ����ʱ,
#Beautiful Soup�������ǰtag����������ڵ�,
#���ֻ������tag��ֱ���ӽڵ�,����ʹ�ò���
#recursive=False .
print soup.find_all('title',recursive=False)

# ֱ�ӷ��ؽ��������list
# find find_all
# find_parents() find_parent
# find_next_siblings()  find_next_sibling()
# find_previous_siblings()  find_previous_sibling()
# find_all_next()  find_next()
# find_all_previous() �� find_previous()

###############cssѡ��������list
# select �������صĽ�������б���ʽ��
# ���Ա�����ʽ�����
# Ȼ���� get_text() ��������ȡ�������ݡ�
soup.select('a')
#tag��class��id,�����Լ���ϲ����ӱ�ǩ���Ҿ���
#һ��tag���class����
# soup.select('tagname.class1.class2')[0]
# soup.find('tagname', class_=['class1', 'class2'])

soup = BeautifulSoup(html, 'lxml')
print type(soup.select('title'))
print soup.select('title')[0].get_text()

for title in soup.select('title'):
    print title.get_text()

from bs4.diagnose import diagnose
data = open(bad.html).read()diagnose(data)