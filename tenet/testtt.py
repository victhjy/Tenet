#encoding=utf-8
import sys
import cmd
import os 
import io
import re
import codecs
import string
import math
import numbers
import random
import json

def string2Dic():
  f = open("./utdid.txt")
#   lines = f.readlines()
#   print (lines)
  resultString = ''
  line = f.readline()
  while line:
      line = line.replace("\n","")
      # print ("%s;" %(line))

      resultString = resultString + line + ';'
      line = f.readline()
  f.close()
  print ("%s" %(resultString))

def domain2Orange():
  f = open("./imagedomain.txt")
  line = f.readline()
  resultString = ""
  while line:
      line = line.replace("\n","")
      resultString = resultString + "," + line
      line = f.readline()
  f.close()
  print(resultString)

def plus():
  a = input("给出数字:")
  arr = list(a)
  arr.reverse()
  addOn = 0
  for i in range(len(arr),0,-1):
    print('test',i)

  print("答案是: ","".join(arr))

def lsdSort(a,w):
  N = len(a)
  R = 256
  stringList = list(string.ascii_uppercase)
  for num in range(0,9):
    stringList.append(str(num))
  for d in range(w-1,0,-1):
    count = list(range(N))
    for i in range(0, N):
      print (a[i][d],":",ord(a[i][d]))
      # if a[i][d] in count:
      #     count[ord(a[i][d])] += 1
      # else:
      #   count[ord(a[i][d])] = 1
    for r in range(0,N):
      pass
      # count[r+1] += count[r]
    # print('result ',a,count)
      # print('a',a[i][d])
  
def formatterString():
  s = 'hello, {}, how are you?'
  print(s.format('hjy'))

def generateRandom():
  f = open("./source/randoms.txt", "w")
  # f.
  for i in range(100):
    result = '{}\n'
    result = result.format(random.randint(-25535,25535))
    result = str(result)
    f.write(result)
  f.close()

def file2Arr():
  f = open("./source/randoms.txt")
  strList = list()
  readLine = f.readline()
  while readLine:
    # print(readLine)
    strList.append(readLine)
    readLine = f.readline()
  f.close()

  for a in range(len(strList)):
    if a >= len(strList)-2:
      continue
    for b in range(a+1,len(strList)):
      if b >= len(strList)-1:
        continue
      for c in range(b+1,len(strList)):
        if int(strList[a]) + int(strList[b]) + int(strList[c]) == 0:
          print(strList[a]+strList[b]+strList[c])
        # print(a,b,c)

def avarage_aug_dau():
  f = open("./source/augdau.txt")
  allDau = list()
  readLine = f.readline()
  while readLine:
    # strList.append(readLine)
    readLine = readLine.replace("\n","")
    readLine = readLine.replace("\x08","")
    allDau.append(readLine)
    readLine = f.readline()
  f.close()
  dauCnt = 0
  for i in range(len(allDau)):
    dauCnt += int(allDau[i])
  print("avg dau", dauCnt/len(allDau))

def hpdataParse(keyField):
  with open(u'./source/20190909.json', 'r') as f:
    dict = json.load(fp=f)
    dataList = dict["data"]
    # print('ds'+ '|' + keyField)
    item = dataList[0]
    defaultKeys = [] 
    titleStr = ''
    for key in item:
      if key in ['SORT_INDEX','REVISIT7D_RATE','REVISIT1D_RATE_GR','REVISIT1D_RATE','REVISIT7D_RATE_GR']:
        continue
      titleStr = titleStr + '*' + key
      defaultKeys.append(key)
    print(titleStr)

# testcode
    testItem = dataList[0]
    for key in testItem:
      testMatrixItem = testItem[key]
      if len(testMatrixItem.keys()) == 0:
        # print("null key "+key)
        pass

    for i in range(len(dataList)):
      dsString = ''
      dsItem = dataList[i]
      for j in range(len(defaultKeys)):
        matrixItem = dsItem[defaultKeys[j]]
        keyValue = matrixItem["value"]
        dsString = dsString+'*'+keyValue
      print(dsString)  

def getimagesfromdic():
  with open(u'./source/tags/1.json', 'r') as f:
    dic = json.load(fp=f)
    for key in dic:
      parseSet(dic[key])
    
      
def parseSet(set):
  if type(set).__name__ == 'dict':
    for key in set:
      parseSet(set[key])
  elif type(set).__name__ == 'list':
    for j in range(len(set)):
      parseSet(set[j])
  elif type(set).__name__ == 'str':
    if set.endswith("png") or set.endswith("jpg") or set.endswith("jpeg") or set.endswith("webp"):
      print(set)
  else:
    # print(type(set).__name__)
    pass

def addFilterToImage():
  # 打开一个jpg图像文件，注意是当前路径:
  im = Image.open('source/img/wechat.jpeg')
  # 应用模糊滤镜:
  im2 = im.filter(ImageFilter.BLUR)
  im2.save('source/img/wechat_blur.jpg', 'jpeg')

def main(argv):
    # string2Dic()s
    # domain2Orange()
    # plus()
    # lsdSort(['AB3422X','CVSD233','9SDSDR3','1SDDDR3','ACDSDD3'],7)
    # formatterString()
    # generateRandom()
    # file2Arr()
    # avarage_aug_dau()
    # hpdataParse("DIRECT_IPV")
    # getimagesfromdic()
    # addFilterToImage()
    dealArgs("a=b,b=1,c=d,d=1")

def dealArgs(args):
  list = args.split(',')
  resultList = []
  for keyvalues in list:
    keyvalueslist = keyvalues.split('=')
    if keyvalueslist[1] == '1':
        resultList.append(keyvalueslist[0])
  print (resultList)
  return resultList

if __name__ == '__main__':
    main(sys.argv)
