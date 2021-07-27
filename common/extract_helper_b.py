#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/7/9 15:03
# @Author : liu yang
# @Desc: 提取 EXCEL 数据信息
from abc import ABC

import pandas as pd
import numpy as np

from interface.extract_operation import ExtractOperation


class ExtractHelperB(ExtractOperation, ABC):

    @staticmethod
    def get_info(df_info):
        """
        :param df_info:只取工号、姓名、公司那一行的数据
        :return:返回工号、姓名
        """
        df_info.dropna(axis=1, how='any', inplace=True)
        df_info.columns = list(range(len(df_info.columns)))
        # return df_info.iloc[0][1], df_info.iloc[0][3], df_info.iloc[0][5]
        return df_info.iloc[0][1], df_info.iloc[0][3]

    @staticmethod
    def get_record(df_record, start_date, end_date, mode='%Y%m%d'):
        """

        :param start_date: 开始日期
        :param end_date: 结束日期
        :param df_record: 取序号以及考勤数据行
        :param mode: 格式为 YYYYMMDD
        :return: 返回打卡记录以及对应的日期
        """
        # df_record = df_record.drop(0, axis=1)
        col_cnt = pd.date_range(start_date, end_date).size
        df_record = df_record.iloc[:, :col_cnt]
        df_record.columns = pd.date_range(start_date, end_date)
        df_record.columns = df_record.columns.to_series().apply(lambda x: x.strftime(mode))
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
    ExtractHelperB.get_record(df, ['6/1/2021', '6/30/2021'])
