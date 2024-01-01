"""
天數相差

描述
給定兩個日期（年、月、日），請計算出這兩日期之間相「差」幾天

輸入
輸入為兩行，各包含三個整數（年、月、日）

輸出
輸出為一行，包含一個整數


輸入範例 1 
1997 12 27
1997 12 21

輸出範例 1
6

輸入範例 2 
2017 7 21
2019 4 24

輸出範例 2
642

提示
建議使用 datetime 這個模組

來源
ccClub Judge
"""

import datetime
d1 = [int(i) for i in input().split()]
d2 = [int(i) for i in input().split()]
td1 = datetime.date(d1[0],d1[1],d1[2])
td2 = datetime.date(d2[0],d2[1],d2[2])
print(abs(td1 - td2).days)

# 可不用 int 的解法

# import datetime
# d1 = datetime.datetime.strptime(input(), '%Y %m %d')
# d2 = datetime.datetime.strptime(input(), '%Y %m %d')
# print(abs(d1 - d2).days)
