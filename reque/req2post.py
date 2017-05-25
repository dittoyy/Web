#coding:utf-8
import requests
# par={'Keywords':'yoyoketang'}
#多个参数格式：{"key1": "value1", "key2": "value2", "key3": "value3"}

'''
# payload={
#     'yoyo':'helloworld',
#     'python':'9999'
# }
# r=requests.post('http://httpbin.org/post',data=payload)
#requests post的要求是str不可以是json
####################1.form表格的字典类型传入################
'''



import json
payload={
    'yoyo':'helloworld',
    'python':'9999'
}
data_json=json.dumps(payload)
##########################2.json的传入##############


r=requests.post('http://httpbin.org/post',data=data_json)
print r.status_code
print r.text
print r.url
print r.json()
'''# print r.json()#内置的json解码器,需要传两个参，不传返回下面的
########################1.form
#{u'files': {},
#u'origin': u'14.153.17.97',
#u'form': {u'python': u'9999', u'yoyo': u'helloworld'},
#u'url': u'http://httpbin.org/post',
#u'args': {},
#u'headers': {u'Content-Length': u'27', u'Accept-Encoding': u'gzip, deflate', u'Host': u'httpbin.org', u'Accept': u'*/*', u'User-Agent': u'python-requests/2.11.1', u'Connection': u'close',
# u'Content-Type': u'application/x-www-form-urlencoded'},
#u'json': None,
# u'data': u''}
#########################2.json
#{u'files': {},
#u'origin': u'14.153.17.97',
#u'form': {},
#u'url': u'http://httpbin.org/post',
#u'args': {},
#u'headers': {u'Content-Length': u'40', u'Accept-Encoding': u'gzip, deflate', u'Host': u'httpbin.org', u'Accept': u'*/*', u'User-Agent': u'python-requests/2.11.1', u'Connection': u'close'},
#u'json': {u'python': u'9999', u'yoyo': u'helloworld'},
#u'data': u'{"python": "9999", "yoyo": "helloworld"}'}

#对比下就知道且content-type也不一样，form传form其他不传，json传json里，data里----Content-Type': 'application/json'
'''
print r.encoding#返回编码格式，居然有返回None
print r.headers#若不存在返回None
print r.cookies
#

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json; charset=utf-8",
            "X-Requested-With": "XMLHttpRequest",
            "Cookie": "xxx.............",    # 此处cookie省略了
            "Connection": "keep-alive"
            }

payload={
    'input1':'GQkdwv67Go1T8kNLmO1WAos9I5QFC8WEOSU7QuptbKKBHDMfC6A7GLfCIgAie0G4Ky9SzMxuCymcgx/HS48RBo8bIKRI49A1U1RbfN8rh7YrIoN7CKmMVnRPyKJAF1JitfMe5hvBxOLSfUdSkESfD1R2FpnMR2ZHUWddeWge+FY=',
    'input2':'QOKdVowqhaSWcHKqZKoq/GetLYM8+QGA6dsrR573H0+JX/f+mPpSSQQGev8cmra3QCvakGAWw53u2/XCLXS99lfYDSxvSzkM0vFHW08vNCTroqv02eMuUDrMIvX+byItrlxmzW2Fi1hCQO+u0NNXYS/cw6UnIkSRukzFeGoUBfI=',
    'remember':True
    }
r.requests.post(url,json=payload,headers=headers,verify=False)
print r.json