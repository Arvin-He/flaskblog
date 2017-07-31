from flask import Blueprint
# 通过实例化一个 Blueprint 类对象可以创建蓝本。
# 这个构造函数有两个必须指定的参数：蓝本的名字和蓝本所在的包或模块
main = Blueprint('main', __name__)

# 注意，这些模块在 app/main/__init__.py 脚本的末尾导入，
# 这是为了避免循环导入依赖，因为在views.py 和 errors.py 中还要导入蓝本 main 。
from . import views, errors
