# coding:utf-8
from bs4 import BeautifulSoup
import requests
headers={}
headers['User-Agent']="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
headers['Host']="tieba.baidu.com"
page_url="https://tieba.baidu.com/f?ie=utf-8&kw=%E7%BE%8E%E5%A5%B3"
request=requests.get(page_url,headers=headers,verify=False)
print request.status_code
content=request.content.decode('utf-8')
soup = BeautifulSoup(content, "html.parser")
print soup




