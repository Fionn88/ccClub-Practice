"""
[8-3] 質數II
Description

接續上題 質數I ，請試著將這期教學影片中的 break ，加入迴圈中適當的位置。


Input
輸入為一行，為一個正整數。


Output
輸入為一行，為一個正整數。


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
i = 1
while i < n+1:
  if n % i == 0:
    count+=1
  i += 1
   
if count > 2:
  print(False)
else:
  print(True)
