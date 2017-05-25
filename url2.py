#coding:utf-8
# from urllib import request
import urllib

# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', data.decode('utf-8'))

import urllib2

# response = urllib2.urlopen("http://www.baidu.com")
# # urlopen(url,data,timeout)
# # print response.read()

# request = urllib2.Request("http://www.baidu.com")
# response = urllib2.urlopen(request)
# print response.read()
from urllib import *
from urllib2 import Request, urlopen, URLError, HTTPError

print('Login to weibo.cn...')
email = input('Email:')
passwd = input('Password:')
login_data = urllib.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = urllib2.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

f=urllib2.urlopen(req, data=login_data.encode('utf-8'))
try:
    f
except HTTPError as e:
    print 'The server couldn\'t fulfill the request.'
    print 'Error code: ', e.code
except URLError as e:
    print 'We failed to reach a server.'
    print 'Reason: ', e.reason
else:
    pass
    # everything is fine

# print('Status:', f.code, f.reason)
# for k, v in f.getheaders():
#     print('%s: %s' % (k, v))
print('Data:', f.read().decode('utf-8'))

# Status: 200 OK
# Server: nginx/1.2.0
# ...
# Set-Cookie: SSOLoginState=1432620126; path=/; domain=weibo.cn
# ...
# Data: {"retcode":20000000,"msg":"","data":{...,"uid":"1658384301"}}

# Data: {"retcode":50011015,"msg":"\u7528\u6237\u540d\u6216\u5bc6\u7801\u9519\u8bef","data":{"username":"example@python.org","errline":536}}




#proxy代理handler
# proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
# proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
# proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
# opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
# f=opener.open('http://www.example.com/login.html')

'''
#post方式
values = {"username":"1016903103@qq.com","password":"XXXX"}
# values={}
# values['username']='1992@qq.com'
# values['password']='ddod'
data = urllib.urlencode(values) #将字典编码
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print response.read()

#get方式
values={}
values['username'] = "1016903103@qq.com"
values['password']="XXXX"
data = urllib.urlencode(values)
url = "http://passport.csdn.net/account/login"
geturl = url + "?"+data#就是这里最重要？+data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()
'''
