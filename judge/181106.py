"""
幾連霸
描述

給定 k 個數（k >= 1），找出這 k 個數中連續的數（遞增）最多幾次。


輸入
輸入為一行，包含數個整數，以空白為間隔


輸出
輸出為一行，包含一個數字


輸入範例 1 
1 2 3 4 5 6 7 8

輸出範例 1
8

輸入範例 2 
1 2 3 5 6 7 8

輸出範例 2
4

來源
ccClub Judge
"""

# >>>>>>>>> 相關題目： ID 180303  連續整數分堆

lst = [int(i) for i in input().split()]
j,k,re,ans = 0,0,[],[]
for i in range(len(lst)):
  k += 1
  if k == len(lst) or lst[i] + 1 != lst[k]:
    re.append(lst[j:k])
    j = k


for i in re:
  ans.append(len(i))

print(max(ans))
