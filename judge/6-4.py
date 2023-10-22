"""
6-4：數字和
Description

輸入一個數字，輸出各個位數的數字總和。


Input
輸入有一行，包含一個整數


Output
輸出為一個整數


Sample Input 1 
123

Sample Output 1
6

Sample Input 2 
666

Sample Output 2
18

Source
ccClub Judge
"""

N = input()
ans = 0
for i in N:
  ans += int(i)
print(ans)
