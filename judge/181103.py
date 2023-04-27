"""
字串加密 II
描述

輸入一個字串以及一個數字，請依index將字串中的字元對應數字來進行加密：

舉例如下：

輸入abc以及123，請將a經由ASCII code加1進行轉換，b加2、c加3...以此類推


輸入
輸入有兩行，包含一個長度為n的字串以及一個整數（字串與整數的長度不一定相等，以字串長度為準：如果字串比較長要把數字補齊；如果數字比較長的話把多餘的截斷。）


輸出
輸出為一行，包含一個字串


輸入範例 1 
abc
183

輸出範例 1
bjf

輸入範例 2 
ccClub
61743

輸出範例 2
idJpxh

來源
ccClub Judge
"""
s = input()
n = input()

j = 0
for i in s:
  try:                 
    print(chr(ord(i)+int(n[j])),end='')
  except:                   
    j = 0
    print(chr(ord(i)+int(n[j])),end='')
  j += 1
