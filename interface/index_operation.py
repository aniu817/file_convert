#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/7/26 15:19
# @Author : liu yang
# @Desc: 返回基本信息、数据行索引


from abc import ABCMeta, abstractmethod


class IndexOperation(metaclass=ABCMeta):

    @abstractmethod
    def get_row_index(self):
        pass

    # @abstractmethod
    # def get_row_count(self, row_list):
    #     pass

    @abstractmethod
    def get_date(self):
        pass

