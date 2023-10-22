"""
小明發便當
描述

在午餐時間有兩種不同口味的便當，依照給定的順序疊成一疊，並且有一群學生排成一列領便當每個人都分別喜歡一種口味。
在學生領便當的時候，如果最上方的便當不是自己喜歡的口味，學生就會重新回到隊伍的最後面排隊；
但如果是自己喜歡的口味，學生就會取走便當並離開。每個學生最多只會吃一個便當。
在給定便當口味的順序與喜歡不同口味的學生個數下，其中便當數量和人數不一定相同，請問最後有多少人吃不到便當？

舉例來說：
便當兩種口味分別為A、B口味，疊便當的順序從高至低為BAAB。
喜歡吃A口味的有1人，喜歡吃B口味的有3人。
其中一個喜歡B口味的學生會領走第一個邊當，然後喜歡A口味的學生會領走第二個便當，最後因為沒有人取走第三個便當(A口味)所以留下兩個人挨餓。


輸入
輸入包含三行：
第一行為一個字串，由字母 'A''B' 組成，代表疊起來的便當口味順序。
第二行跟第三行分別為喜歡口味 A 以及喜歡口味 B 便當的學生數量。


輸出
輸出為一行，包含一個整數，為吃不到便當的學生人數。


輸入範例 1 
BAAB
1
3

輸出範例 1
2

輸入範例 2 
AABBABAB
1
10

輸出範例 2
10

提示
提示1：跟排隊的順序沒關係
提示2：pop(-1) 比 pop(0) 快很多，至於為什麼...歡迎大家關注未來會推出的資料結構與演算法課程

來源
ccClub Judge
"""

n = list(input())
A = int(input())
B = int(input())
while len(n) > 0 and A >= 0 and B >= 0:
  if n[0] == 'A':
    n.pop(0)
    A -= 1
  elif n[0] == 'B':
    n.pop(0)
    B -= 1
if A < 0 or B < 0:
  print(A+B+1)
elif A > 0 or B > 0:
  print(A+B)
else:
  print(0)
