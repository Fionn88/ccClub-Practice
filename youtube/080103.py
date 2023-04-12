"""
[8-1] 質數I
Description

給定一個正整數 n，請判斷此正整數是否為質數。若為質數請輸出 True，反之則輸出 False。


Input
輸入為一行，為一個正整數。


Output
輸出為一行，為一個布林值。


Sample Input 1 
5

Sample Output 1
True

Sample Input 2 
102

Sample Output 2
False

Source
ccClub Judge
"""
n = int(input())
count = 0
for i in range(1,n+1):
  if n % i == 0:
    count+=1
   
if count > 2:
  print(False)
else:
  print(True)
