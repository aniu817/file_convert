#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/7/12 08:59
# @Author : liu yang
# @Desc: EXCEL 格式转换程序入口


from common.index_helper import IndexHelper
import pandas as pd
from common.extract_helper import ExtractHelper


file_name = '/Users/liuyang/Downloads/test.xls'
row_index = IndexHelper(file_name).get_row_index()
row_count = IndexHelper(file_name).get_row_count(row_index)
date_range = ['6/1/2021', '6/30/2021']
output = pd.DataFrame()

for idx in range(0, len(row_index)):
    a = row_index[idx]
    b = row_count[idx]
    df_info = pd.read_excel(file_name,
                            nrows=1,
                            skiprows=row_index[idx],
                            header=None)
    work_number, name = ExtractHelper.get_info(df_info)

    df_record = pd.read_excel(file_name,
                              nrows=(row_count[idx] - 1),
                              skiprows=(row_index[idx] + 1),
                              header=None)
    df_check = ExtractHelper.get_record(df_record, date_range)

    for ix, row in df_check.iterrows():
        row_not_null = row[row.notnull()]
        for row_idx, row_value in row_not_null.items():
            work_time = row[row_idx].split()
            for time in work_time:
                # dic = {'序号': [1], '姓名': ['刘洋'], '日期': ['20210705'], '打卡时间': ['15：30']}
                dic = {'序号': [work_number], '姓名': [name], '日期': [row_idx], '打卡时间': [time]}
                output = output.append(pd.DataFrame(dic))

output.to_excel('/Users/liuyang/Downloads/1.xlsx', index=False)
