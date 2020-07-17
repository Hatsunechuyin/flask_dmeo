from flask import jsonify

# from app.error.error_code import ErrorCode

class ResponseFormat:

    def __init__(self, error_code=200):
        """
        创建一个响应
        """
        self.error_code = error_code
        self.error_message = None
        self.data = None

        self.status_code = 200
        self.headers = None

    @staticmethod
    def ok():
        """
        返回一个响应
        """
        return ResponseFormat()

    def set_status_code(self, status_code):
        """
        设置状态码
        """
        self.status_code = status_code
        return self

    def set_error_code(self, error_code):
        """
        设置错误代码
        """
        self.error_code = error_code
        return self

    def set_error_message(self, error_message):
        """
        设置错误消息
        """
        self.error_message = error_message
        return self

    def set_data(self, data):
        """
        设置返回数据
        """
        self.data = data
        return self

    def set_headers(self, headers):
        """
        设置响应头
        """
        self.headers = headers
        return self

    def to_json(self):
        return jsonify({
            "error_code": self.error_code,
            "error_message": self.error_message,
            "data": self.data,
        }), self.status_code, self.headers
