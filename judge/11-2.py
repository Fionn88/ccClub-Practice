"""
11-2：字串字典
描述

給定一個字串 s，請利用字典，依照字母順序輸出此字串中每個不同字元的出現次數。

英文大小寫視為一樣，若出現非英文字母的符號將不計（詳見 sample input 2）


輸入
輸入為一行，包含一個字串s


輸出
輸出為一行，依照字母順序輸出此字串中每個不同字元的出現次數，以空白間隔。


輸入範例 1 
apple

輸出範例 1
a1 e1 l1 p2

輸入範例 2 
python3

輸出範例 2
h1 n1 o1 p1 t1 y1

來源
ccClub Judge
"""

s = input()
d = {}
for i in s:
  if i.isalpha() and all(ord(c) < 128 for c in i):
    if i.lower() not in d:
        d[i.lower()] = 1
    else:
        count = d.get(i.lower())
        count += 1
        d[i.lower()] = count

sort_dictionary = dict(sorted(d.items(), key=lambda item: item[0])) 
count = 0
for key, value in sort_dictionary.items():
    if count == len(sort_dictionary) - 1:  # 最後一個元素
        print(key, value, sep='')
    else:
        print(key, value, sep='', end=' ')
        count += 1