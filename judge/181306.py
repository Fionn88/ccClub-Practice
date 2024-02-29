"""
合併串列

描述
給定兩個依照數字大小排序的串列，將其合併，並依照數字大小排序。

輸入
輸入有兩行，分別包含 n, m 個整數（n, m>=0），整數之間以空白為間隔

輸出
輸出為一行，包含 n 個整數（n>=0），整數之間以空白為間隔

輸入範例 1
1 3 5 7
2 4 6 8

輸出範例 1
1 2 3 4 5 6 7 8

輸入範例 2

2 4

輸出範例 2
2 4

來源
ccClub Judge
"""

def func(l1, l2):
  
  if not l1:
    return l2
  if not l2:
    return l1
  
  sorted_lst = []
  i, j = 0, 0
  l1 = list(map(int,l1))
  l2 = list(map(int,l2))

  while i < len(l1) and j < len(l2):
    if l1[i] <= l2[j]:
      sorted_lst.append(l1[i])
      i += 1
    else:
      sorted_lst.append(l2[j])
      j += 1

  sorted_lst.extend(l1[i:])
  sorted_lst.extend(l2[j:])

  return map(str,sorted_lst)

l1 = input().split()
l2 = input().split()
print(' '.join(func(l1,l2)))
