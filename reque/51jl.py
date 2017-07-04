#coding:utf-8
import logging
def main():
    logging.basicConfig(format='%(levelname)s:%(message)s',
            level=logging.WARN)

    print('这是一个帮助IT人士在北上广深找工作的程序，网站是前程无忧，'\
            '按照指示操作，enjoy it.')
    name = input('请输入帐号:')
    passwd = input('请输入密码:')

    sc = User(name, passwd)
    loginCookies = sc.login()
    if not loginCookies:
        logging.warn('结束')
        return

    keyWord = input('职位:')
    html, ssCookies = sc.searchFirst(loginCookies, keyWord)
    cookies = dict(loginCookies, **ssCookies)
    jobids, nextPageUrl = sc.parseSearchFirst(html)
    logging.warn('第1页，共%d个职位' % len(jobids))
    print()
    if len(jobids) == 0:
        logging.warn('结束')
        return
    sc.submitResume(jobids, cookies)
main()