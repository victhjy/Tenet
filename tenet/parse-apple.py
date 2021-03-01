#encoding=utf-8
import sys
import json

def appleParse():
  with open(u'./source/apple-appid.json', 'r') as f:
    dict = json.load(fp=f)
    dataList = dict["data"]
    for i in range(len(dataList)):
      obj = dataList[i]["attributes"]
      # print(obj)
      print(obj["email"],'*',obj["firstName"],obj["lastName"],'*',obj["roles"])
def main(argv):
    appleParse()
if __name__ == '__main__':
  main(sys.argv)