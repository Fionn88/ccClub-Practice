"""
佛心公司

描述
喵喵健身房最近要舉辦活動，老闆喵球打算找出最適合的會員，免費帶他們上減重課程，以作為未來的宣傳材料。
現有數筆會員資料，記載該會員的身高、體重、有無心血管疾病、入會時間（單位：月）。
喵球希望依據所有會員的資料排序，找出活動的優先參與者。
排序的依據如下（若相同則比較下一個條件）：
1. 入會時間在一個月以上、一年以下者優先
2. bmi（數字高的人在前面）
3. 體重 - 身高 （數字大的在前面）
4. 有心血管疾病的優先
5. 入會時間長的優先
請你幫喵球排出名單的順序。

輸入
有 N+1 行，第一行是資料的筆數。第 2 ~ N+1 行則是會員的資料，內容分別是身高、體重、有無心血管疾病（0 表示無、1 表示有）、入會時間，以空白分隔。

輸出
輸出為一行，為輸入之會員資料的 index，以空白分隔。

輸入範例 1
5
170 65 0 20
184 100 1 18
170 65 1 15
157 82 1 3
164 55 0 35

輸出範例 1
3 1 2 0 4

輸入範例 2
4
190 150 0 0
190 150 0 3
177 90 1 16
180 87 0 10

輸出範例 2
1 3 0 2
"""


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed

def timing(listData):
    ans = []
    for index,month in enumerate(listData):
        if 1 <= month <= 12:
            ans.append(index)
    return ans

def dataHigh(listData):
    sorted_pairs = sorted(enumerate(listData), key=lambda x: x[1], reverse=True)
    sorted_indices = [index for index, value in sorted_pairs]
    return sorted_indices

def diseasePriority(listData):
    ans = []
    for index,data in enumerate(listData):
        if data == 1:
            ans.append(index)

    return ans

n = int(input())
allData = []
for index in range(n):
    tall, weight, disease, time = map(int,input().split())
    allData.append([time,weight/tall*tall,weight-tall,disease])

transpose_list = transpose_matrix(allData)
priority = []


# 排序，如遇到相同情況要繼續往下比較，該怎麼做會如何比較有效率。
first = timing(transpose_list[0])
if len(first) == 1:
    priority.append(first[0])

second = dataHigh(transpose_list[1])
third = dataHigh(transpose_list[2])
forth = diseasePriority(transpose_list[3])
fifth = dataHigh(transpose_list[0])
print(first)
print(second)
print(third)
print(forth)
print(fifth)
