"""
助教業績統計
描述

每次的課程總是有一些辛勤的助教在幫助大家解惑。

希望你能夠寫個小程式，幫計算每個助教的業績，並找出業績最高的助教。


輸入
每一行有多個數字，數字之間以空格分開，第 n 行代表編號 n 的助教每天的業績。

最後一行為 0 ，代表結束輸入助教的業績。


輸出
輸出有一行，包含兩個數字，分別代表業績最高的助教編號，以及他的總業績。

數字之間用空格分開。


輸入範例 1 
1 2 3 4
5 6 1
1 1 2 2 2 2
0

輸出範例 1
2 12

輸入範例 2 
1 2 3
4 5 6
7 8 9
100
10 11 2 1 4 6 7 3
5 3 2 5 7
0

輸出範例 2
4 100

來源
ccClub Judge
"""
ans = []
while True:
    num = input()
    if num == '0':
        break
    else:
        count = 0
        num = list(map(int,num.split()))
        ans.append(sum(num))

maxCount = max(ans)
print(ans.index(maxCount)+1,end=' ')
print(maxCount)

