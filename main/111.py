#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/7/9 14:09
# @Author : liu yang
# @Desc:

import pandas as pd


df = pd.read_excel('/Users/liuyang/Downloads/test.xls',
                       nrows=2,
                       skiprows=5,
                       header=None)
                       # skiprows=75,
                       # header=[0, 1])


# def get_info(df):
#     df.dropna(axis=1, how='any', inplace=True)
#     df.columns = list(range(len(df.columns)))

df.dropna(axis=1, how='any', inplace=True)
print(000)
