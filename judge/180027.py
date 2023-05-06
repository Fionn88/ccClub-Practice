"""
10-2：自訂費式數列
描述

已知 f(0) = 0，f(1) = 1，f(2) = 2，f(n) = f(n-1) + f(n-2) + f(n-3)。輸入數字 n ，輸出 f(n)。


輸入
輸入為一行，包含一個正整數n


輸出
請輸出f(n)


輸入範例 1 
2

輸出範例 1
2

輸入範例 2 
3

輸出範例 2
3

來源
ccClub Judge
"""
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
      return 2
    else:
        return fibonacci(n-1) + fibonacci(n-2) + fibonacci(n-3)
print(fibonacci(int(input())))