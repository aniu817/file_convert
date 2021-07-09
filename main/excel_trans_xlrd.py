#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/7/9 08:59
# @Author : liu yang
# @Desc: xlrd excel 格式转化


import xlrd

file_name = '/Users/liuyang/Downloads/test.xls'
sheet_name = '员工刷卡记录表'
row_list = []
row_tag = '工号'

workBook = xlrd.open_workbook(file_name)
data = workBook.sheet_by_name(sheet_name)

row_count = data.nrows
for idx in range(row_count):
    row_data = data.row_values(idx)
    for value in row_data:
        if row_tag in str(value):
            row_list.append(idx)


print(row_list)


