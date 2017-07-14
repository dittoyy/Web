#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-14 10:33:05
# @Author  : ditto (969956574@qq.com)
# @Link    : https://github.com/dittoyy
# @Version : $Id$

# coding=utf-8

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import redis

class Redis:

    def __init__(self, host='127.0.0.1', port=6379, db=0, password=None):
        self.__conn = redis.Redis(connection_pool=redis.BlockingConnectionPool(max_connections=15,host=host, port=port, db=db, password=password))

    def __getattr__(self, command):
        def _(*args):
            return getattr(self.__conn, command)(*args) # 重新组装方法调用
        return _

if __name__ == '__main__':
    conn = Redis()
    print conn.set('test', 'yes')#True
