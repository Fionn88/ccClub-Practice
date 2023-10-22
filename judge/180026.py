"""
10-1：階乘
描述

我們在課程中介紹過階乘，0! = 1，1! =1，n! = n*(n-1)!，輸入 n ，請輸出 n! 的值。


輸入
輸入有一行，包含一個正整數n


輸出
請輸出一個整數，值為n!


輸入範例 1 
2

輸出範例 1
2

輸入範例 2 
5

輸出範例 2
120

來源
ccClub Judge
"""

n = int(input())
j = 1
if n == 0:
  print(1)
else:
  for i in range(1,n+1):
    j *= i
  print(j)
  