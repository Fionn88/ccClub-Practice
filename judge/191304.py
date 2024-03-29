"""
雜湊函數
描述

給定一個整數 n 和數個以逗號分隔的整數，請回傳這數個整數對 n 取的餘數。

舉例來說，當 n 為 10，給定的數個整數為 [15, 16, 17, 18]，請回傳 [5, 6, 7, 8]。

然而，有可能出現兩個整數對 n 取到相同的餘數，如果發生這樣的情況，請將取得的餘數加一以後再次對 n 取餘數再放入答案當中。若加一以後取餘數還是遇到該數字已經在答案當中的情況，請繼續加一取餘數直到沒有相同的數字在答案當中為止。


輸入
輸入有兩行，第一行包含一個整數，第二行則是包含數個整數，以逗號分隔


輸出
輸出有一行，包含和輸入第二行相同數量的整數，以逗號分隔


輸入範例 1 
10
15,16,17,18

輸出範例 1
5,6,7,8

輸入範例 2 
5
1,6,11,16

輸出範例 2
1,2,3,4

來源
ccClub Judge
"""

n = int(input())
lst = list(map(int,input().split(',')))
ans = []
for i in lst:
    temp = i % n
    while temp in ans:
        temp += 1
        temp %= n  
    ans.append(temp)

ans = list(map(str, ans))
print(','.join(ans))
    