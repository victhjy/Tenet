#encoding=utf-8
import sys
import json

def hpdataParse():
  with open(u'./source/weeklyreport/1028.json', 'r') as f:
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
    # testItem = dataList[0]
    # for key in testItem:
    #   testMatrixItem = testItem[key]
    #   if len(testMatrixItem.keys()) == 0:
    #     # print("null key "+key)
    #     pass
    for i in range(len(dataList)):
      dsString = ''
      dsItem = dataList[i]
      for j in range(len(defaultKeys)):
        matrixItem = dsItem[defaultKeys[j]]
        keyValue = matrixItem["value"]
        dsString = dsString+'*'+keyValue
      print(dsString)  
def main(argv):
    hpdataParse()
if __name__ == '__main__':
  main(sys.argv)