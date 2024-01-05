"""
比賽排名

描述
給定一串數字，代表賽跑的成績（秒），皆為非負整數，請根據成績進行排名。請輸出從第一名到最後一名的 index，若兩人成績相同，則 index 小的在前。

輸入
輸入為數個整數，代表賽跑所花費的秒數

輸出
輸出為數個整數，以 index 代表選手，依照秒數小到大排序

輸入範例 1 
5 3 3 1

輸出範例 1
3 1 2 0

輸入範例 2 
9 8 3 3 5 4 1 5 6 0 7 5 0 5 0

輸出範例 2
9 12 14 6 2 3 5 4 7 11 13 8 10 1 0

來源
ccClub Judge
"""

lst = [int(x) for x in input().split()]
rank = [x for x in range(len(lst))]
rank.sort(key = lambda x: lst[x])
print(*rank)
