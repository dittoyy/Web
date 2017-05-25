#coding:utf-8
#j禁止重定向redirects
import requests
url = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
           }  # get方法其它加个ser-Agent就可以了


s = requests.session()
r = s.get(url, headers=headers,allow_redirects=False,verify=False)
print r.status_code
new_url=r.headers['Location']
print new_url
#Location: /user/signin?ReturnUrl=http%3a%2f%2fi.cnblogs.com%2fEditPosts.aspx%3fopt%3d1

# allow_redirects=True