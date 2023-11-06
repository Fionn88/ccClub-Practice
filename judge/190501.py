"""
數字組合最大值
描述

請寫出一個函式，參數是一個數字，型態是整數。而回傳值是該數字各位數重新排列可以排出來的最大值，型態為整數。


輸入
參數有一個，包含一個整數


輸出
回傳值有一個，包含一個整數


輸入範例 1 
max_sort_num(539)

輸出範例 1
953

輸入範例 2 
max_sort_num(7862)

輸出範例 2
8762

來源
ccClub Judge
"""

def max_sort_num(num):
        
    # do something to calculate parking fee
    num = str(num)
    
    return ''.join(sorted(num, reverse=True))
