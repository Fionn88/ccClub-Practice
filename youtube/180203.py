"""
字母三角形
描述

輸入一個正整數 n ，輸出 n 層的字母三角形。


輸入
輸入一個正整數 n ，輸出 n 層的字母三角形。


輸出
輸出有 n 行，會組成一個字母三角形。


輸入範例 1 
3

輸出範例 1
A
BC
DEF

輸入範例 2 
8

輸出範例 2
A
BC
DEF
GHIJ
KLMNO
PQRSTU
VWXYZAB
CDEFGHIJ

來源
ccClub Judge
"""
n = int(input())
num = ord('A')    
for i in range(n):
    for j in range(i+1):
        print(chr(num), end='')
        num += 1    
        if num > ord('Z'):   
            num = ord('A')
    print()
