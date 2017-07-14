#coding=utf-8
from selenium import webdriver
import os

driver = webdriver.Chrome()

#打开上传功能页面
file_path =  'file:///' + os.path.abspath('uplad.html')
driver.get(file_path)

#点击打开上传窗口
driver.find_element_by_name("file").click()
#调用upfile.exe上传程序
os.system("D:\\upfile2.exe")

# driver.quit()