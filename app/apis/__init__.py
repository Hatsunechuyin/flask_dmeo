from flask import Blueprint

apis = Blueprint('apis', '__name__')

# 路由列表
def route():
    import app.apis.auth

# 路由注册
def register(app):
    route()
    app.register_blueprint(apis, url_prefix='/apis')
