#coding:utf-8
from  selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import  ActionChains

import time

from selenium.common.exceptions import NoSuchElementException



driver = webdriver.Firefox()

driver.implicitly_wait(20)

driver.maximize_window()

driver.get("http://www.yibaolib.com/Login.aspx")



user = driver.find_element_by_css_selector('#ContentPlaceHolder1_txtPhone').send_keys('15755172398')
js='$("#ContentPlaceHolder1_txtPwd").style.display=""'
driver.execute_script(js)
pwd = driver.find_element_by_css_selector('#ContentPlaceHolder1_txtPwd').send_keys('456789')

# p=driver.find_element_by_css_selector('#ContentPlaceHolder1_txtPwd')



driver.find_element_by_css_selector('#ContentPlaceHolder1_txtPwd').send_keys(Keys.ENTER)



time.sleep(10)

# js = "var q=document.body.scrollTop=10000"

# driver.execute_script(js)

# 为了快速滑动，先设置超时时间为1秒

driver.implicitly_wait(1)



# 不停的滑啊滑

while True:

    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    try:

        # 定位页面底部的一个标题

        driver.find_element_by_xpath('//*[@id="waterfall"]/div[2]/div[33]/div/div/a')

        # 如果没抛出异常就说明找到了底部标志，跳出循环

        break

    except NoSuchElementException as e:

        # 抛出异常说明没找到底部标志，继续向下滑动

        pass



# 将超时时间改回10秒

driver.implicitly_wait(10)



title=driver.find_elements_by_xpath('//*[@id="waterfall"]/div/div/div/div/a')

print(len(title))

for  i in title:

    print(i.text)

