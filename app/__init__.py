from flask import Flask

from app import apis
from app import errorhandler
from app import extension
from app import config
from app import db

def create_app():
    app = Flask(__name__)
    # 加载配置
    app.config.from_object(config)
    # 路由注册
    apis.register(app)
    # 注册全局错误处理
    errorhandler.register(app)
    # 注册数据库
    extension.register(app)
    # 引入数据库表--用于迁移用的
    db.register(app)

    return app

