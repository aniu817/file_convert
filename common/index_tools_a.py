#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/7/26 15:31
# @Author : liu yang
# @Desc: 返回 a 格式考勤机数据索引


from abc import ABC

from interface.index_operation import IndexOperation
from common.sheet_reader import SheetReader
import numpy as np


class IndexToolsA(IndexOperation, ABC):

    def __init__(self,
                 file,
                 row_tag='姓',
                 row_list=[],
                 date_tag='考勤'):
        self.sheet_data = SheetReader.get_sheet(file)
        self.row_tag = row_tag
        self.row_list = row_list
        self.date_tag = date_tag

    def get_row_index(self):
        for idx in range(self.sheet_data.nrows):
            row_data = self.sheet_data.row_values(idx)
            for value in row_data:
                if self.row_tag in str(value):
                    self.row_list.append(idx)

        diff = [self.row_list[idx + 1] - self.row_list[idx] for idx in range(len(self.row_list) - 1)]
        last_row_cnt = self.sheet_data.nrows - self.row_list[-1]
        diff.append(last_row_cnt)
        row_cnt = (np.array(diff) - 2).tolist()
        row_cnt[-1] = 1 if row_cnt[-1] == 0 else row_cnt[-1]
        return self.row_list, row_cnt

    def get_date(self):
        for idx in range(self.sheet_data.nrows):
            row_data = self.sheet_data.row_values(idx)
            date_str = ''.join(row_data)
            date_str = ''.join(date_str.split())
            date_str = date_str.replace('/', '-')
            if self.date_tag in date_str:
                start_date = date_str[5:15]
                end_date = date_str[16:26]
                return start_date, end_date


if __name__ == "__main__":
    file_name = '/Users/liuyang/Downloads/员工刷卡记录表-yijingfeng(1)(1).xls'
    # idx, cnt = IndexToolsA(file_name).get_row_index()
    IndexToolsA(file_name).get_date()

