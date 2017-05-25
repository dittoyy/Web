#coding:utf-8

import requests,json
#JavaScript Object Notation
#数据交换格式,常用于http请求中
#
j1=json.dumps(['foo',{'bar':('i','love','you')}])
# print j1
#()变成[]看数吧
#'["foo", {"bar": ["baz", null, 1.0, 2]}]'
j2=json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True)
# print j2
# {"a": 0, "b": 0, "c": 0}
from StringIO import StringIO
io = StringIO()
json.dump(['streaming API'], io)
print io.getvalue()#'["streaming API"]'


'''python里面字典的payload后面
bool值是True和False,
json里面bool值是true和false,并且区分大小写'''
# 所以要data_json=json.dumps(payload)


'''以content字节输出，
返回的是一个字符串：{"success":true}
经过json解码后，解码是dumps，编码是loads
返回的就是一个字典：{u'success': True}
这样获取后面那个结果，
就用字典的方式去取值：result2["success"]'''

url = "http://www.kuaidi.com/index-ajaxselectcourierinfo-1202247993797-yunda.html"
headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
           }  # get方法其它加个ser-Agent就可以了


s = requests.session()
r = s.get(url, headers=headers,verify=False)
result=r.json()
data=result['data']
print data
print data[0]
get_result=data[0]['context']
print get_result


if u"已签收" in get_result:
    print "yeah"
else:
    print 'not'


