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

# Wrong Answer
def func(l1, l2):
  sorted_lst = l1 + l2
  length = len(sorted_lst)
  for front in range(length-1):
    for back in range(1,length):
      if sorted_lst[front] > sorted_lst[back]:
        swap = sorted_lst[front]
        sorted_lst[front] = sorted_lst[back]
        sorted_lst[back] = swap
  
  return sorted_lst

l1 = [1, 3, 5, 7]
l2 = [2, 4, 6, 8]
print(func(l1, l2))
