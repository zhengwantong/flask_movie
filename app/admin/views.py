# encoding: utf-8
# 调用蓝图对象
from . import admin


@admin.route('/')
def index():
    return '<h1 style="color:red">this is admin</h1>'
