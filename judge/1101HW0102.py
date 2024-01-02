"""
小仔算GPA

描述
小仔上學期選了三門課，老師們都已經上傳成績，但系統好像壞掉了沒有幫他算出平均 GPA，題目給定三堂課的成績與學分數，請你利用下圖幫他算出他學期平均 GPA 吧！（計算無條件捨去到小數點後第二位）

====
請至 judge 查看圖片
====

輸入
輸入總共 6 行，
每 2 行的輸入，
第一行包含一字串，為學門成績等第(不會有 X 的情況)
第二行包含一整數，為上一行學門的學分數，
以此類推

輸出
輸出包含一浮點數

輸入範例 1 
A+
3
A+
5
A+
2

輸出範例 1
4.30

輸入範例 2 
A
2
A-
3
C+
3

輸出範例 2
3.25
"""

# 三堂課的(一堂的等第積分 * 一堂的學分數) / 三堂課的(學分數)
D = {"A+":4.3,"A":4.0,"A-":3.7,"B+":3.3,"B":3.0,"B-":2.7,"C+":2.3,"C":2.0,"C-":1.7,"F":0}
credit = 0
weighted_grade = 0
for i in range(3):
    grade = D[input()]
    weight = int(input())
    credit += weight
    weighted_grade += weight * grade
avg = weighted_grade / credit
str_avg = str(avg)[:4]
print(f"{float(str_avg):.2f}")
