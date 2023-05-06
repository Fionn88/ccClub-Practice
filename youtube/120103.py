"""
[12-1] 自訂數列
描述

請完成函式f，已知 f(0) = 0，f(1) = 1，f(n) = n*f(n-2) - f(n-1)。

f(2) = 2*f(0) - f(1) = 0 - 1 = -1

f(3) = 3*f(1) - f(2) = 3 - (-1) = 4

f(4) = 4*f(2) - f(3) = (-4) - 4 = -8

f(5) = 5*f(3) - f(4) = 20 - (-8) = 28

以此類推。

輸入數字 n ，輸出 f(n)。


輸入
輸入有一行，包含一個正整數 n。


輸出
輸出有一行，包含一個整數 f(n)。


輸入範例 1 
1

輸出範例 1
1

輸入範例 2 
5

輸出範例 2
28

來源
ccClub Judge
"""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n*fibonacci(n-2)- fibonacci(n-1)
print(fibonacci(int(input())))