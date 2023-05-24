"""
時間戳記
Description

經過程式的運算，有時我們得到的時間並不會是 年-月-日 時:分:秒 的形式，而是以秒計算的時間戳記 (timestamp) 。如 timestamp 為 1600000000 時，代表的時間是 2020 年 9 月 13日 12 點 26 分 40 秒。


Input
輸入為一行，包含一個整數


Output
輸出為一行，包含一個字串時間


輸入範例 1 
143644473

輸出範例 1
1974-07-21 13:14:33

輸入範例 2 
1600000000

輸出範例 2
2020-09-13 12:26:40

提示
建議使用 datetime 這個模組

來源
ccClub Judge
"""
from datetime import datetime

timestamp = int(input())
dt = datetime.fromtimestamp(timestamp)
formatted_dt = dt.strftime('%Y-%m-%d %H:%M:%S')
print(formatted_dt)
