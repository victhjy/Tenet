#encoding=utf-8
from flask import Flask
from flask_restful import Resource, Api
import app
from app.detail import Detail

app = Flask(__name__)
api = Api(app)

class HelloWorldResource(Resource):
    def get(self):
        return {
          'hello': '中文,这波啊，这波是肉蛋葱鸡',
          "asd": "aeiou aiueo",
          "中文key":"nihakkkk"
        }

    def post(self):
        return {'msg': 'post hello world'}

api.add_resource(HelloWorldResource, '/')
api.add_resource(Detail,'/detail')
# 此处启动对于1.0之后的Flask可有可无
if __name__ == '__main__':
    app.run(debug=True)