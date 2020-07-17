from app.extension import db

import datetime

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.String(32), primary_key=True)

    # 手机号
    phone = db.Column(db.String(32), nullable=False, unique=True, index=True)

    # 用户名
    name = db.Column(db.String(32), nullable=False, unique=True, index=True)

    # 哈希密码
    hash_password = db.Column(db.String(32))

    # 创建时间
    ctime = db.Column(db.BigInteger, nullable=False)

    # 修改时间
    utime = db.Column(db.BigInteger, nullable=False)
