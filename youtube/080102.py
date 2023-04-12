"""
[8-1] 閉區間
Description

給定 n 個整數，請計算總共有多少個整數介於閉區間 [a, b] 之間（含 a 與 b）


Input
輸入為兩行，第一行為兩整數，為閉區間的下限 a 與上限 b，兩整數間以逗號作為間隔；

第二行為數個整數，整數間以逗號作為間隔。


Output
輸出為一行，請輸出一個整數，表介於閉區間的整數個數


Sample Input 1 
2,8
7,4,1,8,3,11,6,2

Sample Output 1
6

Sample Input 2 
1,4
21,3,5,8,2,1,6,9,13,16

Sample Output 2
3

Source
ccClub Judge
"""
n = input().split(',')
nList = input().split(',')
ans = 0
for i in nList:
  if int(n[0]) <= int(i) <= int(n[1]):
    ans += 1
print(ans)
