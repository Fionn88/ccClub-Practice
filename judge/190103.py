"""
字串解密
描述

今天我們要藉由 ASCII 來進行解密，給定一個字串，請將 index 為零的字元轉換為 ASCII code 下編碼 -1 的字元，index為 1 的字元轉換為 ASCII code 下編碼 -2的字元，以此類推來進行加密


輸入
輸入為一行，包含一個字串


輸出
輸出為一行，包含一個字串


輸入範例 1 
bdf

輸出範例 1
abc

輸入範例 2 
deFpzh

輸出範例 2
ccClub

來源
ccClub Judge
"""
s = input()
for index,value in enumerate(s):
  if index == len(s) -1:
    print(chr(ord(value) - (index+1)))
  else:
    print(chr(ord(value) - (index+1)),end='')
