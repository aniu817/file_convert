#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/7/9 10:15
# @Author : liu yang
# @Desc: 返回行索引


import xlrd


class IndexHelper:
    def __init__(self,
                 file_name,
                 sheet_name='员工刷卡记录表',
                 row_tag='工号',
                 row_list=[]):
        self.file_name = file_name
        self.sheet_name = sheet_name
        self.row_tag = row_tag
        self.row_list = row_list

    def get_row_index(self):
        self._get_sheet()
        for idx in range(self.data.nrows):
            row_data = self.data.row_values(idx)
            for value in row_data:
                if self.row_tag in str(value):
                    self.row_list.append(idx)
        print(self.row_list)
        return self.row_list

    def _get_sheet(self):
        work_book = xlrd.open_workbook(self.file_name)
        self.data = work_book.sheet_by_name(self.sheet_name)
        return self.data

    def get_row_count(self):
        self.get_row_index()
        diff = [self.row_list[idx + 1] - self.row_list[idx] for idx in range(len(self.row_list) - 1)]
        last_row_count = (self.data.nrows + 1) - self.row_list[-1]
        diff.append(last_row_count)
        print(diff)


if __name__ == "__main__":
    IndexHelper('/Users/liuyang/Downloads/test.xls').get_row_index()
    IndexHelper('/Users/liuyang/Downloads/test.xls').get_row_count()
