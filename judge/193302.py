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
matrix = []
result = []
for _ in range(n):
    a1, b1, c1, d1 = map(int,input().split())
    matrix.append([a1,b1,c1,d1])

for index in range(n-1):
    if index == 0:
        a = matrix[0][0] * matrix[1][0] + matrix[0][1] * matrix[1][2]
        b = matrix[0][0] * matrix[1][1] + matrix[0][1] * matrix[1][3]
        c = matrix[1][0] * matrix[0][2] + matrix[1][2] * matrix[0][3]
        d = matrix[1][1] * matrix[0][2] + matrix[0][3] * matrix[1][3]
        result.extend([a,b,c,d])
    else:
        a = result[0] * matrix[index+1][0] + result[1] * matrix[index+1][2]
        b = result[0] * matrix[index+1][1] + result[1] * matrix[index+1][3]
        c = matrix[index+1][0] * result[2] + matrix[index+1][2] * result[3]
        d = matrix[index+1][1] * result[2] + result[3] * matrix[index+1][3]
        result[0] = a
        result[1] = b
        result[2] = c
        result[3] = d

print(result)
