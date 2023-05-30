"""
平均成績
描述

已知全班成績，輸入欲查詢的學生學號之後，輸出這些學生們的平均成績。


輸入
輸入有 n+2 行。

第 1 行包含一個整數 n，代表總共有 n 個學生。

第 2~n+1 行各包含兩個整數，數字間以空格分開，代表該學生的學號及成績。

第 n+2 行包含數個整數，數字間以空格分開，代表欲查詢的學生學號。


輸出
輸出有一行，包含一個浮點數，代表欲查詢學生們的平均成績。


輸入範例 1
5
3 100
2 90
5 80
4 70
1 60
5 3 1

輸出範例 1
80.0

輸入範例 2 
20
8 100
16 95
12 90
14 85
4 80
7 80
2 75
11 75
17 70
3 60
9 60
1 55
20 50
6 45
13 40
5 35
19 30
15 25
10 20
18 15
2 7 1 19 14 3 6 12 15 18

輸出範例 2
56.0

來源
ccClub Judge
"""
n = int(input())
gradeSet = {}
for i in range(n):
  student,grade = input().split()
  gradeSet[student] = int(grade)
sarch = input().split()
ans = []
for i in sarch:
  ans.append(gradeSet[i])

print(sum(ans)/len(ans))
