# coding:utf-8
from selenium import webdriver
from login_page import LoginPage, login_url
from login_sucess_page import LoginSucessPage, login_sucess_url
driver = webdriver.Firefox()

# 登录页面操作
driver_login = LoginPage(driver)
driver_login.open(login_url)
driver_login.login(u"上海-悠悠", "xxx")

# 登录成功页面操作
driver_sucess = LoginSucessPage(driver)
driver_sucess.input_sign("hao123")
driver_sucess.click_by_blog()