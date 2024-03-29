"""
數字最小值排列

描述
輸入一個正整數，請將數字重新排列後，輸出數值最小的數。

輸入
輸入為一行，為一個正整數。

輸出
輸出為一行，為一個正整數。

輸入範例 1 
98765

輸出範例 1
56789

輸入範例 2 
43210

輸出範例 2
10234

輸入範例 3 
100000000000000

輸出範例 3
100000000000000

提示
0 不能放在數字首位
讀取輸入值時，嘗試使用最適合的型態（ex: int, str）讓實作上變得更簡單

來源
ccClub Judge
"""

n = input()
n = sorted(n)
swapIndex = n.index(next(filter(lambda x: x!='0', n)))
for index,value in enumerate(n):
    if index == 0 and value == '0':
        n[0], n[swapIndex] = n[swapIndex], n[0]

for i in n:
    print(i, end='')
