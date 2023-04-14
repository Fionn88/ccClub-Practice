"""
[10-1] 最大平方數
Description

請實作一個函式square_check，這個函式會回傳小於參數 n 的最大的平方數（n 必定大於 0）。本題只需實作函式，不用自行處理 input()。


Input
輸入為一數字。


Output
函式在符合條件才有回傳值，型態為整數。


Sample Input 1 
10

Sample Output 1
9

Sample Input 2 
25

Sample Output 2
16

Source
ccClub Judge
"""
def square_check(x):
  if x == 1:
    print(0)
  elif x == 2:
    print(1)
  else:
    for i in range(1,x):
      if i*i >= x:
        print((i-1)*(i-1))
        break

n = int(input())
square_check(n)

