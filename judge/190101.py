"""
ASCII sum
描述

如同我們剛才所說的，ASCII code是用來代表字元的一種編碼方式，可以透過ord(character)以及chr(code)來進行轉換：

給定兩個輸入的字元，請將其轉換成 ASCII code 並且相加以後輸出。


輸入
輸入有兩行，各包含一個字元（character）


輸出
輸出有一行，包含一個整數


輸入範例 1 
a
b

輸出範例 1
195

輸入範例 2 
A
B

輸出範例 2
131

來源
ccClub Judge
"""

count = 0
s = []
while True:
  try:
    s.append(input())
  except:
    break

for i in s:
  count += ord(i)
print(count)
