"""
凱凱去 shopping
描述

凱凱是個棒球狂，每次進到支持球隊的旗艦店就會忍不住購物。

由於想買的東西總是太多，常常最後結帳時才發現錢不夠，需要把商品再擺回架上。

請你寫一個程式，根據預算的額度，當錢不夠的時候提醒他。


輸入
輸入有 n+2 行。

第一行為一個正整數，代表預算的額度。

第二行為一個正整數 n ，代表想要買的商品種類數量

接下來 3 至 n+2 行，每行有兩個資訊，分別為商品名稱（字串）和售價（正整數），彼此間以空格分開。


輸出
輸出有 m+1 行。

第一行為購買的商品種類數量。

第 2 至 m+1 行每行為購買的商品名稱（依照想買的順序排列），若錢不夠買任何商品則輸出「一項都買不起」


輸入範例 1
400
6
經典球衣#92 2040
經典球衣#59 1980
T-shirt#23 1080
應援球帽#15 840
應援毛巾#15 410
應援毛巾#32 430

輸出範例 1
0
一項都買不起

輸入範例 2 
600
5
紀念球#11 360
應援毛巾#22 390
經典球衣#71 2080
應援毛巾#4 350
應援毛巾#7 450

輸出範例 2
1
紀念球#11

輸入範例 3 
14000
18
應援球帽#89 840
紀念球#85 360
經典球衣#65 2000
應援球帽#33 860
經典球衣#13 2040
經典球衣#97 2000
經典球衣#60 2000
應援球帽#38 900
T-shirt#95 1020
經典球衣#64 2040
應援毛巾#11 450
應援球帽#44 800
紀念球#5 360
應援毛巾#7 410
T-shirt#4 980
紀念球#39 380
紀念球#9 300
應援球帽#66 800

輸出範例 3
13
應援球帽#89
紀念球#85
經典球衣#65
應援球帽#33
經典球衣#13
經典球衣#97
經典球衣#60
應援球帽#38
T-shirt#95
應援毛巾#11
應援球帽#44
紀念球#5
紀念球#9

提示
想要買的商品依照喜好度排序，凱凱會依照喜好度順序購買。
"""

money = int(input())
category = int(input())
ans = []
for _ in range(category):
    item,price = input().split()
    money -= int(price)
    if money >= 0:
        ans.append(item)
    else:
        money += int(price)
if not ans:
    print(0)
    print("一項都買不起")
else:
    print(len(ans))
    for i in ans:
        print(i)
