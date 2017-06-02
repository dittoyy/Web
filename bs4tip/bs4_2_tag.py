#coding:utf-8
from bs4 import BeautifulSoup

htm=open('ind2.html')

soup=BeautifulSoup(htm,'html.parser')
# print soup.prettify()

'''Tag :   标签对象，如：<p class="title"><b>yoyoketang</b></p>，这就是一个标签。   多个相同的标签名称，返回的是第一个

NavigableString ：也就是tag.string字符对象，如：这里是我的微信公众号：yoyoketang

BeautifulSoup   ：就是整个html对象

Comment    ：注释对象，如：!-- for HTML5 --，它其实就是一个特殊NavigableString'''

'''tag的name属性attrs属性'''