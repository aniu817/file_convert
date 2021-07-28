#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/7/14 14:30
# @Author : liu yang
# @Desc: 文件上传后端接口


# coding:utf-8

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
        file = request.files['file']
        if file is None:
            # 表示没有发送文件
            return "未上传文件"

        file_name = file.filename
        file_content = file.read()
        pd.read_excel(file)
        EntryA(file).run()
        print(111)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
