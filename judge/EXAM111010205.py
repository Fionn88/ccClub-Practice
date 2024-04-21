"""
行列式

描述
給定一個 n * n 的矩陣 A，試計算矩陣 A 行列式的值，det(A)。

輸入
輸入共有一組測試資料。其中第一行為一個正整數 n。
接下來有 n 行，每行有 n 個整數，其中第 i 行（row）的第 j 個數為 Aij 的值。

輸出
輸出共一個數，為det(A)

輸入範例 1
2
1 2
3 4

輸出範例 1
-2

輸入範例 2
4
80 -80 -83 -66
-13 -48 -58 -79
-34 77 -47 0
-60 36 55 -76

輸出範例 2
-67697286

提示
1 <= n <= 6
100 <= Aij <= 100
"""

def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    else:
        det = 0
        for j in range(n):
            cofactor = matrix[0][j] * determinant(cofactor_matrix(matrix, 0, j))
            det += (-1) ** j * cofactor
        return det

def cofactor_matrix(matrix, row, col):
    n = len(matrix)
    return [[matrix[i][j] for j in range(n) if j != col] for i in range(n) if i != row]

length = int(input())
matrix = []
for _ in range(length):
    input_data = list(map(int,input().split()))
    matrix.append(input_data)

print(determinant(matrix)) 
