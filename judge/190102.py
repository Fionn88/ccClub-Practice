"""
簡易計算機

描述
輸入包含兩個數字以及一個運算符號（"+", "-", "*", "/"），請依據運算符號進行相應的計算並輸出

輸入
輸入有三行，前兩行個包含一個整數，第三行包含一個字元

輸出
輸出有一行，包含一個浮點數 float

輸入範例 1 
123
234
+

輸出範例 1
357.0

輸入範例 2 
1111
104
-

輸出範例 2
1007.0

來源
ccClub Judge
"""

x = float(input())
y = float(input())
caculate = input()
if caculate == '+':
  print(x+y)
elif caculate == '-':
  print(x-y)
elif caculate == '*':
  print(x*y)
else:
  print(x/y)
  