# -*- coding:utf-8 -*-
__author__ = u'harry'

import win32com
from win32com.client import Dispatch,constants
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))# Excel表格中测试结果底色
OK_COLOR = 0xffffff
False_COLOR = 0xff
# NT_COLOR=0xffff
NT_COLOR = 0xC0C0C0

# Excel表格中测试结果汇总显示位置
TESTTIME = [1, 14]
TESTRESULT = [2, 14]

# Excel模版设置
# self.titleindex=3        #Excel中测试用例标题行索引
# self.casebegin =4        #Excel中测试用例开始行索引
# self.argbegin   =3       #Excel中参数开始列索引
# self.argcount  =8        #Excel中支持的参数个数
class excel():
    # def __init__(self, sFile, dtitleindex=3, dcasebegin=4, dargbegin=3, dargcount=8):
    def __init__(self, sFile):
        self.xlApp = win32com.client.Dispatch('Excel.Application')  # MS:Excel  WPS:et
        try:
            self.book = self.xlApp.Workbooks.Open(sFile)
        except:
            print(u"打开文件失败")
            exit()

    def close(self):
        # self.book.Close(SaveChanges=0)
        #self.book.Save()
        self.book.Close(SaveChanges=0)
        # self.xlApp.Quit()
        del self.xlApp

    def read(self, iSheet, iRow, iCol):
        try:
            sht = self.book.Worksheets(iSheet)
            sValue = str(sht.Cells(iRow, iCol).Value)
        except:
            self.close()
            print(u'读取数据失败')
            exit()
            # 去除'.0'
        if sValue[-2:] == '.0':
            sValue = sValue[0:-2]
        return sValue

    def write(self, iSheet, iRow, iCol, sData):
        try:
            sht = self.book.Worksheets(iSheet)
            sht.Cells(iRow, iCol).Value = sData  # .decode("utf-8")
            if sData == "Failed":
                sht.Cells(iRow, iCol).Interior.Color = False_COLOR
                self.book.Save()
            else:
                sht.Cells(iRow, iCol).Interior.Color = OK_COLOR
                self.book.Save()
        except Exception:
            self.close(SaveChanges=0)
            print(u'写入数据失败:'+Exception)
            exit()

'''
excelpath = r'D:\template\template1\log\TestCase1.xls'
test = excel(excelpath)
test.write(2, 11, 7,"aaa")
test.close()
'''