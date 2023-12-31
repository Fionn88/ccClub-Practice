"""
長方形家族

描述
給定平面上四個點，皆為整數，且 x, y 範圍皆在 10 內。
四個點分別是 (X1,Y1) (左上) , (X2,Y2) (右上) , (X3,Y3) (左下) , (X4,Y4) (右下)，請判斷這四個點是否能組成與 x 軸及 y 軸平行的正方形。
如果可以，則輸出”正方形”，如果判斷是長方形則輸出”長方形”，如果都不屬於，則輸出“什麼也不是”。

輸入
共 1 行，代表 x1 y1 x2 y2 x3 y3 x4 y4，數字間用空白隔開

輸出
共 1 行，如果是正方形則輸出”正方形”，若為長方形，則輸出”長方形”，如果都不屬於，則輸出“什麼也不是”。

輸入範例 1 
0 1 1 1 0 0 0 1

輸出範例 1
什麼也不是

輸入範例 2 
0 1 1 1 0 0 1 0

輸出範例 2
正方形
"""

x1, y1, x2, y2, x3, y3, x4, y4 = [int(i) for i in input().split()]

# 確保是長方形
if y1 == y2 and y3 == y4 and x1 == x3 and x2 == x4 and x2 - x1 > 0 and y2 - y4 > 0:
    # 垂直兩邊一樣長
    if x2 - x1 == y1 - y3:
        print('正方形')
    else:
        print('長方形')
else:
    print('什麼也不是')
