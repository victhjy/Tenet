#encoding=utf-8

from linknode import linknode
from nodebean import nodebean
from parseTags import main
import sys
import time


def sliptList(a, lo, hi):
  i = lo
  j = hi
  t = a[i]
  while i < j:
    while i < j and a[j] > t:
      j -= 1
    if i < j:
      a[i] = a[j]
      i += 1
    
    while i < j and a[i] < t:
      i += 1
    if i < j:
      a[j] = a[i]
      j -= 1
  a[i] = t
  return i
def quickSortIter(test, lo, hi):
  if lo >= hi:
    return
  mid = sliptList(test, lo, hi)
  print(test)
  quickSortIter(test, lo, mid - 1)
  quickSortIter(test, mid + 1, hi)
  

def quickSort(test):
  quickSortIter(test, 0, len(test)-1)



def quickSortIterForKth(test, lo, hi, k):
  if lo >= hi:
    return
  mid = sliptList(test, lo, hi)
  if mid < k:
      return quickSortIterForKth(test, mid + 1, hi, k)
  elif mid > k:
      return quickSortIterForKth(test, lo, mid - 1, k)
  else:
      return test[mid]

def findKth(nums,k):
  if k > len(nums):
    return -1
  return quickSortIterForKth(nums,0, len(nums) - 1, k-1)



def popSort(test):
  count = 0
  for i in range(len(test)):
    for j in range(i + 1,len(test)):
      if test[i] >= test[j]:
        t = test[i]
        test[i] = test[j]
        test[j] = t
        count = count + 1
    print(test)
  print('次数',count)

def selectSort(test):
  count = 0
  for i in range(len(test)):
    min = test[i]
    for j in range(i + 1,len(test)):
      if min >= test[j]:
        temp = min
        min = test[j]
        test[j] = temp
        count = count + 1
    print(test)
    test[i] = min
  print('次数',count)

def longestStr(strrr):
  print(strrr)
  start = 0
  result = 0
  midmap = {}

  targetS = 0
  for index in range(len(strrr)):
    cur = strrr[index]
    if cur in midmap:
      start = max(start, midmap[cur])
    if result <= index - start + 1:
      result = index - start + 1
      targetS = start
    midmap[cur] = index + 1
  print(result)
  print(strrr[targetS:targetS+result])

def myLongstSubString(s):
  print('origin string ', s)
  l = total = 0
  r = 0
  tempMap = {}
  while r < len(s):
    if s[r] in tempMap:
      l = tempMap[s[r]] + 1
      tempMap[s[r]] = r
      total = max(total, r - 1)
      print('mid 1 total ', total , l, r)
    else:
      tempMap[s[r]] = r
      total = max(total, r - l + 1)
      print('mid 2 total ', total , l, r)
    r += 1
  print('max substring ', total)

fibmap = {}
def fib(tar):
  if tar <= 0:
    return 0
  if tar == 1 or tar == 2:
    return 1
  else:
    # 单次，省空间
    cur = 1
    pre = 1
    for i in range(3,tar+1,1):
      sum = cur + pre
      pre = cur
      cur = sum
    return cur
    # 备忘录类型
    if tar in fibmap:
      return fibmap[tar]
    a = fib(tar-1) + fib(tar - 2)
    fibmap[tar] = a
    return a

def coinsToAmount(coins, amount):
  midmap = {}
  def dp(n):
    if n <= 0:
      return 0 
    res = 999
    targetCoin = 0
    for coin in coins:
      tempKey = n-coin
      tempValue = 0
      if tempKey in midmap:
        tempValue = midmap[tempKey]
      else:
        tempValue = dp(tempKey)
        midmap[tempKey] = tempValue
      if res >= tempValue + 1:
        res = tempValue + 1
        targetCoin = coin
      # res = min(res, tempValue + 1)
    print(targetCoin)
    return res
  return dp(amount)

