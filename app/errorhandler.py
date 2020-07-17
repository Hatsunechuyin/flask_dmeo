# from app.error.error_code import ErrorCode
# from app.error import error
from app.utils.response import ResponseFormat

import traceback


def service_error(err):
    print(traceback.format_exc())
    return err.error_response().to_json()
    # return ResponseFormat(500).set_error_message("服务器异常").to_json()


def exception(err):
    print(traceback.format_exc())
    return ResponseFormat(500).set_error_message("服务器内部错误").to_json()


def error_500(err):
    print(traceback.format_exc())
    # return error.ServerInternalError().error_response().to_json()
    return ResponseFormat(500).set_error_message("服务器异常").to_json()


def error_404(err):
    return ResponseFormat(404).set_error_message("路由不存在").to_json()


def register(app):
    """
    注册错误处理
    """
    app.errorhandler(505)(service_error)
    app.errorhandler(Exception)(exception)
    app.errorhandler(500)(error_500)
    app.errorhandler(404)(error_404)
