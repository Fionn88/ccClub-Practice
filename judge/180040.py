"""
綜合2-5：計算機 again & again
描述

給定一個字串 s，代表希望計算的運算式。內容包含加減乘除四種運算符號、括號（括號優先，接著先乘除後加減）以及數字，括號、運算符號、數字之間皆用一個空格隔開。

請計算運算式 s 的結果，並將其印出，輸出值的型態請使用 float 浮點數。


輸入
輸入為一行，包含一個字串s


輸出
輸出為一行，包含一個浮點數


輸入範例 1 
-1 / ( ( 2 + 3 ) * 4 - 10 )

輸出範例 1
-0.1

輸入範例 2 
-100 / ( ( 2.5 + 7.5 ) * ( 2 * 2.5 ) )

輸出範例 2
-2.0

來源
ccClub Judge
"""

question = input().split()
queue = []

while len(question) != 1:
  # 處理括號順序

  # 處理加減乘除
  while '*' in question or '/' in question:
      if (question.index("/") if "/" in question else float('Inf')) <  (question.index("*") if "*" in question else float('Inf')):
        for i in range(len(question)):
            if question[i] == '/':
                ans = float(question[i-1]) / float(question[i+1])
                question =  question[:i-1] + [ans] + question[i+2:]
                break
        for i in range(len(question)):
            if question[i] == '*':
                ans = float(question[i-1]) * float(question[i+1])
                question =  question[:i-1] + [ans] + question[i+2:]
                break
      else:
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
      if (question.index("+") if "+" in question else float('Inf')) < (question.index("-") if "-" in question else float('Inf')):
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
      else:
        for i in range(len(question)):
            if question[i] == '-':
                ans = float(question[i-1]) - float(question[i+1])
                question =  question[:i-1] + [ans] + question[i+2:]
                break
        for i in range(len(question)):
            if question[i] == '+':
                ans = float(question[i-1]) + float(question[i+1])
                question =  question[:i-1] + [ans] + question[i+2:]
                break


print(float(question[0]))