def switch0To0(matrix):
  row0Has0 = False
  col0Has0 = False
  for i in range(len(matrix)):
    if matrix[i][0] == 0:
      col0Has0 = True
    if i == 0:
      for j in range(len(matrix[i])):
        if matrix[0][j] == 0:
          row0Has0 = True
  print('row0Has0: ',row0Has0, 'col0Has0: ',col0Has0)
  for i in range(1, len(matrix), 1):
    for j in range(1, len(matrix[i]), 1):
      print('before condition', i, j)
      if matrix[i][j] == 0:
        matrix[0][j] = 0
        matrix[i][0] = 0
        print('value 0', i, j)
  
  print('flags row0',matrix[0])
  tempresult = []
  for a in matrix:
    tempresult.append(a[0])
  print('flags col0',tempresult)

  for i in range(0, len(matrix), 1):
    if i == 0:
      for subi in range(1,len(matrix[1]),1):
        if matrix[0][subi] == 0:
          for sssubi in range(1, len(matrix), 1):
            matrix[sssubi][subi] = 0
    else:
      if matrix[i][0] == 0:
        for subi in range(len(matrix[i])):
         matrix[i][subi] = 0
  if row0Has0:
    for i in range(len(matrix[0])):
      matrix[0][i] = 0
  if col0Has0:
    for i in range(len(matrix)):
      matrix[i][0] = 0
  printMatrix(matrix)

          
      
def printMatrix(matrix):
  print('start print matrix')
  for i in range(len(matrix)):
    print(matrix[i])
  print('end print matrix')



def maxHuiWen(originS):
  
  maxStart = 0
  maxLength = 0
  def getMaxHuiWen(str,i, startI, startJ):
    innerMaxStart = 0
    innerMaxLenth = 0
    while startI >= 0 and startJ <= len(str)-1:
      if str[startI] == str[startJ]:
        if startJ - startI + 1 >= innerMaxLenth:
          innerMaxLenth =  startJ - startI + 1
          innerMaxStart = startI
      else:
        break
      startI = startI - 1
      startJ = startJ + 1
    return (innerMaxStart, innerMaxLenth)

  for i in range(len(originS)):
    result = getMaxHuiWen(originS, i, i-1, i+1)
    if result[1] > maxLength:
      maxLength = result[1]
      maxStart = result[0]
    result1 = getMaxHuiWen(originS, i, i-1, i)
    if result1[1] > maxLength:
      maxLength = result1[1]
      maxStart = result1[0]
  print('origin huiwen: ', originS)
  print('huiwen result: ',originS[maxStart: maxStart + maxLength])
  # print('huiwen result: ', maxStart, maxLength)

  # for index in range(len(originS)):
  #   maxLoop = max(index, len(originS) - index)
  #   for i in range(maxLoop):
  #     left = index - 1 - i
  #     right = index + 1 + i
  #     if left >= 0 and right <= len(originS) - 1:
  #       if originS[left] == originS[right]:
  #         if maxResult1 < right - left + 1:
  #           maxResult1 = right - left + 1
  #           print('huiwen max A  ', index, originS[index], maxResult1)
  #         continue
  #       else:
  #         break
  # maxResult2 = 0
  # for index in range(len(originS)):
  #   maxLoop = max(index, len(originS) - index)
  #   maxVal = maxResult2
  #   for i in range(maxLoop):
  #     left = index - i
  #     right = index + 1 + i
  #     if left >= 0 and right <= len(originS) - 1:
  #       if originS[left] == originS[right]:
  #         if maxResult1 < right - left + 1:
  #           maxResult1 = right - left + 1
  #           print('huiwen max B  ', index, originS[index], maxResult1)
  #         continue
  #       else:
  #         break
          
  # print('max huiwen input: ', originS, ' result: ',max(maxResult1, maxResult2))


def stockNoFee(stockPriceList, k):
  print(stockPriceList, k)
  if len(stockPriceList) < 2:
    return 0
  maxProfile = 0
  minBuy = stockPriceList[0]
  for price in stockPriceList:
    if price > minBuy:
      maxProfile = max(maxProfile, price - minBuy)
    else:
      minBuy = min(minBuy, price)
  print('max profile: ',maxProfile)

def islandDps(islandMatrix, row, column):
  if row >= 0 and column >= 0 and len(islandMatrix) - 1 >= row and len(islandMatrix[0]) - 1 >= column and islandMatrix[row][column] == 1:
    islandMatrix[row][column] = 0
    islandDps(islandMatrix, row -1, column)
    islandDps(islandMatrix, row +1, column)
    islandDps(islandMatrix, row, column - 1)
    islandDps(islandMatrix, row, column + 1)

