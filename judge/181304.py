"""
連續區間
描述

給定一個由 0 和 1 組成的字串，請輸出這個字串當中一共有幾個 1 的區段。


輸入
輸入為一行，包含數個 0 和 1 。


輸出
輸出為一行，包含一個整數。


輸入範例 1 
1100001100

輸出範例 1
2

輸入範例 2 
111011011011

輸出範例 2
4

來源
ccClub Judge
"""

s = input()
flag = False
count = 0
for index,value in enumerate(s):
  if (index == 0 and value == '1') or (not flag and value == '1'):
    flag = True
    count += 1
  elif index != 0 and value == '1' and flag:
    flag = True
  else:
    flag = False
print(count)
