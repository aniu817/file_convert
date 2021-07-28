#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/7/26 15:44
# @Author : liu yang
# @Desc: 读取 sheet 内容
import xlrd


class SheetReader:

    @staticmethod
    def get_sheet(file,
                  sheet_name='员工刷卡记录表'):
        work_book = xlrd.open_workbook(file)
        data = work_book.sheet_by_name(sheet_name)
        return data


if __name__ == "__main__":
    file_name = '/Users/liuyang/Downloads/员工刷卡记录表（彩云城体验中心）.xls'
    SheetReader.get_sheet(file_name)
