"""
奇偶遞迴
描述

今天請利用遞迴實踐一個函式 f(x)：

當 x = 1，f(1) = 1。當 x = 2k + 1 (k >= 1)，即大於 1 的正奇數，f(2k + 1) = f(k) + f(k + 1)。當 x = 2^n * k (n >= 1, k >= 1)，即正偶數，f(2^n * k) = f(k)。

舉例來說，若 x = 12：f(12) = f(2^2 * 3) = f(3) = f(2 * 1 + 1) = f(1) + f(2) = f(1) + f(2^1 * 1) = f(1) + f(1) = 1 + 1 = 2。

請在給定正整數 n 的情況下，算出 f(n)。


輸入
輸入為一行，包含一個正整數 n。


輸出
輸出為一行，包含一個正整數 f(n)。


輸入範例 1 
12

輸出範例 1
2

輸入範例 2 
3

輸出範例 2
2

來源
ccClub Judge
"""

def f(x):
    if x == 1:
        return 1
    elif x > 1 and x % 2 == 1:
        k = x // 2
        return f(k) + f(k + 1)
    else:
        k = x // 2
        return f(k)
n = int(input())
print(f(n))
