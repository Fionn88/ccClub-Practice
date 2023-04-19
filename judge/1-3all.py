"""
綜合1-3：字母數（ㄕㄨˇ）數（ㄕㄨˋ）
描述

輸入一個字串（保證皆為小寫英文字母），依照字母順序 a~z，輸出每個英文字母以及他出現的次數。


輸入
輸入為一行，包含一個字串


輸出
輸出為一個字串，包含數個字母以及其出現的次數


輸入範例 1 
banana

輸出範例 1
a3b1n2

輸入範例 2 
pneumonoultramicroscopicsilicovolcanoconiosis

輸出範例 2
a2c6e1i6l3m2n4o9p2r2s4t1u2v1

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

for key, value in sort_dictionary.items():
    print(key, value, sep='',end='')
