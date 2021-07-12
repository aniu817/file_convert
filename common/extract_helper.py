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
        """
        :param df_info:只取工号、姓名、公司那一行的数据
        :return:返回工号、姓名
        """
        df_info.dropna(axis=1, how='any', inplace=True)
        df_info.columns = list(range(len(df_info.columns)))
        return df_info.iloc[0][1], df_info.iloc[0][3]

    @staticmethod
    def get_record(df_record, date_range, mode='%Y%m%d'):
        """
        :param date_range: list，开始、结束日期
        :param df_record: 取序号以及考勤数据行
        :param mode: 格式为 YYYYMMDD
        :return: 返回打卡记录以及对应的日期
        """
        df_record.dropna(axis=1, how='all', inplace=True)
        df_record.iloc[0] = pd.date_range(date_range[0], date_range[1])
        df_record.iloc[0] = df_record.iloc[0].apply(lambda x: x.strftime(mode))
        df_record.columns = df_record.iloc[0]
        df_record.drop([0],  inplace=True)
        return df_record


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
    ExtractHelper.get_record(df, ['6/1/2021', '6/30/2021'])
