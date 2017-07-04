#coding:utf-8

import requests
#这里发帖等要保持那个session登陆
#
url='https://passport.cnblogs.com/user/signin'
# 添加请求头headers,可以用fiddler抓包
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json; charset=utf-8",
            # "VerificationToken": "xxx...",  # 已省略
            "X-Requested-With": "XMLHttpRequest",
            #　"Referer": "https://passport.cnblogs.com/user/signin?ReturnUrl=http%3a%2f%2fmsg.cnblogs.com%2fsend%2f%e4%b8%8a%e6%b5%b7-%e6%82%a0%e6%82%a0",
            "Content-Length": "385",
            "Cookie": "xxx.....",   # 已省略
            "Connection": "keep-alive"
            }

payload={
    'input1':'GQkdwv67Go1T8kNLmO1WAos9I5QFC8WEOSU7QuptbKKBHDMfC6A7GLfCIgAie0G4Ky9SzMxuCymcgx/HS48RBo8bIKRI49A1U1RbfN8rh7YrIoN7CKmMVnRPyKJAF1JitfMe5hvBxOLSfUdSkESfD1R2FpnMR2ZHUWddeWge+FY=',
    'input2':'QOKdVowqhaSWcHKqZKoq/GetLYM8+QGA6dsrR573H0+JX/f+mPpSSQQGev8cmra3QCvakGAWw53u2/XCLXS99lfYDSxvSzkM0vFHW08vNCTroqv02eMuUDrMIvX+byItrlxmzW2Fi1hCQO+u0NNXYS/cw6UnIkSRukzFeGoUBfI=',
    'remember':True
    }
#session登陆
s=requests.Session()
# with requests.Session() as s:
#     s.get('http://httpbin.org/get')
r=s.post(url,json=payload,headers=headers,verify=False)
# print r.json()
#




#保存草稿箱
url2= "https://i.cnblogs.com/EditPosts.aspx?opt=1"
body = {"__VIEWSTATE": "",
        "__VIEWSTATEGENERATOR":"FE27D343",
        "Editor$Edit$txbTitle":"这是我的标题：this my ti",
        "Editor$Edit$EditorBody":"<p>这里是中文内容eeee：hketang/</p>",
        "Editor$Edit$Advanced$ckbPublished":"on",
        "Editor$Edit$Advanced$chkDisplayHomePage":"on",
        "Editor$Edit$Advanced$chkComments":"on",
        "Editor$Edit$Advanced$chkMainSyndication":"on",
        "Editor$Edit$lkbDraft":"存为草稿",
         }
r2 = s.post(url2, data=body, verify=False)
print r.content