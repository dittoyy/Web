# coding:utf-8
from selenium import webdriver
def browser(browser='firefox'):
    """
    打开浏览器函数，"firefox"、"chrome"、"ie"、"phantomjs"
    """
    try:
        if browser == "firefox":
            profile=webdriver.FirefoxProfile(r'C:\Users\ditto.he\AppData\Roaming\Mozilla\Firefox\Profiles\r8tbe0ai.default')
            profile.accept_untrusted_certs=True
            driver=webdriver.Firefox(firefox_profile=profile)
            return driver
        elif browser == "chrome":
            options=webdriver.ChromeOptions()
            options.add_argument('--ignore-certificate-errors')
            driver=webdriver.Chrome(chrome_options=options)
            return driver
        elif browser == "ie":
            capabilities = webdriver.DesiredCapabilities().INTERNETEXPLORER
            capabilities['acceptSslCerts'] = True
            driver = webdriver.Ie(capabilities=capabilities)
            return driver
        elif browser == "phantomjs":
            driver = webdriver.PhantomJS()
            return driver
        else:
            print("Not found this browser,You can enter 'firefox', 'chrome', 'ie' or 'phantomjs'")
    except Exception as msg:
        print "browser error is : %s" % msg
class My_selenium():               # 这个是底层二次封装selenium
    def __init__(self, driver):
        self.driver = driver       # 参数化driver

    def open(self, url):
        self.driver.get(url)

class Page1(My_selenium):         # 这个是page1页面的所以操作，继承上面类
    def open_n(self,url):
        self.open(url)

class Page2(My_selenium):         # 这个是page2页面的所以操作，继承上面类
    def open_n(self,url):
        self.open(url)
if __name__ == "__main__":
    # driver = webdriver.Firefox()    # 这个driver是打开空浏览器，只打开一次
    s=browser()
    driver1 = Page1(s)         # 这个driver是打开page1页面实例
    driver1.open("http://www.baidu.com")
    driver2 = Page2(s)         # 这个driver是打开page2页面实例
    driver2.open("http://www.cnblogs.com/")
