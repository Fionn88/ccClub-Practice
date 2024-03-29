"""
綜合2-3：計算機

描述
給定一個字串 s，代表希望計算的運算式。內容包含加減乘除四種運算符號（先乘除，後加減）以及數字，數字與運算符號之間皆用一個空格隔開。
請計算運算式 s 的結果，並將其印出，輸出值的型態請使用 float。

輸入
輸入為一行，包含一個字串s

輸出
輸出為一行，包含一個浮點數

輸入範例 1 
0.1 + 0.2 * 0.3 / 0.4

輸出範例 1
0.25

輸入範例 2 
-1.5 + 2.5 - 3 * 4

輸出範例 2
-11.0

來源
ccClub Judge
"""

question = input().split(' ')

while '*' in question or '/' in question:
    for i in range(len(question)):
        if question[i] == '*':
            ans = float(question[i-1]) * float(question[i+1])
            question =  question[:i-1] + [ans] + question[i+2:]
            break
    for i in range(len(question)):
        if question[i] == '/':
            ans = float(question[i-1]) / float(question[i+1])
            question =  question[:i-1] + [ans] + question[i+2:]
            break

while '+' in question or '-' in question:
    for i in range(len(question)):
        if question[i] == '+':
            ans = float(question[i-1]) + float(question[i+1])
            question =  question[:i-1] + [ans] + question[i+2:]
            break
    for i in range(len(question)):
        if question[i] == '-':
            ans = float(question[i-1]) - float(question[i+1])
            question =  question[:i-1] + [ans] + question[i+2:]
            break

print(float(question[0]))
