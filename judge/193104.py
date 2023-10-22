"""
奇偶運算
描述

輸入兩個數字 a 和 b，依據數字的奇偶狀況做不同的指令：

如果皆為奇數，輸出 a-b
如果皆為偶數，輸出 a+b
如果一奇一偶，輸出 a*b

輸入
輸入有兩行，皆為整數。


輸出
輸出有一行，為一個整數。


輸入範例 1
15660
61506

輸出範例 1
77166

輸入範例 2 
47998
80907

輸出範例 2
3883374186

來源
ccClub Judge
"""

def check_even_odd(number):
  if number % 2 == 0:
    return True 
  else:
    return False

n1 = int(input())
n2 = int(input())
ans = []
ans.append(check_even_odd(n1))
ans.append(check_even_odd(n2))
if ans[0] == False and ans[1] == False:
  print(n1-n2)
elif (ans[0] == True and ans[1] == False) or (ans[1] == True and ans[0] == False):
  print(n1*n2)
elif ans[0] == True and ans[1] == True:
  print(n1+n2)
