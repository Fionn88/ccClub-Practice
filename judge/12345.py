"""
換座位

描述
小明是二年甲班的班長，在班會的時候被老師指派要協助同學換座位
班上同學七嘴八舌提議不同的方法，正當他在苦思的時候，突然撇見牆壁上的時鐘
靈機一動的他想要請全班同學從現在的座位一起按照順時鐘的方向轉動一次
請幫忙小明重新安排座位吧！

輸入
輸入為有 n+1 行
第一行為一正整數，表示陣列的大小
第二行到第 n+1 行為一串正整數，分別為學生的座號，用逗號區隔

輸出
輸出為 n 行
每行為一串正整數，分別為調整後的學生座號，用逗號區隔

輸入範例 1 
3
1,2,3
4,5,6
7,8,9

輸出範例 1
7,4,1
8,5,2
9,6,3

輸入範例 2 
4
5,1,9,27
2,4,8,11
13,3,6,7
15,14,12,16

輸出範例 2
15,13,2,5
14,3,4,1
12,6,8,9
16,7,11,27
"""

def transpose_matrix(a):
    row = len(a)
    for i in range(row):
        for j in range(i+1,row):
            a[i][j],a[j][i] = a[j][i],a[i][j]
    return a

n = int(input())
res = []
for _ in range(n):
    sit = input().split(',')
    res.append(sit)

res.reverse()
for i in transpose_matrix(res):
    print(','.join(i))

# Another Solution
n = int(input())
matrix = [list(map(int, input().split(','))) for _ in range(n)]
rotated_matrix = list(zip(*reversed(matrix)))

for row in rotated_matrix:
    print(','.join(map(str, row)))
