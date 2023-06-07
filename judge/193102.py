"""
大小寫互換
描述

輸入一個全大寫或全小寫的字串，如果是全大寫，則把他轉成小寫並輸出，如果是全小寫，則把他轉成大寫並輸出。


輸入
輸入有一行，包含一個字串（必為全大寫或全小寫）。


輸出
輸出有一行，包含一個字串，為轉換為大小寫後的結果。

輸入範例 1
apple

輸出範例 1
APPLE

輸入範例 2 
WTF

輸出範例 2
wtf

來源
ccClub Judge
"""
s = input()
swapped_string = s.swapcase()
print(swapped_string)
