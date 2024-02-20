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

# Wrong Transfer
def infix_to_postfix(expression):
    def precedence(op):
        precedences = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        return precedences.get(op, 0)

    output = []
    stack = []
    for char in expression:
        if char.isalnum():  # Operand
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Pop '(' from stack
        else:  # Operator
            while stack and precedence(char) <= precedence(stack[-1]):
                output.append(stack.pop())
            stack.append(char)
    
    while stack:
        output.append(stack.pop())
    
    return ''.join(output)

n = input().replace(" ","")
postfix_expr = infix_to_postfix(n)
print(postfix_expr)

