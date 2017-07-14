# coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import re,os,requests
from bs4 import BeautifulSoup
from selenium import webdriver
def get_content(url):
    # url="http://tieba.baidu.com/f?ie=utf-8&kw=%E6%B9%96%E5%8D%97%E7%A7%91%E6%8A%80%E5%A4%A7%E5%AD%A6"
    driver=webdriver.PhantomJS()
    driver.implicitly_wait(10)
    driver.get(url)
    content = driver.page_source#主页面
    return content
    driver.close()
# print content
# url_list = re.findall('href=\"(.*?)\"', content, re.S)
# url_all = []
# for url in url_list:
#     url_all.append(url)
import time
now=time.strftime('%Y_%m_%d__%H_%M_%S')
def get_image(content):
    soup = BeautifulSoup(content,'html.parser')
    pics = soup.find_all("img", {"class": "BDE_Image"})
    print pics
    for i in range(0, len(pics)):
        img_url = pics[i]['src']
        img_name=pics[i].string
        print img_url
        with open(os.getcwd()+"/img2/"+str(i)+'.jpg', "wb") as f:
            f.write(requests.get(img_url).content)

if __name__ == '__main__':
    # s=get_content('https://tieba.baidu.com/p/4907146798')
    # get_image(s)
    for k in range(5):

        #s=get_content('https://tieba.baidu.com/p/4907146798')
        s=get_content('https://tieba.baidu.com/p/4907146798?pn={}'.format(str(k)))
        get_image(s)
    # [<img changedsize="true" class="BDE_Image" height="746" size="103531" src="http://imgsrc.baidu.com/forum/w%3D580/sign=4803564d0d082838680ddc1c8898a964/c555bc315c6034a831a345d3c11349540823768b.jpg" style="cursor: url(http://tb2.bdstatic.com/tb/static-pb/img/cur_zin.cur), pointer; " width="560"/>, <img changedsize="true" class="BDE_Image" height="746" size="80145" src="http://imgsrc.baidu.com/forum/w%3D580/sign=ee53cf6a22381f309e198da199004c67/e0415c6034a85edffdcd037143540923dc54758b.jpg" style="cursor: url(http://tb2.bdstatic.com/tb/static-pb/img/cur_zin.cur), pointer; " width="560"/>, <img changedsize="true" class="BDE_Image" height="420" size="82154" src="http://imgsrc.baidu.com/forum/w%3D580/sign=7674e05a1530e924cfa49c397c096e66/001034a85edf8db1ba6f81360323dd54574e748b.jpg" style="cursor: url(http://tb2.bdstatic.com/tb/static-pb/img/cur_zin.cur), pointer; " width="560"/>, <img changedsize="true" class="BDE_Image" height="746" size="78339" src="http://imgsrc.baidu.com/forum/w%3D580/sign=5a44d752e324b899de3c79305e071d59/68d85edf8db1cb133b28c141d754564e93584b8b.jpg" style="cursor: url(http://tb2.bdstatic.com/tb/static-pb/img/cur_zin.cur), pointer; " width="560"/>, <img changedsize="true" class="BDE_Image" height="420" size="65337" src="http://imgsrc.baidu.com/forum/w%3D580/sign=6c4c2146b299a9013b355b3e2d940a58/02af8db1cb1349547a5f15365c4e9258d0094a8b.jpg" style="cursor: url(http://tb2.bdstatic.com/tb/static-pb/img/cur_zin.cur), pointer; " width="560"/>, <img class="BDE_Image" src="http://bj.bcebos.com/fc-feed/0/pic/d166b61dcb543e3c0444d5fe1db3e10e.jpg"/>]
    # None
    # None
    # None
    # None
    # None
    # None
    # [Finished in 10.3s]