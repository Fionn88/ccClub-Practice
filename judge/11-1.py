"""
11-1：平方字典

描述
給定一個整數 n ，請利用字典，印出小於等於n的數字以及他的平方。

輸入
輸入為一行，包含一個整數n

輸出
輸出為n行，每行包含一個數字以及他的平方數

輸入範例 1 
3

輸出範例 1
1 1
2 4
3 9

輸入範例 2 
2

輸出範例 2
1 1
2 4

來源
ccClub Judge
"""

n = int(input())
for i in range(1,n+1):
  print(i,i*i)
  