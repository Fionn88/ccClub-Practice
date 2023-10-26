"""
消失的號碼
描述

給定一串隨意排列的數列，請你找出不在數列中的最小正整數。
提示：數列中的數字不會重複


輸入
輸入有一行，為一個整數數列。


輸出
輸出有一行，請輸出不在數列中的最小正整數。


輸入範例 1 
4 3 1 7 -1 2 8

輸出範例 1
5

輸入範例 2 
-3 -2 -8 0 -4

輸出範例 2
1
"""

n = list(map(int,input().split()))
n.sort()

if n[0] > 1:
    print(1)
    exit()

l,r = 0,1
flag = False
while r < len(n):
    if n[l]+1 != n[r]:
        if n[l]+1 < 1:
            pass
        else:
            print(n[l]+1)
            flag = True
            break
    l += 1
    r += 1

if not flag:
    print(n[-1]+1)
