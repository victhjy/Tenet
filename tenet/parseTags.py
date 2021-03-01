# -- coding: utf-8 --
import sys
import json

def parseTagJson(name):
  file = './source/tags/' + name + '.json'
  list = []
  with open(file, 'r') as f:
    dict = json.load(fp=f)
    dataDic = dict["datas"]

    
    for key in dataDic:
      if dataDic[key] == "1":
        list.append(key)
      # print(key)
  return list
  # pass
def appendDataFrom(text, list):
  subList = parseTagJson(text)
  for i in range(len(subList)):
    if subList[i] in list:
      pass
    else:
      list.append(subList[i])
  def parseAllJson():
    fullList = []
    appendDataFrom("1", fullList)
    appendDataFrom("2", fullList)
    appendDataFrom("3", fullList)
    appendDataFrom("4", fullList)
    appendDataFrom("5", fullList)
    appendDataFrom("6", fullList)
    appendDataFrom("7", fullList)
    appendDataFrom("8", fullList)
    print(fullList)
def parseResult():
  file = './source/tags/' + 'fulltags' + '.json'
  list = []
  with open(file, 'r') as f:
    list = json.load(fp=f)
    for i in range(len(list)):
      print(list[i])
def main(argv):
  parseResult()

if __name__ == '__main__':
  main(sys.argv)