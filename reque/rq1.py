#coding:utf-8
import requests,json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

par={'type':'yunda','postid':'3901357983152'}
# data_json=json.dumps(par)
r=requests.get('https://www.kuaidi100.com/query',params=par,verify=False)
content=r.json()
print type(content)



def format_json(content):
    """
    格式化JSON
    """
    if isinstance(content, basestring):
        content = json.loads(content)

    if 1:
        result = json.dumps(content, sort_keys=True, indent=4, separators=(',', ': ')). \
            encode('latin-1').decode('unicode_escape')
    else:
        result = json.dumps(content, sort_keys=True, indent=4, separators=(',', ': ')). \
            decode("unicode_escape")

    return result


def pretty_print(content):
    """
    美化打印
    """
    print(format_json(content))

pretty_print(content)







'''https://www.kuaidi100.com/query?type=yunda&postid=3901357983152'''
'''{
    "message": "ok",
    "nu": "3901357983152",
    "ischeck": "1",
    "condition": "F00",
    "com": "yunda",
    "status": "200",
    "state": "3",
    "data": [
        {
            "time": "2017-05-10 10:41:59",
            "ftime": "2017-05-10 10:41:59",
            "context": "[福建漳州公司]快件已被 已签收 签收",
            "location": "福建漳州公司"
        },
        {
            "time": "2017-05-10 10:40:59",
            "ftime": "2017-05-10 10:40:59",
            "context": "[福建漳州公司]进行派件扫描；派送业务员：黄春香；联系电话：18350649825",
            "location": "福建漳州公司"
        },
        {
            "time": "2017-05-09 15:17:43",
            "ftime": "2017-05-09 15:17:43",
            "context": "[福建晋江分拨中心]从站点发出，本次转运目的地：福建漳州公司",
            "location": "福建晋江分拨中心"
        },
        {
            "time": "2017-05-09 09:57:10",
            "ftime": "2017-05-09 09:57:10",
            "context": "[福建晋江分拨中心]在分拨中心进行卸车扫描",
            "location": "福建晋江分拨中心"
        },
        {
            "time": "2017-05-08 00:00:02",
            "ftime": "2017-05-08 00:00:02",
            "context": "[北京分拨中心]进行装车扫描，即将发往：福建晋江分拨中心",
            "location": "北京分拨中心"
        },
        {
            "time": "2017-05-07 23:53:12",
            "ftime": "2017-05-07 23:53:12",
            "context": "[北京分拨中心]进行中转集包扫描，将发往：福建晋江分拨中心漳龙集包代码",
            "location": "北京分拨中心"
        },
        {
            "time": "2017-05-07 22:13:46",
            "ftime": "2017-05-07 22:13:46",
            "context": "[北京分拨中心]在分拨中心进行称重扫描",
            "location": "北京分拨中心"
        },
        {
            "time": "2017-05-07 19:32:23",
            "ftime": "2017-05-07 19:32:23",
            "context": "[北京西城区平安里公司]进行装车扫描，即将发往：北京分拨中心",
            "location": "北京西城区平安里公司"
        },
        {
            "time": "2017-05-04 14:55:26",
            "ftime": "2017-05-04 14:55:26",
            "context": "[北京西城区平安里公司]进行派件扫描；派送业务员：陈；联系电话：18518659360",
            "location": "北京西城区平安里公司"
        },
        {
            "time": "2017-05-04 10:35:49",
            "ftime": "2017-05-04 10:35:49",
            "context": "[北京西城区平安里公司]快件异常；备注：客户拒收",
            "location": "北京西城区平安里公司"
        },
        {
            "time": "2017-04-29 14:35:34",
            "ftime": "2017-04-29 14:35:34",
            "context": "[北京西城区平安里公司]进行派件扫描；派送业务员：陈；联系电话：18518659360",
            "location": "北京西城区平安里公司"
        },
        {
            "time": "2017-04-29 14:29:45",
            "ftime": "2017-04-29 14:29:45",
            "context": "[北京西城区平安里公司]到达目的地网点，快件将很快进行派送",
            "location": "北京西城区平安里公司"
        },
        {
            "time": "2017-04-29 10:52:10",
            "ftime": "2017-04-29 10:52:10",
            "context": "[北京分拨中心]从站点发出，本次转运目的地：北京西城区平安里公司",
            "location": "北京分拨中心"
        },
        {
            "time": "2017-04-29 09:06:55",
            "ftime": "2017-04-29 09:06:55",
            "context": "[北京分拨中心]在分拨中心进行卸车扫描",
            "location": "北京分拨中心"
        },
        {
            "time": "2017-04-27 21:54:52",
            "ftime": "2017-04-27 21:54:52",
            "context": "[福建晋江分拨中心]进行装车扫描，即将发往：北京分拨中心",
            "location": "福建晋江分拨中心"
        },
        {
            "time": "2017-04-27 21:52:39",
            "ftime": "2017-04-27 21:52:39",
            "context": "[福建晋江分拨中心]在分拨中心进行称重扫描",
            "location": "福建晋江分拨中心"
        },
        {
            "time": "2017-04-27 18:16:54",
            "ftime": "2017-04-27 18:16:54",
            "context": "[福建漳州公司]进行下级地点扫描，将发往：北京网点包",
            "location": "福建漳州公司"
        },
        {
            "time": "2017-04-27 12:34:17",
            "ftime": "2017-04-27 12:34:17",
            "context": "[福建漳州公司]进行揽件扫描",
            "location": "福建漳州公司"
        }
    ]
}'''