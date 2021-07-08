#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/7/7 09:47
# @Author : liu yang
# @Desc: EXCEL 表格格式转换


import pandas as pd
import numpy as np

from common.config_helper import ConfigHelper

output = pd.DataFrame()
base_num = 0
skip_rows = 0
cols = pd.date_range('5/31/2021', '6/30/2021')
month = '202106'

value_list = ConfigHelper.config_parser('row_list', 'rows', 'row').split(',')
while base_num < 36:
    # print(base_num)
    skip_rows = skip_rows + int(value_list[base_num])
    print(skip_rows)
    if value_list[base_num + 1] == '4':
        rows = 2
    else:
        rows = 1

    df = pd.read_excel('/Users/liuyang/Downloads/test.xls',
                       nrows=rows,
                       skiprows=skip_rows,
                       # skiprows=75,
                       header=[0, 1])
    df.fillna('missing', inplace=True)
    is_null = False
    for idx, tag in df.iloc[0].str.contains('工号').iteritems():
        if tag:
            is_null = tag
            break
    if is_null:
        base_num = base_num + 1
        continue
    else:
        doc_idx = df.columns.values[5][0]
        name = df.columns.values[12][0]

        df.columns = df.columns.to_flat_index()
        # df.columns = np.arange(0, days + 1, 1)
        df.columns = cols
        for index, row in df.iterrows():
            for idx, tag in row.str.contains('missing').iteritems():
                if tag:
                    continue
                else:
                    work_time = row[idx].split()
                    for time in work_time:
                        # dic = {'序号': [1], '姓名': ['刘洋'], '日期': ['20210705'], '打卡时间': ['15：30']}
                        dic = {'序号': [doc_idx], '姓名': [name], '日期': [idx], '打卡时间': [time]}
                        output = output.append(pd.DataFrame(dic))
        base_num = base_num + 1

print(output)
output.to_excel('/Users/liuyang/Downloads/winner.xlsx', index=False)