def downIsland(islandMatrix):
  count = 0
  rowCount = len(islandMatrix)
  colCount = len(islandMatrix[0])

  printMatrix(islandMatrix)
  for i in range(rowCount):
    for j in range(colCount):
      if islandMatrix[i][j] == 1:
        count = count + 1
        islandDps(islandMatrix, i,j)
      else:
        continue
  print("island count ", count)

def allSort(originList):
  if originList == None:
    return
  dpsSort(originList, 0, len(originList))
  print("origin string", originList)

def dpsSort(arr, position, end):
  if position == end:
    print(arr)
  else:
    for index in range(position, end):
      arr[index], arr[position] = arr[position], arr[index]
      dpsSort(arr, position + 1, end)
      arr[index], arr[position] = arr[position], arr[index]
      print('midd p ', position,'  ',arr)
    
def worksKuoHao(demoString):
  print('kuohao: ', demoString)
  if len(demoString) < 1:
    return False
  temp = {
    '{':'}',
    '[':']',
    '(':')'
  }
  cur = []
  for i in demoString:
    if i in temp:
      cur.append(temp[i])
    else:
      if len(cur) > 0 and cur[-1] == i:
        cur.pop()
        continue
      else:
        return False
  if len(cur) == 0:
    return True
  return False
def findOnlyOne(originList):
  print('findOnlyOne: ', originList)
  print('result: ', iterOnlyOne(originList))

def iterOnlyOne(originList):
  if len(originList) == 1:
    return originList[0]
  else:
   a = originList[0]
   originList.pop(0)
   if a in originList:
     originList.remove(a)
     return iterOnlyOne(originList)
   else:
     return a

def printLinknode(linkNode):
  result = str(linkNode.val)
  while linkNode.next:
    linkNode = linkNode.next
    result = result+' -> '
    result = result + str(linkNode.val)
  print('linknode: ', result)
# 层次遍历（广度优先）
def BFS(root):
    if root:
        res = []
        queue = [root]
        while queue:
            currentNode = queue.pop(0)
            res.append(currentNode.val)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
    return res

def myBfs(root):
  if root:
    res = []
    queue = [root]
    while len(queue) > 0:
      cur = queue.pop(0)
      res.append(cur.val)
      if cur.left:
        queue.append(cur.left)
      if cur.right:
        queue.append(cur.right)
  return res

# 深度优先
def DFS(root):
    if root:
        res = []
        stack = [root]
        while stack:
            currentNode = stack.pop()
            res.append(currentNode.val)
            if currentNode.right:
                stack.append(currentNode.right)
            if currentNode.left:
                stack.append(currentNode.left)
    return res
def myDfs(root):
  if root:
    res = []
    stack = [root]
    while len(stack) > 0:
      cur = stack.pop()
      res.append(cur.val)
      if cur.right:
        stack.append(cur.right)
      if cur.left:
        stack.append(cur.left)
    return res
def minSumThanTarget(sourceList, target):
  l = total = 0
  ans = len(sourceList) + 1
  for r in range(len(sourceList)):
    total += sourceList[r]
    while total >= target:
      ans = min(ans, r-l+1)
      total -= sourceList[l]
      l += 1
  return 0 if ans == len(sourceList) + 1 else ans

def reverseLink(link):
  if link.next == None:
    return link
  else:
    last = reverseLink(link.next)
    link.next.next = link
    link.next = None
    printLinknode(last)
    return last

def aimStrInSourceStr(aimStr, sourceStr):
  print('aimStrInSourceStr ',aimStr, ' ', sourceStr)
  if len(aimStr) > len(sourceStr):
    return -1
  map2 = {}
  for s in aimStr:
        if s in map2:
          map2[s] += 1
        else:
          map2[s] = 1
  def sameStr(str1):
    if str1:
      map1 = {}
      for s in str1:
        if s in map1:
          map1[s] += 1
        else:
          map1[s] = 1
      
      if len(map1) == len(map2):
        allSame = True
        for (i, j) in map1.items():
          # print(i,j)
          if i in map2 and map2[i] == j:
            continue
          else:
            allSame = False
            break
        return allSame
      else:
        return False
  i = 0
  res = -1
  while i + len(aimStr) <= len(sourceStr):
    str1 = sourceStr[i:i+4:1]
    print('str idx', str1, i)
    if  sameStr(str1):
      res = i
      break
    else:
      i += 1
    print(str1)
  return res
