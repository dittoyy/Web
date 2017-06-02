# coding:utf-8
from bs4 import BeautifulSoup
import requests
import os
r = requests.get("http://699pic.com/sousuo-218808-13-1.html")
fengjing = r.content
soup = BeautifulSoup(fengjing, "html.parser")
# 找出所有的标签
images = soup.find_all(class_="lazy")
print images # 返回list对象

# for i in images:
#     jpg_rl = i["data-original"]
#     title = i["title"]
#     print title
#     print jpg_rl
#     print ""
#     #requests里get打开图片的url地址，
#     #content方法返回的是二进制流文件，可以直接写到本地
#     with open(os.getcwd()+"\\img\\"+title+'.jpg', "wb") as f:
#         f.write(requests.get(jpg_rl).content)