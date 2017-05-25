#coding:utf-8

import requests
#这里发帖等要保持那个session登陆
#
url='https://passport.cnblogs.com/user/signin'

'''cookie ={u'domain': u'.cnblogs.com',
u'name': u'.CNBlogsCookie',
u'value': u'19CE542385F9ACBF40DE4ECEAB9DF698901A08CAFE7A97419086AEB4BE70871A586F6947DB476A357D2B8D39FABFD0344D61F6B9BA4E5950465117C861E768D374166250DFBDBC057BF04347103D50D6745C564076BC0C982837710F8218DEA0BE667BA3',

u'expiry': 1491887887,
u'path': u'/',
u'httpOnly': True,
u'secure': False
}'''

'''
###fiddler只能看到value和name，其余的看不到，所以要多加下面这些
name：cookie的名称

value：cookie对应的值，动态生成的

domain：服务器域名

expiry：Cookie有效终止日期

path：Path属性定义了Web服务器上哪些路径下的页面可获取服务器设置的Cookie

httpOnly：防脚本攻击

secure:在Cookie中标记该变量，表明只有当浏览器和Web Server之间的通信协议为加密认证协议时，

浏览器才向服务器提交相应的Cookie。当前这种协议只有一种，即为HTTPS。
'''
########### 1先打开登录首页，获取部分cookie
url = "https://passport.cnblogs.com/user/signin"
headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
           }  # get方法其它加个ser-Agent就可以了

##################################方法1update
#往session里加cookie
s = requests.session()
r = s.get(url, headers=headers,verify=False)
print s.cookies#最开始的cookies

###########2添加登录需要的两个cookie
coo=requests.cookies.RequestsCookieJar()
# 多个就加多次，格式酱紫的coo.set('cookie-name','cookie-value',path='.xxx.com')
coo.set('.CNBlogsCookie','19CE542385F9ACBF40DE4ECEAB9DF698901A08CAFE7A97419086AEB4BE70871A586F6947DB476A357D2B8D39FABFD0344D61F6B9BA4E5950465117C861E768D374166250DFBDBC057BF04347103D50D6745C564076BC0C982837710F8218DEA0BE667BA3')
coo.set('.Cnblogs.AspNetCore.Cookies','CfDJ8Mmb5OBERd5FqtiQlKZZIG5WpxgEvb7OwEqUzxi9xSQMBheMp_NQdNERvTOZsa35yD9CxFJXNEuYZ2cDMfJ1rxjWqWfScsXKxCjTxkKgRie-qGbZTspFupO0xzd-kE_SQh9JDKJg3uLcNn1mTMUW3hrvX0Lh1YK8XBGTu0YVkodA61EYv89tlKPdXVsSJOmWw8-YL8upftWmXQHkX5vyGf0wtThzKG386baUGXPl3MopCE-NJLZvcNJpoz0SwWnMgcaSW-FCCoDlrdvym0eD6jsjJRV1hb48TXHEbZnh5vN0C-SdHwg9VCEvYNgkhfhKuQ')
s.cookies.update(coo)
print s.cookies

##################3登录成功后保存编辑内容
url2= "https://i.cnblogs.com/EditPosts.aspx?opt=1"
body = {"__VIEWSTATE": "",
        "__VIEWSTATEGENERATOR":"FE27D3433",
        "Editor$Edit$txbTitle":"34444wr-dfs",
        "Editor$Edit$EditorBody":"<p>helloertfnehfie这里dg/</p>",
        "Editor$Edit$Advanced$ckbPublished":"on",
        "Editor$Edit$Advanced$chkDisplayHomePage":"on",
        "Editor$Edit$Advanced$chkComments":"on",
        "Editor$Edit$Advanced$chkMainSyndication":"on",
        "Editor$Edit$lkbDraft":"存为草稿",
         }
r2 = s.post(url2, data=body, verify=False)
print r2.content
