"""
揪狼殺
描述

恬很想要玩狼人殺，就問了他的朋友們哪些時間有空。

因為恬很喜歡玩十二人局（亦即需要有十二個玩家），在人數不到十二人的情況下，恬會約最多人有空的時間。

倘若人數超過十二人的情況下，恬會約超過十二人連續最長的時間（希望可以玩越久越好，如果有複數個相同，請輸出最早的那個時間）。

請寫一個程式，根據恬的朋友們回報的狀況，統計出恬要約狼殺的時間。


輸入
輸入有 n+1 行。

第 1 行為數字 n，代表恬總共問了幾個朋友。

第 2~n+1 行分別為每個朋友的回報狀況，每一行有數個整數（0~23），數字間用空格分割，代表該位朋友幾點有空。


輸出
輸出為 1 行，包含一個整數，代表恬要約幾點。

規則：

如果人數不到十二人：選擇人數最多的那個時間。
如果人數人數夠，則選擇人數至少十二人中，連續最長的時間（輸出起始時間）

輸入範例 1 
22
20 5 7 22 9 15 23
23 12 3 6 17 8 15 19 20 4 0 1 14
18 22 21 0 17 19 6 9 12 13 1 3
14 22 23 4 5 1 10 8 17 3 20 11
5 12 3 21 19 2 9 8 15 17 10 1
7 6 21 5 4 22 12 15 8 0 1 11 13 10 14 19 18
4 8 16 15 7 13 10 14 17 0 23 1 22
20 0 8 23 1 11 3 22 2 14 15 5 6 17 16 9 19 4
15 20 8 9 13 23 16 17
21 2 7 9 20 17 1 3 15 13 16 12 10 6 8
7 9 15 1 8 2 19 5 20 4
20 15 6 13 2 7 16
14 12 16 22 23 0 4 8 20 6 11 3 15 18 2 19 5 9 10 17
23 9 18 5 10 20 8 0 1 11 7 19 4 6 16
18 14 2 8 23 10 1 11 6 16 4 0 17 7 3
0 18 13 2 21 22 20
22 13 9 11 23 5 8
2 8 4 12 5 21 17 16 13 0 18
17 13 8 18 5 21 10 2
17 1 20 0 9 3 16 6
17 22 15 18 0 5
19 10 22 15 16

輸出範例 1
0

輸入範例 2 
21
1 8 6 11 21 13 7 0 19 2 18 15 17
2 23 22 5 16 18 20 9 1 14
15 9 14 5 18 4 21 11 3
21 19 16 14 12 7 18 6 15 9 17 0 11 3 22 10 2
15 8 19 20 6 13 1
6 15 3 8 5 14 13 20
10 18 16 20 6 17 19
1 0 5 19 14 17 11 15 4 7 10 20 23 22 18 13 21 16
13 22 20 8 15 23 10 6 3 5 19 12 7 18
9 2 0 17 23 8 20 11 13 21 11 8 19 7 12 14
18 10 3 5 20 1 12 17 11 16 19 0 14 6 2
22 7 14 23 18 8
6 22 5 18 14 4 10 3 19 13
12 4 17 20 5 6 9 11 23 16 019 14 15
12 18 17 19 4 21 23 13 1 0 3 14 9 22 15
13 0 9 16 11 19 10 6 23 3 12 18 8 21 20 17 14 5 7 2
23 3 16 12 1 11 2 17 15 19 22 14 18
16 8 0 13 17 22 15 18 11 6 19 20 21 4
2 15 22 8 21 9 12 16 17 4 7 20 3 13 18 0 14 1 19 6
7 11 2 19 0 5 3 21
3 5 20 10 23 17

輸出範例 2
17

提示
雖然題目說是十二人局，但因為一直玩很累所以恬還是希望能找 12 個朋友。

來源
ccClub Judge
"""
n = int(input())
valueOfPeopleHaveSpareTime = [0] * 25
ans = {}
initGraterTwelvePeopleTimePoint,constantTimeCount = 25,0

for _ in range(n):
    timeList = input().split()
    for timePoint in timeList:
        valueOfPeopleHaveSpareTime[int(timePoint)] += 1

for timePoint in range(25):
    if valueOfPeopleHaveSpareTime[timePoint] >= 12 and timePoint <= initGraterTwelvePeopleTimePoint:
        constantTimeCount += 1
        initGraterTwelvePeopleTimePoint = timePoint
        ans[initGraterTwelvePeopleTimePoint] = constantTimeCount
    elif valueOfPeopleHaveSpareTime[timePoint] >= 12 and timePoint > initGraterTwelvePeopleTimePoint:
        constantTimeCount += 1
        ans[initGraterTwelvePeopleTimePoint] = constantTimeCount
    elif valueOfPeopleHaveSpareTime[timePoint] < 12:
        constantTimeCount = 0
        initGraterTwelvePeopleTimePoint = 25

if ans:
    print(max(ans, key=ans.get))
else:
    print(valueOfPeopleHaveSpareTime.index(max(valueOfPeopleHaveSpareTime)))