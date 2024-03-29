"""
合併串列 II

描述
請實作一個函式 func，給定兩個依照數字大小排序的串列，將其合併，並依照數字大小排序後回傳。
注意：請勿使用 sort() 或 sorted()。

本題只需實作函式，不需要自己處理輸入和輸出

輸入
函式有兩個參數，l1 及 l2 為兩個由小到大排序好的串列，元素皆為整數。

輸出
請回傳一個串列，為將兩個串列合併後由小到大排序好的串列。

輸入範例 1
l1 = [1, 3, 5, 7]
l2 = [2, 4, 6, 8]
func(l1, l2)

輸出範例 1
[1, 2, 3, 4, 5, 6, 7, 8]

輸入範例 2
l1 = []
l2 = [2, 4]
func(l1, l2)

輸出範例 2
[2, 4]

輸入範例 3
l1 = [1, 1, 2, 2, 3, 4]
l2 = [2, 3, 4, 4]
func(l1, l2)

輸出範例 3
[1, 1, 2, 2, 2, 3, 3, 4, 4, 4]
"""

# Using "del" will encounter a TLE => del is O(N)
def func(l1, l2):
  
  if not l1:
    return l2
  if not l2:
    return l1
  
  sorted_lst = []
  i, j = 0, 0

  while i < len(l1) and j < len(l2):
    if l1[i] <= l2[j]:
      sorted_lst.append(l1[i])
      i += 1
    else:
      sorted_lst.append(l2[j])
      j += 1

  sorted_lst.extend(l1[i:])
  sorted_lst.extend(l2[j:])

  return sorted_lst

l1 = [1, 1, 2, 2, 3, 4]
l2 = [2, 3, 4, 4]
print(func(l1, l2))
