"""
帕斯卡三角形
描述

輸入一個正整數 n ，請輸出一個 n 層的帕斯卡三角形。


輸入
輸入有一行，為一個正整數


輸出
輸出為一個串列，串列中的元素為 n 個串列，第 i 個串列表在帕斯卡三角形中的第 i 層


輸入範例 1 
1

輸出範例 1
[[1]]

輸入範例 2 
5

輸出範例 2
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

提示
關於帕斯卡三角形 (Pascal's triangle) 的規則與介紹，歡迎參考這篇
"""

num = int(input())
ans = []
prev_row = []
for n in range(num):
    curr_row = [1]  # 每一行的開頭都是1
    if prev_row:  # 如果前一行存在
        for i in range(len(prev_row) - 1):
            curr_row.append(prev_row[i] + prev_row[i + 1])  # 根據前一行生成當前行
        curr_row.append(1)  # 每一行的结尾也是1
    ans.append(curr_row)
    
    prev_row = curr_row  # 更新前一行
print(ans)
