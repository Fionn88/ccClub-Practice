"""
數字三角形

描述
輸入一個正整數 n ，輸出 n 層的數字三角形。

輸入
輸入有一行，包含一個正整數n。

輸出
輸出有 n 行，會組成一個數字三角形。

輸入範例 1 
3

輸出範例 1
1
23
456

輸入範例 2 
7

輸出範例 2
1
23
456
7890
12345
678901
2345678

來源
ccClub Judge
"""

n = int(input())
num = 1   
for i in range(n):
    for j in range(i+1):
        print(num, end='')
        num += 1    
        if num > 9:   
            num = 0
    print()
