#coding=utf-8
import  json,requests

r=requests.get('http://wthrcdn.etouch.cn/weather_mini?city=北京')
# print (r.text,u'数据类型:',type(r.text))
print json.dumps(json.loads(r.content),ensure_ascii=False)
#对数据进行反序列化的操作
dic=json.loads(r.text)
# print (dic,u'数据类型:',type(dic))