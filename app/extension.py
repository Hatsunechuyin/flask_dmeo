from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

db = SQLAlchemy()
migrate = Migrate(db=db)

def register(app):
    db.init_app(app)
    migrate.init_app(app)
    # manager = Manager(app)
    # # 第一个参数是flask实例，第二个参数SQLAlchemy实例
    # Migrate(app, db)
    # # manager是Flask-Script的实例，这条语句在flask-Script中添加一个db命令
    # manager.add_command("db", MigrateCommand)