def jumpFloor( number):
  # write code here
  if number == 1:
      return 1
  if number == 2:
      return 2
  v1 = 1
  v2 = 2
  for i in range(3,number + 1):
      v2 = v1 + v2
      v1 = v2 - v1
  return v2
# 两数之和
def twoSum(numbers , target ):
  # write code here
  map = {}
  for i in range(len(numbers)):
      v = numbers[i]
      subTarget = target - v
      if subTarget in map:
          return [map[subTarget], i]
      else:
          map[v] = i
  return []

  # BFS 
def levelOrder(self , root ):
  # write code here
  if root == None:
      return []
  arr = [root]
  res = []
  while len(arr) > 0:
      count = len(arr)
      subRes = []
      for i in range(count):
          subRoot = arr[i]
          subRes.append(subRoot.val)
          if subRoot.left != None:
              arr.append(subRoot.left)
          if subRoot.right != None:
              arr.append(subRoot.right)
      res.append(subRes)
  return res

def maxLength(arr):
  map = {}
  maxVal = 0
  start = 0
  end = 0
  while end < len(arr):
    c = arr[end]
    if c in map.keys():
      start = map[c] + 1
    else:
      maxVal = max(maxVal, end - start + 1)
    map[c] = end
    end += 1
  return maxVal

def reversePrint():
  a = [x for x in range(5)]
  for i in a[::-1]:
    print(i)

def reversePrint():
  for i in range(5-1,-1,-1):
    print(i)


def cycle10NStep(k):
  # n 为 10
  res = 0
  if k % 2 == 1:
    return 0
  #  dp[i][j]  i 步 到 j 点的方法数量   dp[i][j] = dp[i-1][(j-1+n)%n] + dp[i-1][(j+1)%n]
  dp = [[0]*10] * (k+1)
  a = dp[1]
  a[0] = 1
  # for j in range(1, k+1, 1):
  #   for i in range(10):
  #     print("j, i: ", j, i, " === ", j-1,(i-1+10)%10," +++ ", j-1, (i+1)%10)
  #     dp[j][i] = dp[j-1][(i-1+10)%10] + dp[j-1][(i+1)%10]
  #     print("val: ", dp[j][i])
  print(dp)
  return res

def frogFloor(n):
  dp = [0]*(n+1)
  dp[0] = 0
  dp[1] = 1
  dp[2] = 2
  for i in range(3,n+1):
    dp[i] = dp[i-1] + dp[i - 2]
  print(dp)
  print(dp[n])

def gatherMoney(moneys, target):
  dp = [sys.maxsize]* (target+1)
  for i in range(target+1):
    if i == 0:
      dp[i] = 0
    minVal = sys.maxsize
    for subI in moneys:
      if i - subI >= 0 :
        minVal = min(minVal, dp[i - subI] + 1)
    if minVal != sys.maxsize:
      dp[i] = minVal
      
  
  print(dp)
  dps = []
  for i in range(len(dp)):
    dps.append(i)
  print(dps)

def bigNumAdd(a,b):
  print(a,' + ', b)
  c = max(len(a), len(b))
  while c != len(a) or c != len(b):
    if c != len(a):
      a = '0' + a
    else:
      b = '0' + b
  c = 0
  carry = 0
  res = []
  while c < len(a):
    sum = carry + int(a[0 - c - 1]) + int(b[0 - c - 1])
    if sum >= 9:
      carry = 1
    else:
      carry = 0
    res.insert(0, sum%10)
    c += 1
  if carry == 1:
    res.insert(0, 1)
  while len(res) > 0 and res[0] == 0:
    res = res[1:]
  print("".join([str(x) for x in res]))

def mySqrt(num, step):
  if num < 0:
    print('error result', -1)
  r = num
  l = 0
  m = l + (r-l)/2
  while abs(m*m - num) > step:
    if m*m > num:
      r = m
    else:
      l = m 
    m = l + (r-l)/2
    print("l, m, r", l, m, r)
  print('result: ', m, m*m)



def sortListNode(head):
  listQuickSort(head, None)
  return head

def listQuickSort(head, end):
  if head != end:
    midNode = listSortSpart(head)
    listQuickSort(head, midNode)
    listQuickSort(midNode.next, end)

