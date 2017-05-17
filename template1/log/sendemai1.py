# TODO(harry.he@xiucai.com):这是邮件发送的代码
# -*- coding:utf-8 -*-
__author__ = u'harry'

import smtplib
import time
import string

from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from xiucai.xiucai_s import excel
excelpath = 'D:\\python\\DATA\\TestCase1.xls'


class post:
    def send_mail(self):
        excelX = excel.excel(excelpath)
        email_from = "email@email.com" #邮件发送人
        email_to = ["email@email.com","email@email.com"]    #收件人
        email_Sub = "自动化测试报告"+str(time.strftime("%Y/%m/%d",time.localtime()))

        msg = MIMEMultipart()
        msg['From'] = Header(email_from, 'utf-8')
        msg['To'] = Header("自动化测试报告收件人", 'utf-8')
        msg['Subject'] = Header(email_Sub,'utf-8')
        # 邮件主体内容
        mail_body = ("<table border=1 cellspacing=0 cellpadding=10 ><font face=Verdana><tr><td bgcolor=c5d9f1 align=right>"+ excelX.read(1,2,2) + "</td><td align=left>" + excelX.read(1,3,2) + "</td></tr>" +
                                          "<tr><td bgcolor=c5d9f1 align=right>"+excelX.read(1,2,3) + "</td><td align=left>" +excelX.read(1,3,2) + "</td></tr>" +
                                          "<tr><td bgcolor=c5d9f1 align=right>"+excelX.read(1,2,4) + "</td><td align=left>" +excelX.read(1,3,4) + "</td></tr>" +
                                          "<tr><td bgcolor=c5d9f1 align=right>"+excelX.read(1,2,5) + "</td><td align=left>" +excelX.read(1,3,5) + "</td></tr>" +
                                          "<tr><td bgcolor=c5d9f1 align=right>"+excelX.read(1,2,6) + "</td><td align=left>" +format(float(excelX.read(1,3,6)), '.0%') + "</td></tr>" +
                                          "<tr><td bgcolor=c5d9f1 align=right>"+excelX.read(1,2,7) + "</td><td align=left>" +format(float(excelX.read(1,3,7)), '.0%') + "</td></tr>" +"</td></tr></center></font></table>")

        # 邮件正文内容  "plain","html"
        msg.attach(MIMEText(mail_body, 'html', 'utf-8'))
        # 构造附件，传送当前目录下的 文件
        att = MIMEText(open(excelpath, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att["Content-Disposition"] = 'attachment; filename="TestCase.xls"'
        msg.attach(att)

        smtp = smtplib.SMTP()
        try:
            smtp.connect("smtp.exmail.qq.com") #使用的邮箱smtp服务器
            smtp.login(email_from,'Emailpassword') #邮箱登录
            smtp.sendmail(email_from,email_to,msg.as_string())#发送邮件内容
            smtp.quit() #关闭链接
            excelX.close()
            print("邮件已发送成功")
        except smtplib.SMTPException:
            print("Error:邮件发送失败")

#post().send_mail()