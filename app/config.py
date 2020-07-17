from flask_sqlalchemy import SQLAlchemy

SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://{}:{}@{}/{}'.format('root', 'root', '127.0.0.1', 'laravel')
# 动态追踪修改设置，如未设置只会提示警告
SQLALCHEMY_TRACK_MODIFICATIONS = False
#查询时会显示原始SQL语句
SQLALCHEMY_ECHO = True
# 数据库连接池大小
SQLALCHEMY_POOL_SIZE = 10