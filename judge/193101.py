"""
數字相加
描述

將輸入的兩個數字相加起來，並輸出。


輸入
輸入有一行，包含兩個數字，數字之間用空格分開。


輸出
輸出有一行，包含一個數字，為兩個數字的和。


輸入範例 1 
8 9

輸出範例 1
17

輸入範例 2 
612 7867

輸出範例 2
8479

來源
ccClub Judge
"""
s = list(map(int,input().split()))
print(sum(s))