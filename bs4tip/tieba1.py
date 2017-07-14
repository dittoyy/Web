#coding:utf-8
import requests
import re
from bs4 import BeautifulSoup
import os


def get_image(url, page):
    html = requests.get(url, headers=header).content.decode('UTF-8')
    soup = BeautifulSoup(html)
    pics = soup.find_all("img", {"class": "BDE_Image", "pic_type": "0"})
    for i in range(0, len(pics)):
        img_url = pics[i]['src']
        img = requests.get(img_url).content
        save_path = 'C:/Users/Administrator/Desktop/Web-master/bs4tip/img2/%s/' % page
        if os.path.exists(save_path):
            pass
        else:
            os.mkdir(save_path)
        with open(save_path + '%s.jpg' % str(i), 'wb') as f:
            f.write(img)
            print img_url + ' saved'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive'
}
tieba_url = 'http://tieba.baidu.com/p/2491624899'
response = requests.get(tieba_url, headers=header,verify=False).content.decode('UTF-8')
pattern = re.compile(r'共<span class="red">([0-9]*)</span>页')
# print pattern
max_page = pattern.findall(response)
print max_page
# max_page=max_page[0]
# if max_page == '1':
#     page_url = tieba_url
#     get_image(page_url,1)
# else:
#     for i in range(1, int(max_page)):
#         page_url = tieba_url + '?pn=' + str(i)
#         get_image(page_url, str(i))
