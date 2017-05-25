#coding:utf-8

import requests
#加上headers模拟浏览器等访问
##verify=False以防ssl问题
url='https://passport.cnblogs.com/user/signin'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json; charset=utf-8",
            "X-Requested-With": "XMLHttpRequest",
            "Cookie": "ccc",  # 此处cookie省略了

            "Connection":"keep-alive"
            }
'''SERVERID=9b2e527de1fc6430919cfb3051ec3e6c|1493001791|1493001791; AspxAutoDetectCookieSupport=1; .Cnblogs.AspNetCore.Cookies=CfDJ8Mmb5OBERd5FqtiQlKZZIG7_TyGSv5MJorL6C_IXtTkYrai9MG3hSOAQMuVmYXQ-YT0IokX62E9Tac0_CmVQyYFSzeizl1FahYHsCqvZk38Pnd9ETZ14Yy9GF7IyxQJrHrq8l0uraO1lPkxZZYm5oz4yWv_CH2RgDKBQZq19CriUiOT_MGDoH5pmKBuJ1F1zY22Ca0u3_-l788Q7Oe0MxKUOT8oU07VhOEi9JSeSpeDj1suGVJWjG8oKQ8k5hCuVX-CBodDRjeO_2qyVVRePpoOyDcMQkqV6njFOQxJbaGn0nYa85q0WMO92-5QIgYJ0cw;
                                                 _ga=GA1.2.1708797398.1492748076'''
payload={
    'input1':'GQkdwv67Go1T8kNLmO1WAos9I5QFC8WEOSU7QuptbKKBHDMfC6A7GLfCIgAie0G4Ky9SzMxuCymcgx/HS48RBo8bIKRI49A1U1RbfN8rh7YrIoN7CKmMVnRPyKJAF1JitfMe5hvBxOLSfUdSkESfD1R2FpnMR2ZHUWddeWge+FY=',
    'input2':'QOKdVowqhaSWcHKqZKoq/GetLYM8+QGA6dsrR573H0+JX/f+mPpSSQQGev8cmra3QCvakGAWw53u2/XCLXS99lfYDSxvSzkM0vFHW08vNCTroqv02eMuUDrMIvX+byItrlxmzW2Fi1hCQO+u0NNXYS/cw6UnIkSRukzFeGoUBfI=',
    'remember':True
    }
r=requests.post(url,json=payload,headers=headers,verify=False)
print r.json()