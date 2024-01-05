"""
中位數 II

描述
給定數個整數（並未依照大小排序），請輸出這個數列的中位數（請輸出浮點數）

輸入
輸入為一行，包含數個整數，以空白作為間隔

輸出
輸出為一行，包含一個浮點數

輸入範例 1 
2 20 18 16 9 5

輸出範例 1
12.5

輸入範例 2 
7 11 1 6 20 1 20 18 14 20 10 15 6 4 6

輸出範例 2
10.0

來源
ccClub Judge
"""

n = list(map(int,input().split()))
n.sort()
length = len(n)
index = int(length / 2)
if length % 2 == 0:
    print((n[index-1] + n[index])/2)
else:
    print(float(n[index]))
