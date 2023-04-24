"""
最大奇偶相差
描述

給定若干個數，找出最大奇數和最大偶數的差。


輸入
輸入有一行，包含若干個數，數字間以空格分開。


輸出
輸出有一行，包含一個數，即最大偶數和最大奇數的差。


輸入範例 1 
1 2 7 5 6 3

輸出範例 1
1

輸入範例 2 
1 100

輸出範例 2
99

來源
ccClub Judge
"""

n = list(map(int,input().split()))
maxOdd = 0
maxEven = 0
for i in n:
  if i % 2 == 0:
    if maxEven < i:
      maxEven = i
  else:
    if maxOdd < i:
      maxOdd = i

print(abs(maxEven-maxOdd))