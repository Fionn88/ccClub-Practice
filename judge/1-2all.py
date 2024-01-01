"""
綜合1-2：一奇多偶

描述
給一個內含整數的串列 lst，其中只有一個元素出現過奇數次，其餘元素皆出現偶數次，找出出現奇數次的值並將其印出。

輸入
輸入為一行，包含數個整數，以空格分隔

輸出
輸出為一行，包含一個整數

輸入範例 1 
1 2 3 2 1 1 1 3 3 3 3

輸出範例 1
3

輸入範例 2 
1 2 3 4 2 3 4 5 6 6 5

輸出範例 2
1

來源
ccClub Judge
"""

sentence = input().split()
d = {}

for i in sentence:
  if i not in d:
    d[i] = 1
  else:
    count = d.get(i)
    count += 1
    d[i] = count


for i in d:
  if d[i] % 2 != 0:
    print(i)
    break
