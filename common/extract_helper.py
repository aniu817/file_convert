#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/7/9 15:03
# @Author : liu yang
# @Desc: 提取 EXCEL 数据信息

import pandas as pd
import numpy as np


class ExtractHelper:

    @staticmethod
    def get_info(df_info):
        df_info.dropna(axis=1, how='any', inplace=True)
        df_info.columns = list(range(len(df.columns)))
        return df_info.iloc[0][1], df_info.iloc[0][3]

    @staticmethod
    def get_record(df_record, mode='%Y%m%d'):
        df_record.dropna(axis=1, how='all', inplace=True)
        df_record.iloc[0] = pd.date_range('6/1/2021', '6/30/2021')
        df_record.iloc[0] = df_record.iloc[0].apply(lambda x: x.strftime(mode))
        df_record.columns = df_record.iloc[0]
        df_record.drop([0],  inplace=True)
        for idx, row in df_record.iterrows():
            for col_idx, tag in row.iteritems():
                if np.isnan(tag):
                    pass
                else:
                    work_time = row[col_idx].split()
                    for time in work_time:
                        return col_idx, time


if __name__ == "__main__":
    # df = pd.read_excel('/Users/liuyang/Downloads/test.xls',
    #                    nrows=1,
    #                    skiprows=4,
    #                    header=None)
    # ExtractHelper.get_info(df)

    df = pd.read_excel('/Users/liuyang/Downloads/test.xls',
                       nrows=2,
                       skiprows=5,
                       header=None)
    ExtractHelper.get_record(df)
