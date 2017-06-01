#coding=utf-8
from  selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re,time
##########加载profile，可以免登陆
#profile = webdriver.FirefoxProfile(r'C:\Users\Administrator\AppData\Local\Mozilla\Firefox\Profiles\urkg7uqr.default')
#driver = webdriver.Firefox(profile,timeout=300)

#driver = webdriver.Firefox(timeout=50)
driver=webdriver.Chrome()
driver.get('https://tieba.baidu.com/p/4778694923')
str_cookie='BIDUPSID=1B0EC2BA376CBF4E68F4952620B2C7A6; PSTM=1491645170; BDUSS=3NNcWtmZHI2MXdqaE55MUhUN35EYTR-cHppV2VCdDYxLXE5T3Z5eTVvNlhRQkJaSVFBQUFBJCQAAAAAAAAAAAEAAAAw2CBnudvS9LTzyqrAsgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJez6FiXs-hYa; BAIDUID=17ECF3B92FDCAFB2D548C94DXXXXXXX:FG=1'     #cookie字符串用f12查看网络中的请求贴吧的，请求头中的cookie
list=re.findall('([\s\S]*?)=([\s\S]*?); ',str_cookie+'; ')
for  l in list:
    ck={'name':l[0],'value':l[1]}
    print ck
    driver.add_cookie(ck)           #来个正则把cookie字符串转成slenium的cookie格式字典，添加到driver。cookie字符串是请求贴吧时用f12查看的 network的headers的请求头的cookie，复制就可以了，这样selenium也可以免登陆
driver.get('https://tieba.baidu.com/p/4778694923')

###########回主贴，写内容但不回帖
driver.find_element_by_id('ueditor_replace').click()
time.sleep(5)                                            #停5秒钟可以发现上面的代码click已经自动拖到页面底部了，没有必要先点击输入框直接赋值也可以，考虑到模拟正常情况，还是点击下，因为百度有些post参数是动态的。
js="document.getElementById('ueditor_replace').innerHTML='abc'"
driver.execute_script(js)


all=driver.find_elements_by_css_selector('div.l_post')     ###获取所有层主的外层div
print all
for a in all:
    #print a.text,'*************************\n'
    bt=''
    try:
        bt=a.find_element_by_id('post_content_106859548218')              ####回复指定的层主

    except Exception,e:
        pass
    if bt!='':
        #a.find_element_by_class_name('lzl_link_unfold').click()    #首次回复
        try:
            bt.click()                            #这句会报错，但可以帮助跳到指定层主，非常有用，如果不跳到指定层主的位置，就会定位不到那个层主的‘我也说一句’的按钮，百度贴吧会在我们离开层主的视界后自动收缩层主的跟帖，所以会造成定位不到。肉眼很难观察到，用f12反复关闭和打开，再搜索可以看到。
        except Exception,e:
            pass
　　　　 time.sleep(3)
        print a.tag_name
        print a.text,'\n*****************************************************************'
        for i in range(1000):
            #driver.find_element_by_xpath('//*[@id="j_p_postlist"]/div[22]/div[2]/div[2]/div[2]/div[2]/ul/li[6]/a').click()   #这种方式不靠谱，前面插了广告或者删了帖子，可能回复层别的层主了
            a.find_element_by_class_name('j_lzl_p').click()
            #a.find_elements_by_partial_link_text('我也说一句')[0].click()     ##我也说一句按钮

            driver.find_element_by_id('j_editor_for_container').click()
            driver.execute_script('document.getElementById("j_editor_for_container").innerHTML="hello"')
            driver.find_element_by_css_selector('.lzl_panel_submit').click()

            time.sleep(60)                 #每隔60秒回帖






从第28行道49行繁琐了一些，功能主要是跳转到指定的层主的页面位置，换种方法也可以这样
floor=dr.find_element_by_xpath('//span[contains(text(),"21楼")]')

dr.execute_script("arguments[0].scrollIntoView();", floor)

time.sleep(2)

#再去定位元素

tar = dr.find_element_by_xpath('//div[contains(@data-field,"157780442")]//a[contains(text(),"我也说一句")]')

tar.click()