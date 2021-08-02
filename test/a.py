#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/7/29 08:45
# @Author : liu yang
# @Desc: 测试


import threading
import time
from flask import Flask
import pandas as pd

app = Flask(__name__)

count = 0


@app.route('/test')
def hello_world():
    global count

    count += 1
    if count % 2 == 1:
        print(threading.currentThread().ident, 'sleep 10')
        time.sleep(10)
    else:
        print(threading.currentThread().ident, 'sleep 5')
        time.sleep(5)

    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
