# coding:utf-8
from bs4 import BeautifulSoup
import requests
import os,random,json

user_agent_list = [ \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1" ,\
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", \
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 ke Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozillaa/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", \

    ]
def tieba_com(page_url):    ##列表页

    headers={}

    headers['User-Agent']=random.choice(user_agent_list)
    headers.update({
        "Host":"tbmsg.baidu.com",
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive'
        })
    print headers
    while(1):
        content=''
        try:
            content=requests.get(page_url,headers=headers,verify=False,timeout=10).content
            soup = BeautifulSoup(content, "html.parser")
            print soup
            #print text#500CUOWU
        except Exception as e:
            print e
        if content!='':
            break

    # 找出所有的标签
    index_page = soup.find_all('a',class_="j_th_tit")#找到所有其他的小页面的a列
    print len(index_page) # 返回list对象

    for page in index_page:
        index_url='https://tieba.baidu.com'+page['href']#次url
        # return 'index_url','--',page.string#输出所以的url和title
        print 'index_url','--',page.string
        '''这里还有max-page，，，pn=n'''


def get_detail(index_url):    ###详情页
    header={'User-Agent':random.choice(user_agent_list)}
    header.update({"Host":"tbmsg.baidu.com"})
    while(1):
        content=''
        try:
            content=requests.get(index_url,headers=header,verify=False,timeout=10).content
        except Exception as  e:
            print e
        if content!='':
            break
    # image=getlist0(re.findall('<img class="BDE_Image" src="(.*?)" size',content))
    images=soup.find_all(class_='BDE_Image')
    for tu in images:
        img_rl=tu['src']
        img_name=tu.string
        with open(os.getcwd()+"\\img1\\"+img_name+'.jpg', "wb") as f:
            f.write(requests.get(img_rl).content)
#get_detail('http://esf.sz.fang.com/chushou/3_193928457.htm')
def getlist0(list):
    if list:
        return list[0]
    else:
        return '空'

if __name__ == '__main__':
    page_url="https://tieba.baidu.com/f?ie=utf-8&kw=%E7%BE%8E%E5%A5%B3"#主pageurl
    tieba_com(page_url)





