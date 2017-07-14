#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-10 14:12:18
# @Author  : ditto (969956574@qq.com)
# @Link    : https://github.com/dittoyy
# @Version : $Id$
from selenium import webdriver
import exescript

d=webdriver.PhantomJS("phantomjs")
d.get("http://www.cnblogs.com/")
exejs=exescript.ExeJs(d)
exejs.exeWrap('$(".post_item").length')
print exejs.getMsg()
#out:
"""
20
"""

jsstr="""(function(){
var r=[];
$(".post_item").each(function(){
  var $this=$(this);
  var $h3=$this.find("h3");
  r.push($h3.text());
});
return r.join(',');})()"""
exejs.exeWrap(jsstr)
l=exejs.getMsg()
for title in l.split(','):
    print title
#out:
# 20
# 编译原理——算符优先分析文法（附源代码）
# 常用页面布局分享
# [Open Source] RabbitMQ 高可用集群方案
# OpenCV探索之路（十）：图像修复技术
# Neo4j 第二篇：图形数据库
# 写给Android App开发人员看的Android底层知识（3）
# Java编程之委托代理回调、内部类以及匿名内部类回调(闭包回调)
# JavaScript性能优化 DOM编程
# SQLServer 延迟事务持久性
# Android官方架构组件介绍之LifeCycle
# 把需求变化带来的代码修改成本降至最低的一种方法
# My-Blog搭建过程：如何让一个网站从零到可以上线访问
# .Net程序员学用Oracle系列(28)：PLSQL 之SQL分类和动态SQL
# 提高逼格，给自己的网站加入智能聊天功能
# 饿了么订单--快到碗里来
# 云计算之路-阿里云上：攻击火上浇油，与云盾玩起了踢皮球
# 白话讲session
# Nodejs 进阶：Express 常用中间件 body-parser 实现解析
# 读Zepto源码之集合操作
# 在CentOS上使用Jexus托管运行 ZKEACMS