"""
[5-綜合] 到站時間
Description

輸入火車的出發時間與行駛時間，請輸出火車的到站時間。時間的格式固定為 24 小時制，個位數字前面不用補零。


Input
輸入為兩行，第一行為火車出發時間，格式為 hh:mm；第二行為行駛時間，固定以分鐘為單位。


Output
輸出為一行，請輸出火車到站時間，格式為 小時:分鐘。


Sample Input 1 
15:32
37

Sample Output 1
16:9

Sample Input 2 
6:10
74

Sample Output 2
7:24

Source
ccClub Judge
"""

t = input().split(":")
add = int(input())
if int(t[1])+add <60:
  print(t[0],":",int(t[1])+add,sep='')
elif (int(t[1])+add) % 60 != 0:
  hour = int(t[0]) + (int(t[1])+add) // 60
  print(hour,":",int(t[1])+add - 60*(hour-int(t[0])),sep='')