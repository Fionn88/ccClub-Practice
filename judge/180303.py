"""
連續整數分堆
描述

給定若干個數，請將連續遞增的整數分成同一堆並放進一個 list 中，最後將 list 內的數字輸出。


輸入
輸入有一行，包含若干個數，數字間以空格分開。


輸出
輸出有若干行，每一行包含數個分堆好的數，數字間以空格分開。


輸入範例 1 
1 2 3 5 6 7

輸出範例 1

1 2 3
5 6 7

輸入範例 2 
1

輸出範例 2
1

輸入範例 3 
3 4 2 1 2

輸出範例 3
3 4
2
1 2

輸入範例 4 
9 8 7 6 5 4 3

輸出範例 4
9
8
7
6
5
4
3

提示
sample 1 中，輸入為「1 2 3 5 6 7」，過程中你會得到 lst = [[1, 2, 3], [5, 6, 7]]
最後，將 lst 依照規則輸出，即得到答案。

來源
ccClub Judge
"""
# 使用 Two Pointer 解題
lst = [int(i) for i in input().split()]
j,k,re = 0,0,[]
for i in range(len(lst)):
  k += 1
  if k == len(lst) or lst[i] + 1 != lst[k]:
    re.append(lst[j:k])
    j = k
for i in re:
  print(' '.join(map(str,i)))
