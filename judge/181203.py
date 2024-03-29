"""
完全平方數 II

描述
定義：對於任意整數 Q，只要符合 P = Q * Q 的條件，我們視為 P 為一個完全平方數。
給定兩個數字 a 和 b，保證 a <= b，請找出 [a, b] 區間中有幾個完全平方數（包含 a 和 b）。

輸入
輸入為一行，包含兩個整數，數字間以空格分開。

輸出
輸出為一行，包含一個整數。

輸入範例 1 
-3 4

輸出範例 1
3

輸入範例 2 
-1234 -1

輸出範例 2
0

來源
ccClub Judge
"""

def countPerfectSquares(a, b):
    count = 0
    num = 0
    while num * num <= b:
        if num * num >= a:
            count += 1
        num += 1
    return count

a, b = map(int, input().split())
result = countPerfectSquares(a, b)
print(result)
