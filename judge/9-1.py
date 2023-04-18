"""
9-1：數字總和排序
描述

給定一個 list ，排序規則：依照數字的每個位數總和（ex：123 的各個位數總和為 6 ），由小到大排，並且輸出。


輸入
給定一行輸入，包含數個整數，以空白為間隔，請將之轉換成一個 list


輸出
輸出為一行，包含一個內容為整數的串列


輸入範例 1 
123 221 5

輸出範例 1
[221, 5, 123]

輸入範例 2 
15 7 6

輸出範例 2
[15, 6, 7]

來源
ccClub Judge
"""
N = input().split()
ansDict = {}
for i in N:
  count = 0
  for j in i:
    count+= int(j)
  ansDict[int(i)] = count
sort_dictionary= dict(sorted(ansDict.items(), key=lambda item: item[1])) 
print(list(sort_dictionary))