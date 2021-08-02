#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/7/27 17:00
# @Author : liu yang
# @Desc: 正式环境入口
import datetime
import os

from common.path_helper import PathHelper
from main.entry_a import EntryA


class Main:
    def __init__(self, dirs):
        self.dirs = dirs

    def run(self):
        for root, dirs, files in os.walk(self.dirs):
            for file in files:
                file_name = root + '/' + file
                # print(os.path.basename(file_name))
                print(file_name)
                if 'DS' in file_name:
                    continue
                EntryA(file_name).run()


if __name__ == "__main__":
    file_path = PathHelper.get_package_dir('file')
    today = datetime.date.today().strftime('%Y-%m-%d')
    dirs = file_path + '/' + today + '/a'
    PathHelper.dir_make(dirs)
    Main(dirs).run()


