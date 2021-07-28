#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/7/26 18:32
# @Author : liu yang
# @Desc: 返回 sheet 表数据


from abc import ABCMeta, abstractmethod


class ExtractOperation(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def get_info():
        pass

    @staticmethod
    @abstractmethod
    def get_record():
        pass
