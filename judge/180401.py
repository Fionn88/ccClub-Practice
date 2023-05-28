"""
變形費式相乘
描述

請利用遞迴，實作以下方程式 f(x)，並輸出結果：

如果 x 在 1 到 4 之間，f(x) = x ；若否，則 f(x) = f(x-1) + f(x-2)*2 + f(x-3)*3 + f(x-4)*4。

給定 x 的值，請輸出 f(x)的值。


輸入
輸入為一行，內容為一個整數。


輸出
輸出為一行，包含一個整數。


輸入範例 1 

13
輸出範例 1

28207
輸入範例 2 

6
輸出範例 2

45
來源

ccClub Judge
"""
# =============== Wrong Answer ================
def fibonacci(n):
    print(n)
    if n >= 1 and n <= 4:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)*n + fibonacci(n-3)*n + fibonacci(n-4)*n
print(fibonacci(int(input())))