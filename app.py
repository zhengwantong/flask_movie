# encoding: utf-8

# 注册蓝图对象
from flask import Flask

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app = Flask(__name__)
app.debug = True


app.register_blueprint(home_blueprint)
# 并为admin设置了url前缀"/admin"
app.register_blueprint(admin_blueprint, url_prefix="/admin")