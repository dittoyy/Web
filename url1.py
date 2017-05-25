#coding:utf-8
#爬虫思路，静态，1获取源码read(),readline()，2获取图片3下载4多页requests get/post content
#爬虫最重要的是正则re,bs4直接根据标签找到内容,soup.prettify()比正则好用
#requests 基础-实践案例基础知识+思路-项目案例吃透项目方法
# import re
# re,findall('y','htttpsjkh')#出来的是list
# 中文在可迭代对象就是unicode对象
# import urllib
# a=urllib.urlopen('')

#5种数据类型
# number,string,list,tuple,dict

# import requests
# q=requests.get('http://www.baidu.com')
# #获取源码，content 编码啥的好用些
# q.text
# q.content
# print q.status_c


#pengfu网图片和标题



# from bs4 import BeautifulSoup
# html='<div>hello world <i>ghhhhhhhhhh</i>你好哇！</div>'
# soup=BeautifulSoup(html,'html.parser')#解析网页
# print soup.div

# from bs4 import BeautifulSoup
# html=''
# soup=BeautifulSoup(open('a.html'))
# print soup.prettify()


import re
import httplib
httplib.HTTPConnection.debuglevel = 1
# re,findall('y','htttpsjkh')#出来的是list
#中文在可迭代对象就是unicode对象
#字符串格式化
cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
urllib2.install_opener(opener)
opener.handle_open["http"][0].set_http_debuglevel(1)
import urllib,sys

def page(pg):
    url='http://www.pengfu.com/index_%s.html'%pg
    html=urllib.urlopen(url).read()
    # print html
    return html

# page(1)

def title(html):

    reg=re.compile(r'<h1 class="db-p"><a href=".*?" target="_blank">(.*?)</a>')
    item=re.findall(reg,html)
    print item[0]#切片
    for t in item:
        print t
    return item
html=page(1)
b=title(html)

def content(html):
    html=page(1)
    reg=r'<img src="(.*?)" width='
    item=re.findall(reg,html)
    print item
    return item

def download(url,name):
    path='img\%s.jpg'%name.decode('utf-8').encode('gbk')
    urllib.urlretrieve(url,path)#下载并保存到路径

# for i in range(1,6):
#     html=page(1)
#     title_list=title(html)
#     content_list=content(html)
#     for i,z in zip(title_list,content_list):
#         download(z,i)#自定义下载方法
#         print i,z

