#encoding=utf-8
from flask_restful import Resource, Api
from flask_restful import reqparse
import time
import app


class Detail(Resource):
  def get(self):
    parser = reqparse.RequestParser()
    parser.add_argument('id',type =str)
    parser.add_argument('a',type =str)
    args = parser.parse_args()
    curDate = time.ctime()
    print(args)

    newValue = ""
    if args["a"]:
      newValue = args["a"]
    else:
      newValue = "null"
    time.sleep(5)
    return {
      "time":str(curDate),
      "input":newValue
    }
