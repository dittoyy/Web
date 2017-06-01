#coding:utf-8
import requests
import re
import json
import time
ss=requests.session()

str_cookie='BAIDUID=9BB79332C64C55ADFF47BB66E2XXXXXXXXX:FG=1; PSTM=1490700622; BIDUPSID=E5593392C48A25ACD2751413DE5A5707; TIEBA_USERTYPE=ab202a741d89ac4664dafb03; bdshare_firstime=1491115637991; BDSFRCVID=A08sJeC62ZvIB7ciINso-O6ye2xAuYRTH6aouvwQVMCH1Qmt0l4GEG0PqM8g0KubLsfKogKK3gOTH4rP; H_BDCLCKID_SF=tJuO_I8afI83fP36q4r2DjvWqxby26nCtnbeaJ5nJDoAflTtjPbEyfCyhgc9tJc-tjbCLxT4QpP-HJ7G5RJG3xudyaQI2R0jannxKl0MLPjYbb0xynoDXbtEyUnMBMPe52OnaIb-LIcjqR8Zj6KajTbP; bottleBubble=1; pgv_pvi=3998808064; pgv_si=s197984256; BDRCVFR[S_ukKV6dOkf]=mk3SLVN4HKm; PSINO=6; H_PS_PSSID=1448_19035_21084; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; TIEBAUID=3b218806eb200790fd2ae7b1; BDUSS=F-LVMwU09YOVBpcEZwZjlYRVlEbVY0MjZNZ0dWU1dTaHdvM0k2UmZYQ3hSaEJaSVFBQUFBJCQAAAAAAAAAAAEAAAAw2CBnudvS9LTzyqrAsgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALG56FixuehYNH; STOKEN=5cb27861dad46603e26d289c5a8ec87c75e0acaf2a2ad105c34cf3c029c9f757; wise_device=0; LONGID=1730205744;'
reg='([\s\S]*?)=([\s\S]*?);'
dict_cookie={}
for c in  re.findall(reg,str_cookie):
   dict_cookie[c[0]]=c[1]
print 'dict_cookie:',dict_cookie           ###cookie字符串转字典，也可以直接把cookie字符串携带在requests的请求头中实现登录

user_agent_list = ['Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2372.400 QQBrowser/9.5.10548.400'
    ]
header={}
import random
dict_data={
'ie':'utf-8',
'kw':'中华城市',
'fid':'429477',
'tid':'5063074699',
'floor_num':'2',
'quote_id':'106047109156',
'rich_text':'1',
'tbs':'1d2e70d051724ba01491647010',
'content':'啦啦啦',
'lp_type':'0',
'lp_sub_type':'0',
'new_vcode':'1',
'tag':'11',
'repostid':'106047109156',
'anonymous':'0',

}   ####抓包得到的
dict_data['kw']='中华城市' 了 #重要，不能填错
dict_data['fid']='429477'        #fid是贴吧什么时候建的，可以抓包也可以用上面的获取fid的接口得到，fid指的是贴吧是第多少个建的贴吧，数字越小，说明贴吧建的越早
dict_data['tbs']='1d2e70d051724ba01491647010'   ##这个值是有生命周期的，用个天把时间没问题
dict_data['tid']='5065229106'    ##tid指的是主题帖子的id
dict_data['floor_num']='2'     ###这个不重要，随便多少都可以
dict_data['quote_id']='106092995926'      #用f12定位看以看到post_id字段，指的是层主帖子的id
dict_data['repostid']=dict_data['quote_id']
dict_data['content']='啦啦啦德玛西亚'   #content顾名思义是回复的内容了，除了这几个外其他的data参数都可以不修改。


#获取fid的接口 ，吧name换成贴吧名字，复制到浏览器地址栏回车就ok了http://tieba.baidu.com/f/commit/share/fnameShareApi?ie=utf-8&fname=%E6%B5%A0%E6%B0%B4%E4%BA%8C%E4%B8%AD

i=0

while(1):
    i=i+1
    try:
        header['User-Agent']=random.choice(user_agent_list)   ##习惯性的学爬虫来个随机换user-agent,但贴吧和知乎 这种都是基于账号追踪的，换ua和代理ip是没有任何作用的，逃避不了被识别为机器人
        header['Connection']='close'
        header.update({ 'Host':'tieba.baidu.com','Origin':'http://tieba.baidu.com','Referer':'http://tieba.baidu.com/p/5065229106'})

        dict_data['content']='哈哈哈哈'+str(i)

        res=ss.post('http://tieba.baidu.com/f/commit/post/add',cookies=dict_cookie,data=dict_data,headers=header)
        res_content=res.content
        res_text=res.text

        print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),'  ',json.dumps(json.loads(res_content),ensure_ascii=False) ###这样可以清楚的看到json里面的\u xxxx之类的对应的中文。

        if '"err_code":0' not in res.content:   ##errcode0表示回帖成功了

            i=i-1

        if '"err_code":220034' in res_content:
            time.sleep(300)     #说话太频繁，这时候不要太快回帖了，回了也没用，会连续返回errcode220034
        if '"need_vcode":0,' not in res_content:
            #print res_content
            print u'需要验证码'
            time.sleep(180)         ###如果回复太快了会弹出验证码，等一段时间不回帖就好啦。
    except Exception,e:
        #i=i-1
        print e
    time.sleep(10)                   ##每隔10秒回帖