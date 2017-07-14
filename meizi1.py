#coding:utf-8
import requests
from bs4 import BeautifulSoup
import os,sys
reload(sys)
sys.setdefaultencoding('utf-8')
def mei():
    r = requests.get(url)
    html = r.content.decode('utf-8')
    Html = BeautifulSoup(html,'html.parser')
    list = Html.find_all(class_='j_th_tit ')
    x=0
    for i in list:
        a = i['href']
        b = ['https://tieba.baidu.com'+a]
        print('\n')
        print('帖子标题链接:       %s'%b)
        print('\n')
        for c in b:
            r = requests.get(c)
            htm = r.content.decode('utf-8')
            Htm = BeautifulSoup(htm, 'html.parser')
            d= Htm.find_all(class_='BDE_Image')
            for aa in d:
                d = aa['src']
                print('妹子图片链接：%s'%d)
                with open(os.getcwd() + "/jpg/" + '%dff.jpg' % x, "wb") as f:
                    f.write(requests.get(d).content)
                # urllib.urlretrieve(aa,'%s.jpg' % x)#这是urllib的做法
                x+=1
if __name__ == '__main__':
    for i in range(0,200,50):
        url = 'https://tieba.baidu.com/f?kw=美女&ie=utf-8&pn=%s'%i
        mei()