def listSortSpart(head):
  slow = head
  fast = head.next
  while fast != None:
    if fast.val < head.val:
      slow = slow.next
      temp = slow.val
      slow.val = fast.val
      fast.val = temp
    fast = fast.next
  temp = slow.val
  slow.val = head.val
  head.val = temp
  return slow

def main(argv):
  test = [28,7,4,3,5,7,6,1,56,43,51,34,15,56,40,9,10,1,0,99,2,4]
  test1 = [4,5,23,12,6,1,9,8,0,24,2]
  start =time.process_time()



  # str = "www.baidu.com"
  # strArr = list(str)
  # str1 = ''.join(strArr)
  # strArr2 = str.split('.')
  # print(str1, strArr2)

  
  l1 = linknode(4)
  l2 = linknode(1)
  l3 = linknode(0)
  l4 = linknode(3)
  l1.next = l2
  l2.next = l3
  l3.next = l4
  printLinknode(l1)
  sortListNode(l1)
  printLinknode(l1)





  # bigNumAdd('1234','000045')

  # mySqrt(7, 0.00000001)
  # frogFloor(20)

  # gatherMoney([2,5], 20)

  # 圆环10个点，n步回到0点的走法 todo
  # cycle10NStep(4)

  # print()
  # reversePrint()
  # print(jumpFloor(4))
  # print(twoSum([2,3,4,6,7], 7))
  # print(maxLength([111123123,213131232,3341341,2123123123,1231233131,12313123,123123123,123123123,12312312312]))
  # print(test1)

  # 快排
  # print(test1)
  # quickSort(test1)
  # print ('quick sort', test1)

  # 第K大
  # print(test1)
  # print("test1 2th: ", findKth(test1, 2))


  # popSort(test)
  # print ('popSort sort')

  # selectSort(test)
  # print ('select sort')
  # 最长子串
  # myLongstSubString('abb')
  # longestStr('11223456413')
  # print(fib(20))

  # print('coins', coinsToAmount([1,2,5], 22))
  
  # matrix = [
  #   [0,1,1,1,1,1],
  #   [1,1,1,1,1,1],
  #   [1,1,1,1,1,1],
  #   [1,1,1,1,1,1],
  #   [1,1,1,0,1,1],
  #   [1,1,1,1,1,0],
  # ]
  # printMatrix(matrix)
  # print(switch0To0(matrix))

  # maxHuiWen('18681018610110')
# 沉没岛屿  最大岛屿数量
  # downIsland([
  #   [1,1,1,0,0,0,1],
  #   [1,1,1,0,0,0,1],
  #   [0,0,0,0,0,1,1],
  #   [1,0,1,0,0,0,1]
  # ])

  # 股票交易 一次
  # stockNoFee([4,9,1,7,5,9,3,12,68,3,2,5], 1)
  # print(aimStrInSourceStr('aace','aa1dcssecaa'))
  # allSort([1,2,3,4])
  # print(worksKuoHao('({[[][]]})'))
  # findOnlyOne([1,2,33,3,4,5,4,3,2,1,5])

# DFS深度   BFS广度
  # nodeArr = [1,3,4,6,None,3,None,2]
  # generateNode(nodeArr)
  # node1 = nodebean(1,None,None)
  # node2 = nodebean(2,None,None)
  # node3 = nodebean(11,node1,None)
  # root = nodebean(3,node3,node2)
  # print(root)
  # print(myDfs(root))
  # print(myBfs(root))

# 滑动窗口
  # print(minSumThanTarget([1,2,3,1],4))
  # print(myMinSumThanTarget([1,2,3,4,5],5))
  # 打印链表
  # link3 = linknode(3,None)
  # link2 = linknode(2, link3)
  # link1 = linknode(1,link2)
  # printLinknode(link1)
  # printLinknode(reverseLink(link1))
  end = time.process_time()
  print('Running time: %s Seconds'%(end-start))

def myMinSumThanTarget(nums, target):
  l = total = 0
  res = len(nums) + 1
  for r in range(len(nums)):
    total += nums[r]
    while total >= target:
      res = min(res, r - l + 1)
      total -= nums[l]
      l += 1
  if res == len(nums) + 1:
    return 0
  else:
    return res

def generateNode(arr):
  print('generate node ', arr)
  
  # return
  # def curNode(node, val):
  #   if val:
  #     node.val = val
  #     return node
  # for i in arr:
  #   if i:
      
if __name__ == '__main__':
  main(sys.argv)
