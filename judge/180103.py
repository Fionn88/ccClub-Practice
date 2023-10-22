"""
字串加密
描述

如同我們剛才所說的，ASCII code是用來代表字元的一種編碼方式，可以透過ord(character)以及chr(code)來進行轉換：

今天我們要藉由ASCII來進行加密，給定一個字串，請將 index 為零的字元轉換為ASCII code下編碼 +1的字元，index為 1 的字元轉換為ASCII code下編碼 +2的字元，以此類推來進行加密


輸入
輸入為一行，包含一個字串 s


輸出
輸出為一行，包含一個經過加密後的字串


輸入範例 1 
abc

輸出範例 1
bdf

輸入範例 2 
ccClub

輸出範例 2
deFpzh

來源
ccClub Judge
"""

s = input()
for i in range(len(s)):
  print(chr(ord(s[i])+i+1),end='') 
