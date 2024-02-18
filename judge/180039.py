"""
綜合2-4：計算機 again

描述
給定一個字串 s ，代表希望計算的運算式。內容包含加減乘除四種運算符號（由左至右，先乘除，後加減）以及數字，數字與運算符號之間可能有「數個空格」或「沒有空格」。
請計算運算式 s 的結果，並將其印出，輸出值的型態請使用 float 浮點數。

輸入
輸入為一行，包含一個字串s

輸出
輸出為一行，包含一個浮點數

輸入範例 1 
-1.5 +-2.5 *   -3.5 /2

輸出範例 1
2.875

輸入範例 2 
   -1     --3.5/   2
   
輸出範例 2
0.75

來源
ccClub Judge
"""

def parse_expression(expression):
    result = []
    number = ''
    for i, char in enumerate(expression):
        if char.isdigit() or char == '.':
            number += char
        elif char == '-' and (i == 0 or expression[i-1] in '+-*/'):
            # If a minus sign is the first character or follows another operator, it's part of a negative number.
            number += char
        else:
            if number:
                result.append(number)
                number = ''
            result.append(char)
    
    # Add the last number to the result, if any
    if number:
        result.append(number)
    
    return result

question = input().replace(" ","")
question = parse_expression(question)


# 加減乘除 依然有順序性
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
