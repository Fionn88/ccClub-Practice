"""
字串回文
描述

給定一個字串，若這個字串在經過任意重組以後（包含不變的情況），能成為一個回文字串請輸出 True，否則請輸出 False。


輸入
輸入為一行，包含一個字串


輸出
輸出為一行，為 True 或是 False


輸入範例 1
aab

輸出範例 1
True

輸入範例 2 
abc

輸出範例 2
False

來源
ccClub Judge
"""

import collections

s = input()
countS = collections.Counter(s)
tag = True
if len(s) % 2 == 0:
    for value in countS.values():
        if value % 2 != 0:
            tag = False
else:
    count = 0
    for value in countS.values():
        if value % 2 != 0:
            count += 1
    if count != 1:
        tag = False
print(tag)
