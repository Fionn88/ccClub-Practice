"""
阿偉下西洋棋

描述
阿偉最近突然對西洋棋感興趣了。他現在想要熟悉各個棋子的走法
已知棋盤是 8*8 的格子，左下角為 A1，左上角為 A8，右下角為 H1，以此類推。
皇后的走法是所有縱橫，及斜格(如下)，棋盤無其他阻擋的位子，試著幫阿偉找出所有皇后下一步可以走的位子。
=====
圖片請至 judge 查看
=====

輸入
輸入為一個棋盤上的位置，由大寫字母(A ~ H)和數字(1 ~ 8)組成

輸出
輸出為一個 list，記錄所有可以走的位置，按字母序及數字大小由小到大排序。

輸入範例 1
D4

輸出範例 1
['A1', 'A4', 'A7', 'B2', 'B4', 'B6', 'C3', 'C4', 'C5', 'D1', 'D2', 'D3', 'D5', 'D6', 'D7', 'D8', 'E3', 'E4', 'E5', 'F2', 'F4', 'F6', 'G1', 'G4', 'G7', 'H4', 'H8']
"""

def horizontal(pos,x):
    ans = []
    index = x.index(pos[0])
    for alphabet in x:
        if alphabet != x[index]:
            ans.append(f'{alphabet}{pos[1]}')
    return ans

def vertical(pos,y):
    ans = []
    for number in y:
        if number != pos[1]:
            ans.append(f'{pos[0]}{number}')
    return ans

def slash(pos,x):
    ans = []

    # 左下方
    index = x.index(pos[0])
    number = int(pos[1])
    while index != 0 and number != 1:
        index -= 1
        number -= 1
        ans.append(f'{x[index]}{number}')

    # 右上方
    index = x.index(pos[0])
    number = int(pos[1])
    while index != len(x) - 1 and number != 8:
        index += 1
        number += 1
        ans.append(f'{x[index]}{number}')

    # 左上方
    index = x.index(pos[0])
    number = int(pos[1])
    while index != 0 and number != 8:
        index -= 1
        number += 1
        ans.append(f'{x[index]}{number}')
    
    # 右下方
    index = x.index(pos[0])
    number = int(pos[1])
    while index != len(x) - 1 and number != 1:
        index += 1
        number -= 1
        ans.append(f'{x[index]}{number}')

    return ans

x = "ABCDEFGH"
y = "12345678"
pos = input()

print(sorted(horizontal(pos,x) + vertical(pos,y) + slash(pos,x)))
