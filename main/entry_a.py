#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/7/26 17:14
# @Author : liu yang
# @Desc: 主程序
import datetime
import os

import pandas as pd

from common.extract_helper_a import ExtractHelperA
from common.index_tools_a import IndexToolsA
from common.path_helper import PathHelper


class EntryA:

    def __init__(self,
                 file):
        self.file = file
        self.tools = IndexToolsA(file)

    def run(self):
        row_idx, row_cnt = self.tools.get_row_index()
        start_date, end_date = self.tools.get_date()
        output = pd.DataFrame()

        for idx in range(0, len(row_idx)):
            df_info = pd.read_excel(self.file,
                                    nrows=1,
                                    sheet_name='员工刷卡记录表',
                                    skiprows=row_idx[idx],
                                    header=None)
            work_number, name = ExtractHelperA.get_info(df_info)

            df_record = pd.read_excel(self.file,
                                      nrows=(row_cnt[idx]),
                                      sheet_name='员工刷卡记录表',
                                      skiprows=(row_idx[idx] + 2),
                                      header=None)

            if df_record.size > 0:
                df_check = ExtractHelperA.get_record(df_record, start_date, end_date)
            else:
                continue

            for ix, row in df_check.iterrows():
                row_not_null = row[row.notnull()]
                for row_ix, row_value in row_not_null.items():
                    work_time = row[row_ix].split()
                    for time in work_time:
                        dic = {'序号': [work_number],
                               '姓名': [name],
                               # '部门': [section],
                               '日期': [row_ix],
                               '打卡时间': [time]}
                        output = output.append(pd.DataFrame(dic))

        try:
            output.to_excel(PathHelper.out_path(self.file, 'output', '/a'), index=False)
            print('写入完成')
        except:
            print('文件持久化错误...')


if __name__ == "__main__":
    file_name = '/Users/liuyang/Downloads/员工刷卡记录表（彩云城体验中心）.xls'
    EntryA(file_name).run()
