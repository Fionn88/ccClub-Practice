"""
ASCII code
描述

如同我們剛才所說的，ASCII code是用來代表字元的一種編碼方式，可以透過ord(character)以及chr(code)來進行轉換：

給定一個字串，請輸出所有字元的ASCII code

輸入
輸入為一行，包含一個長度為n的字串

輸出
輸出為n行，各包含一個整數代碼


輸入範例 1 
abc

輸出範例 1
97
98
99

輸入範例 2 
ccClub

輸出範例 2
99
99
67
108
117
98

來源
ccClub Judge
"""

s = input()
for i in s:
  print(ord(i)) 
