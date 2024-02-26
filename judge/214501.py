"""
小明要上學

描述
小明住的城市是一塊完整的矩形，他家住在城市的左上角，每天要到城市右下角的學校上課
趕時間的他想知道他有幾種最短路線可以抵達學校，你可以幫幫他嗎？

輸入
一行數字，分別是矩形的寬跟長，空格分隔

輸出
一個數字，有幾種到學校的最短路徑

輸入範例 1
3 7

輸出範例 1
28

輸入範例 2
2 2

輸出範例 2
2

提示
小明不能斜著走
"""

# C(x+y−2,x−1)= (x+y−2)! // (x−1)!×(y−1)!

# Solution 1
# from math import factorial
# x, y = [int(_) for _ in input().split()]
# print(factorial(x + y - 2) // (factorial(x - 1) * factorial(y - 1)))

# Solution 2
def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num-1)

def combination(n, k):
    return factorial(n + k - 2) // (factorial(n - 1) * factorial(k - 1))

x, y = [int(_) for _ in input().split()]
print(combination(x, y))

# Error：It will encounter a RecursionError
# def factorial(number):
#     if number == 0:
#         return 1
#     return number * factorial(number)

# x, y = [int(_) for _ in input().split()]
# print(factorial(x + y - 2) // (factorial(x - 1) * factorial(y - 1)))
