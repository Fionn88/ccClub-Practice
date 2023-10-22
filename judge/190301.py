"""
簡易計算機 II
描述

請實作一個函式calculator，依據輸入的運算符號做相對應得運算。

def calculator(num1, num2, op):
    # do something
    return ans
PS 本題只需實作函式，並不用自行處理 input()


輸入
函式有三個參數：

num1: 型態為 float
num2: 型態為 float
op: 型態為 str，代表要做的運算（本題支援"+", "-", "*", "/" 四種運算）。

輸出
函式有一個回傳值，型態為 float。


輸入範例 1
calculator(123, 234, "+")

輸出範例 1
357.0

輸入範例 2 
calculator(1111, 104, "-")

輸出範例 2
1007.0

來源
ccClub Judge
"""

def calculator(num1, num2, op):
    if op == "+":
      ans = num1 + num2
    elif op == "-":
      ans = num1-num2
    elif op == "*":
      ans = num1*num2
    else:
      ans = num1/num2
    return ans
