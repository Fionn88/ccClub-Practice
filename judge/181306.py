"""
合併串列
描述

給定兩個依照數字大小排序的串列，將其合併，並依照數字大小排序。


輸入
輸入有兩行，分別包含 n, m 個整數（n, m>=0），整數之間以空白為間隔


輸出
輸出為一行，包含 n 個整數（n>=0），整數之間以空白為間隔


輸入範例 1
1 3 5 7
2 4 6 8

輸出範例 1
1 2 3 4 5 6 7 8

輸入範例 2

2 4

輸出範例 2
2 4

來源
ccClub Judge
"""
s = []
while True:
  try:
    s.extend(list(map(int,input().split())))
  except:
    break
s.sort()
print(' '.join(map(str,s)))
