"""
綜合2-1：費氏數列
描述

在遞迴的課堂中，我們介紹了使用遞迴的方式計算費氏數列。

已知費氏數列的定義， f(0) = 0 , f(1) = 1 , f(n) = f(n-1) + f(n-2)

給定一個正整數 n ，輸出一個 list ， list 中需包含 f(0) ~ f(n) 的值，共 n+1 項。

注意：請勿使用遞迴的方式解此題

提示：能只用 list 和 for loop 就完成此題嗎？


輸入
輸入為一行，包含一個正整數


輸出
輸出為一行，包含一個list


輸入範例 1 
3

輸出範例 1
[0, 1, 1, 2]

輸入範例 2 
0

輸出範例 2
[0]

來源
ccClub Judge
"""
def fibonacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        fib = [0, 1]
        for i in range(2, n+1):
            fib.append(fib[i-1] + fib[i-2])
        return fib

n = int(input())
ans = fibonacci(n)
print(ans)