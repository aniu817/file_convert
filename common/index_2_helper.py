#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/7/18 09:17
# @Author : liu yang
# @Desc: 返回行索引


import xlrd


class IndexHelper:
    def __init__(self,
                 file_name,
                 sheet_name='刷卡记录',
                 row_tag='工 号',
                 row_list=[]):
        self.file_name = file_name
        self.sheet_name = sheet_name
        self.row_tag = row_tag
        self.row_list = row_list
        self._get_sheet()

    def get_row_index(self):
        """
        :return:读取每组数据跳过的行数
        """
        # self._get_sheet()
        for idx in range(self.data.nrows):
            row_data = self.data.row_values(idx)
            for value in row_data:
                if self.row_tag in str(value):
                    self.row_list.append(idx)
        # print(self.row_list)
        return self.row_list

    def _get_sheet(self):
        work_book = xlrd.open_workbook(self.file_name)
        self.data = work_book.sheet_by_name(self.sheet_name)
        # return self.data

    def get_row_count(self, row_list):
        """
        :return:每组数据的行数
        """
        diff = [row_list[idx + 1] - row_list[idx] for idx in range(len(row_list) - 1)]
        last_row_count = (self.data.nrows + 1) - row_list[-1]
        diff.append(last_row_count)
        return diff


if __name__ == "__main__":
    row_index = IndexHelper('/Users/liuyang/Downloads/2.xls').get_row_index()
    IndexHelper('/Users/liuyang/Downloads/2.xls').get_row_count(row_index)
