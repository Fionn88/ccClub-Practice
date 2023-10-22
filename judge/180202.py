"""
冠亞軍分數差
描述

給定若干個數，找出最大值和次大值的差。


輸入
輸入有一行，包含數個數字，數字間以空格分開。


輸出
輸出最大值和次大值的差。


輸入範例 1 
1 3 5 7 9

輸出範例 1
2

輸入範例 2 
-1 1

輸出範例 2
2

來源
ccClub Judge
"""

s = list(map(int,input().split()))
sortS = sorted(s)
print(abs(sortS[-1]-sortS[-2]))
