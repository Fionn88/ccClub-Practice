"""
醜數

描述
醜數就是因數裡面只含有 2、3 和 5 的數（不包含 1 以及自己）
比方說6的因數只含有 2、3，所以他就是醜數（一般來說 1 被我們特別歸類在醜數）
而 14 的因數含有 7 所以不是醜數

輸入
輸入為一正整數

輸出
輸出為 True 或是 False，取決於他是不是醜數

輸入範例 1 
6

輸出範例 1
True

輸入範例 2 
1

輸出範例 2
True

輸入範例 3 
14

輸出範例 3
False
"""

n = int(input())
x = n
while x >= 1:
    x = x / 4

y = n
while y >= 1:
    y = y / 2


z = n
while z >= 1:
    z = z / 5


fac = [] 
for i in range(2, n):
    if n % i == 0:
        fac.append(i) 
    else:
        pass

if n == 1:
    print(True)
else:
    for i in fac:
        if i == 2 or i == 3 or i == 5:
            output = True
        else:
            output = False
            break
    print(x == 0.25 or y == 0.5 or z == 0.2 or output)
    