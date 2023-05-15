"""
台灣大公園
描述

由於五寒肺炎的關係，臺灣大公園決定對遊客進行管制。 管制辦法以及流程如下：
管理處會先訂出數字 M 以及數字 N，數字 M 代表台灣大公園目前開放的區域數量，而數字 N 則是代表管理處開放讓一個遊客可以遊覽的區域數量。
接著會公布這 M 個區域目前已經入場的遊客數量，再讓遊客提出想要遊覽的區域願望清單。
在遊客提出的願望清單當中，會由管理處分配目前入場人數較少的 N 個區域給該遊客遊覽，排列方式由目前來客數少的區域排列到多的區域。
請寫一個程式幫助管理處分配遊客遊覽區域。


輸入
輸入包含 M + 3 行：
第一行包含一個整數 M，代表所開放的區域數量。
第二至 M + 1 行則各包含一個字母以及一個整數，以空白分隔，代表這 M 個區域目前所在的人數。
第 M + 2 行包含數個字母，代表該遊客想要遊覽的願望清單。
第 M + 3 行則是包含一個整數 N，代表可以開放給該遊客遊覽的區域數量。


輸出
輸出為一行，包含數個字母，為管理處提供給該遊客的遊覽區域順序


輸入範例 1 
3
A 1
B 2
C 3
B C
1

輸出範例 1
B

輸入範例 2 
6
Y 20
F 50
M 49
X 13
S 28
O 96
S Y X
3

輸出範例 2
X Y S

來源
ccClub Judge
"""
def people_sort(s):
    return int(s[1])

M = int(input())
complete_list = [input().split() for i in range(M)]
wish_list = input().split()
N = int(input())

complete_list.sort(key=people_sort)
filtered_list = [item for item in complete_list if item[0] in wish_list]

for i in range(N):
    if i == N - 1:  
        print(filtered_list[i][0])
    else:
        print(filtered_list[i][0], end=' ')

    