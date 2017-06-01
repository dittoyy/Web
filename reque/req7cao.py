# coding:utf-8
import requests

url = "https://passport.cnblogs.com/user/signin"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
           "Accept": "application/json, text/javascript, */*; q=0.01",
           "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
           "Accept-Encoding": "gzip, deflate, br",
           "Content-Type": "application/json; charset=utf-8",
           "X-Requested-With": "XMLHttpRequest",
           "Content-Length": "385",
           "Cookie": "xxx已省略",
           "Connection": "keep-alive"
           }

payload={
    'input1':'GQkdwv67Go1T8kNLmO1WAos9I5QFC8WEOSU7QuptbKKBHDMfC6A7GLfCIgAie0G4Ky9SzMxuCymcgx/HS48RBo8bIKRI49A1U1RbfN8rh7YrIoN7CKmMVnRPyKJAF1JitfMe5hvBxOLSfUdSkESfD1R2FpnMR2ZHUWddeWge+FY=',
    'input2':'QOKdVowqhaSWcHKqZKoq/GetLYM8+QGA6dsrR573H0+JX/f+mPpSSQQGev8cmra3QCvakGAWw53u2/XCLXS99lfYDSxvSzkM0vFHW08vNCTroqv02eMuUDrMIvX+byItrlxmzW2Fi1hCQO+u0NNXYS/cw6UnIkSRukzFeGoUBfI=',
    'remember':True
    }

# 第一步：session登录
s = requests.session()
r = s.post(url, json=payload, headers=headers, verify=False)
print r.json()

# 第二步：保存草稿
url2 = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
body = {"__VIEWSTATE": "",
        "__VIEWSTATEGENERATOR": "FE27343",
        "Editor$Edit$txbTitle": "top11111144444444444411111",
        "Editor$Edit$EditorBody": "<p>这pageos vvvvvvvvvvvvv/</p>",
        "Editor$Edit$Advanced$ckbPublished": "on",
        "Editor$Edit$Advanced$chkDisplayHomePage": "on",
        "Editor$Edit$Advanced$chkComments": "on",
        "Editor$Edit$Advanced$chkMainSyndication": "on",
        "Editor$Edit$lkbDraft": "存为草稿",
        }

r2 = s.post(url2, data=body, verify=False)
# 获取当前url地址
print r2.url

# 第三步：正则提取需要的参数值
import re
postid = re.findall(r"postid=(.+?)&", r2.url)
print postid  # 这里是list
# 提取为字符串
print postid[0]

# 第四步：删除草稿箱
url3 = "https://i.cnblogs.com/post/delete"
json3 = {"postId": postid[0]}
r3 = s.post(url3, json=json3, verify=False)
print r3.json()
