"""
拍手遊戲

描述
為了加強寶寶們對倍數的熟悉程度，張老師又設計了一個數數遊戲：給定一個終點數字 n ，小朋友們要圍一個圈，從 1 開始，一路數到 n ，沿路上如果遇到 3 的倍數要拍手，5 的倍數要拍頭，如果同時是 3 和 5 的倍數則要拍手拍頭，現在，給定數字 n ，請你依序輸出所有寶寶們對應到應該做的事。

輸入
共一行，包含一正整數

輸出
若干行輸出，依指令順序輸出。

輸入範例 1 
2

輸出範例 1
1
2

輸入範例 2 
5

輸出範例 2
1
2
拍手
4
拍頭
"""

n = int(input())
for i in range(1,n+1):
    if i % 3 == 0 and i % 5 == 0:
        print("拍手拍頭")
    elif i % 3 == 0:
        print("拍手")
    elif i % 5 == 0:
        print("拍頭")
    else:
        print(i)
