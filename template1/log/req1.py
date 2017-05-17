# -*- coding:utf-8 -*-
__author__ = u'harry'


import requests   #先导入包,这是必须的

url = 'http://XXXXXXXXXXXXXXX'       #url:接口地址
data = {'XXXX':'XXX'}                        #data:接口传递的参数
headers = {'Connection':'close'}                        #header:传递header信息
                                                            #files:接口中需要上传文件则需要用到该参数
r = requests.post(url,data = data,headers = headers)        #请求url，获得返回的数据信息
print(r.text.encode('utf-8'))　　　　　　　　　　　　　　　　　　#获得的返回数据使用text方法进行获取




# -*- coding:utf-8 -*-
__author__ = u'harry'
import urllib.request
import requests   #先导入包,这是必须的
import urllib.parse

url = 'XXXXXXX'  # url:接口地址
data = {'XXX': 'XXX'}                     #data:接口传递的参数
headers = {'Connection': 'close'}  # header:传递header信息
# files:接口中需要上传文件则需要用到该参数

def requests_test(url,data,headers):
    response = requests.post(url,data = data,headers = headers)        #请求url，获得返回的数据信息
    print(response.text,response.headers)                                     #返回头部信息

def urllib_test(url,data):
    data1 = urllib.parse.urlencode(data).encode('utf-8')
    response = urllib.request.Request(url=url,data = data1)
    html = urllib.request.urlopen(response)
    print(html.read())
    print(html.getcode(),html.msg)        #获得html返回的状态
    print(html.headers)                   #返回头部信息


#下面调用两个方法：
urllib_test(url,data)
requests_test(url,data,headers)


# requests： requests.get("url")
# urllib:不传入data就可以了。
# 如果要解决接口返回值的unicode编码，则
html.read().decode('unicode-escape')