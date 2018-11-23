# !/usr/bin/env python
# -*- coding:utf-8 -*-

import time

from celery import Celery


import time
from celery_app import app


@app.task
def multiply(x, y):
    print 'enter call func...'
    time.sleep(4)
    return x * y