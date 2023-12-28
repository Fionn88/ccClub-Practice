"""
拼圖遊戲
描述

小丹買了一幅新拼圖，在開始拼拼圖前，他想先把所有拼圖做個簡單分類。
給定每片拼圖的類別，請把拼圖整理好後，按照各類別的出現順序分行印出。


輸入
輸入有若干行，每行包含數個小寫英文字母，為散亂的拼圖，以字母代表該片拼圖的類別。
最後一行包含一個 0，代表輸入結束。


輸出
輸出有 n 行，n 為拼圖的類別數。
每行包含該類別的所有拼圖。


輸入範例 1 
ababc
bbcc
0

輸出範例 1
aa
bbbb
ccc

輸入範例 2 
eeca
eb
0

輸出範例 2
eee
c
a
b
"""

D = {}
while True:
    s = input()
    if s == "0":
        break
    for i in s:
        if i not in D:
            D[i] = 1
        else:
            D[i] += 1

for key, value in D.items():
    print(key*value)
