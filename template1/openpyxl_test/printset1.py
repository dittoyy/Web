#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-11 09:57:12
# @Author  : ditto (969956574@qq.com)
# @Link    : https://github.com/dittoyy
# @Version : $Id$

from openpyxl.workbook import Workbook

wb = Workbook()
ws = wb.active
data = [
    ["Fruit", "Quantity"],
    ["Kiwi", 3],
    ["Grape", 15],
    ["Apple", 3],
    ["Peach", 3],
    ["Pomegranate", 3],
    ["Pear", 3],
    ["Tangerine", 3],
    ["Blueberry", 3],
    ["Mango", 3],
    ["Watermelon", 3],
    ["Blackberry", 3],
    ["Orange", 3],
    ["Raspberry", 3],
    ["Banana", 3]
]

for r in data:
    ws.append(r)

ws.auto_filter.ref = "A1:B15"
ws.auto_filter.add_filter_column(0, ["Kiwi", "Apple", "Mango"])
ws.auto_filter.add_sort_condition("B2:B15")

# Print Options
ws.print_options.horizontalCentered = True
ws.print_options.verticalCentered = True
# Headers and Footers
ws.oddHeader.left.text = "Page &[Page] of &N"
ws.oddHeader.left.size = 14
ws.oddHeader.left.font = "Tahoma,Bold"
ws.oddHeader.left.color = "CC3366"
# Print Titles
ws.print_title_cols = 'A:B' # the first two cols
ws.print_title_rows = '1:1' # the first row
# Print Area
ws.print_area = 'A1:F10'
wb.save('print1.xlsx')

