#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/7/14 14:30
# @Author : liu yang
# @Desc: 文件上传后端接口


# coding:utf-8
import datetime
import time

from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from common.path_helper import PathHelper
import pypinyin

from main.entry_a import EntryA
import pandas as pd

app = Flask(__name__)


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        start = time.time()
        file = request.files['file']
        if file is None:
            # 表示没有发送文件
            return "未上传文件"

        file_path = PathHelper.get_package_dir('upload_path')
        today = datetime.date.today().strftime('%Y-%m-%d')
        dirs = file_path + '/' + today + '/a'

        if not os.path.exists(dirs):
            os.makedirs(dirs)

        file_name = file.filename
        full_path = dirs + '/' + file_name
        try:
            file.save(full_path)
            print('保存成功')
        except:
            return '文件上传失败'

        try:
            EntryA(full_path).run()
            print('转换成功')
        except:
            return '转换失败，请确认格式...'

        end = time.time()
        start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print('开始时间：' + start_time)
        print("完成时间: %f s" % (end - start))

        return '完成转换'


if __name__ == '__main__':
    # app.run()
    app.run(host='0.0.0.0')
