from flask_migrate import MigrateCommand
from flask_script import Manager
from app import create_app

app = create_app()

manager = Manager(app)
# manager是Flask-Script的实例，这条语句在flask-Script中添加一个db命令
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()
   # app.run(host='127.0.0.1', port=2000, debug=True)