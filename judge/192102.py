"""
圈圈叉叉
描述

請判斷 3*3 棋盤上的三個棋子是否連成一線。

棋盤上的空位由左至右，如圖，由上至下為 1～9，題目的輸入為 1～9 其中三個數字，由小至大排序。若連成一線請輸出 T，否則輸出 F。

| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |


輸入
輸入包含三個數字，由小到大，以空白為間隔


輸出
輸出為一行，包含一個字元（T 或是 F）


輸入範例 1 
 1 2 3

輸出範例 1
T

輸入範例 2 
1 2 9

輸出範例 2
F

來源
ccClub Judge
"""

i,j,k = map(int,input().split())
if i + 1 == j and j + 1 == k:
    print("T")
elif i + 3 == j and j + 3 == k:
    print("T")
elif i + 4 == j and j + 4 == k:
    print("T")
elif i == 3 and j == 5 and k == 7:
    print("T")
else:
    print("F")
