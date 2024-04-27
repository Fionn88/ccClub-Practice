"""
矩陣相乘

描述
請寫一個能夠計算矩陣相乘的程式，在這題中，我們只需要運算 2*2 的矩陣。
兩個 2*2 的矩陣相乘後的結果如下：
=====
請至 judge 上查看
=====

輸入
輸入有 n+1 行。
第 1 行為一個整數，代表總共有幾個矩陣。
第 2 ~ n 行，每行有 4 個數字，代表一個 2*2 的矩陣（依序分別為題目敘述中的 a, b, c, d），數字之間用空格分開。

輸出
請將這 n 個矩陣照順序相乘後，將結果放到一個 list，並印出這個 list。

輸入範例 1
2
21 53 158 194
15 30 32 50

輸出範例 1
[2011, 3280, 8578, 14440]

輸入範例 2
4
74 67 180 140
56 135 33 149
29 79 165 70
121 75 54 8

輸出範例 2
[523669010, 276189240, 1186616700, 625407500]

來源
ccClub Judge
"""

n = int(input())
matrix = list(map(int,input().split()))

for index in range(n-1):
    a1, b1, c1, d1 = map(int,input().split())
    a = matrix[0] * a1 + matrix[1] * c1
    b = matrix[0] * b1 + matrix[1] * d1
    c = a1 * matrix[2] + c1 * matrix[3]
    d = b1 * matrix[2] + matrix[3] * d1
    matrix[0] = a
    matrix[1] = b
    matrix[2] = c
    matrix[3] = d

print(matrix)
