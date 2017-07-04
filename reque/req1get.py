#coding:utf-8
import requests
par={'Keywords':'dittoyy3991'}
#多个参数格式：{"key1": "value1", "key2": "value2", "key3": "value3"}
r=requests.get('http://zzk.cnblogs.com/s/blogpost',params=par)
print r.status_code
# print r.content#text
#gzip压缩,text可能会乱码，比如百度
#fiddler工具乱码，是可以点击后解码的
#在代码里面可以用r.content这个方法，content会自动解码 gzip 和deflate压缩
'''
import html5lib
from bs4 import BeautifulSoup
print BeautifulSoup(r.text,'html.parser')
# 为何不对'''
print r.url
# print r.json()#内置的json解码器,需要传两个参
print r.encoding#返回编码格式
print r.headers#若不存在返回None
print r.cookies#获取cookies
#<RequestsCookieJar[]>
# print r.raise_for_status()#失败请求(非200)抛出异常,3个参数，不填None


