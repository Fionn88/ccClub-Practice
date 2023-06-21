"""
字元數數
描述

找出一個句子中指定字元出現的次數。


輸入
輸入有兩行。

第一行有三個字元 a, b, c，彼此之間用空格分開。

第二行是一個字串，代表一個句子。


輸出
輸出有一行，包含三個數字，代表 a, b, c 出現的次數。


輸入範例 1 
a d i
I am a idiot

輸出範例 1
2 1 3

輸入範例 2 
y s d
So don t you worry your pretty little mind  People throw rocks at things that shine

輸出範例 2
4 4 2

來源
ccClub Judge
"""
from collections import Counter
key = input().split()
s = input().replace(" ", "").lower()
countChar = dict(Counter(s))
for index,value in enumerate(key):
  if index == len(key) - 1:
    print(countChar.get(value))
  else:
    print(countChar.get(value),end=' ')
