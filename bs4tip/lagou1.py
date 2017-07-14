#coding:utf-8

import json
import requests


class LagoupositionSpider():
    name = "LagouPosition"
    totalPageCount = 1
    curpage = 1
    city = '杭州'
    myurl = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city={}&needAddtionalResult=false'.format(city)

    header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
    }

    kds = ['Python工程师', '大数据', '云计算', 'docker', '中间件', 'Node.js', '数据挖掘', \
           '自然语言处理', '搜索算法', '精准推荐', '全栈工程师', '图像处理','机器学习', '语音识别']
    kd = kds[0]

    def start_requests(self,cur):
        post_data = {'first': 'false', 'pn': str(cur), 'kd': self.kd}
        html = requests.post(self.myurl, data=post_data, headers=self.header)
        html_text = html.text
        return html_text

    def get_result(self):
        result = self.start_requests(self.curpage)
        jdict = json.loads(result)
        jcontent = jdict['content']
        jposresult = jcontent['positionResult']
        jresult = jposresult['result']
        self.totalPageCount = jposresult['totalCount'] / 15 + 1
        for each in jresult:
            positionName = each['positionName'].encode('gbk')
            companyFullName = each['companyFullName'].encode('gbk')
            workYear = each['workYear'].encode('gbk')
            salary = each['salary'].encode('gbk')
            district = self.city.decode('utf-8').encode('gbk')
            with open(r'F:\python.csv', 'ab+') as f:
                f.write('{},{},{},{},{},{}'.format(positionName, district, companyFullName, workYear, salary, '\n'))
        if self.curpage <=  self.totalPageCount:
            self.curpage += 1
            self.start_requests(self.curpage)
            self.get_result()

if __name__ == '__main__':
    lagouspider = LagoupositionSpider()
    lagouspider.get_result()