# encoding: utf-8

# 调用蓝图对象：
from . import home


@home.route('/')
def index():
    return '<h1 style="color:green">this is home</h1>'
