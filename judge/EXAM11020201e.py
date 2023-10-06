"""
學號判斷
描述

台大學號的規則為英文字母開頭，接上八個數字，英文字母代表不同的身份別，前兩位數字代表入學年份。

舉例來說，B89109039 中 B 代表學士班， 89 代表 89 學年度入學。

身份簡易來說可以分成三種， B 代表學士班，R 代表碩士班，D 代表博士班。

請你寫一個程式，判斷該學號同學的年級為何。


輸入
輸入為一個字串，代表一個學號。


輸出
輸出有兩行。

第一行為該學號的身份別。

第二行為該學號的年級（以 110 學年度為基準），年級最多可為七年級。


輸入範例 1 
B08502018

輸出範例 1
學士班
三年級

輸入範例 2 
R10922074

輸出範例 2
碩士班
一年級

輸入範例 3 
D04922047

輸出範例 3
博士班
七年級

提示
題目以 110 學年度為基準：

sample input 1 為 108 學年度入學，故為三年級。
sample input 2 為 110 學年度入學，故為一年級。
sample input 3 為 104 學年度入學，故為七年級。
"""
student_number = input()
level = {'B': '學士班','R':'碩士班','D':'博士班'}
gradeD = {'1': '一年級','2':'二年級','3':'三年級','4':'四年級','5':'五年級','6':'六年級','7':'七年級'}
grade = 110 - int('1' + student_number[1:3]) + 1
print(level.get(student_number[0]))
print(gradeD.get(str(grade)))
