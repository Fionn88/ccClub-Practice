"""
矩陣變形
描述

給定一個 M x N 的矩陣

請將其變形成 O x P 的矩陣，其中 M x N = O x P

舉例來說，今天有一個 M x N = 3 x 4 的矩陣如下：

1 2 3 4

5 6 7 8

9 10 11 12

若給定 O x P = 2 x 6，請輸出如下矩陣：

1 2 3 4 5 6

7 8 9 10 11 12


輸入
輸入第一行為 M 和 N 第二行為 O 和 P，以下 M 行各有 N 個數字，以空白分開


輸出
輸出包含 O 行，每行各有 P 個數字用空白分開


輸入範例 1 
3 4
2 6
1 2 3 4
5 6 7 8
9 10 11 12

輸出範例 1
1 2 3 4 5 6
7 8 9 10 11 12

輸入範例 2 
8 3
12 2
2 1 3
4 3 1
3 3 1
4 1 4
4 2 2
2 2 1
2 2 4
3 3 2

輸出範例 2
2 1
3 4
3 1
3 3
1 4
1 4
4 2
2 2
2 1
2 2
4 3
3 2

來源
ccClub Judge
"""

M, N = map(int, input().split())
O, P = map(int, input().split())

# 讀取矩陣
original_matrix = []
for _ in range(M):
    row = list(map(int, input().split()))
    original_matrix.extend(row) 

# 轉換矩陣
new_matrix = []
for i in range(0, len(original_matrix), P):
    new_matrix.append(original_matrix[i:i+P])

for row in new_matrix:
    print(' '.join(map(str, row)))
