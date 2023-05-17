"""
數字交換最大值
描述

給定一個非負整數 N，你可以將任兩個位數的值交換。

請寫一個程式，計算出應該怎樣交換能使交換後的數字最大。


輸入
輸入有一行，包含一個非負整數 N。


輸出
輸出有一行，包含一個非負整數。


輸入範例 1 
9876

輸出範例 1
9876

輸入範例 2 
3578

輸出範例 2
8573

輸入範例 3 
102030405060708090

輸出範例 3
902030405060708010

來源
ccClub Judge
"""


# def swap_nums(num):
#   s = list(str(num))
#   hash_map = {digit:idx for idx,digit in enumerate(s)}
#   for idx, digit in enumerate(s):
#     for number in range(9, int(digit),-1):
#       temp_str = str(number)

#       if temp_str in hash_map and hash_map[temp_str] > idx:
#         s[idx], s[hash_map[temp_str]] = s[hash_map[temp_str]],s[idx]
#         return int(''.join(s))
#   return int(num)
# num = input()
# res = swap_nums(num)
# print(res)

# ==================================== 使用雙指標 ====================================

n = input()
l_idx, r_idx = -1, -1 
max_idx, max_val = -1, ''

for i in range(len(n)-1, -1, -1):
    if n[i] > max_val:
        max_idx, max_val = i, n[i]
        
    elif n[i] < max_val: 
        l_idx, r_idx = i, max_idx

if l_idx == -1:
    print(n)
else:
    n = list(n)
    n[l_idx], n[r_idx] = n[r_idx], n[l_idx]
    print(''.join(n))
