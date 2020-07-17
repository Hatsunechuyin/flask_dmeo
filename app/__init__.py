from flask import Flask
from flask_migrate import MigrateCommand
from flask_script import Manager

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

    # 数据库迁移指令,没有的话return app即可
    manager = Manager(app)
    # manager是Flask-Script的实例，这条语句在flask-Script中添加一个db命令
    manager.add_command("db", MigrateCommand)

    return manager

