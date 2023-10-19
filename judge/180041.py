"""
綜合2-6：合法括號窮舉
描述

我們定義 () 為一組括號。

給定一個正整數 n ，代表有 n 組括號，請輸出所有合法的括號組合形成的字串。每種組合之間用換行字元 \n 隔開。輸出時，左括號優先，再來才是右括號。

舉例來說，n = 2 時，(())在()() 前面。


輸入
輸入為一行，包含一個正整數


輸出
輸出為數行，每行皆包含由 n 個合法括號組合而成的字串


輸入範例 1
2

輸出範例 1
(())
()()

輸入範例 2
4

輸出範例 2
(((())))
((()()))
((())())
((()))()
(()(()))
(()()())
(()())()
(())(())
(())()()
()((()))
()(()())
()(())()
()()(())
()()()()

來源
ccClub Judge
"""
def generate_valid_parentheses(n):
    def backtrack(combination, left, right):
        if len(combination) == 2 * n:
            combinations.append(combination)
            return
            
        if left < n:
            backtrack(combination + '(', left + 1, right)
        if right < left:
            backtrack(combination + ')', left, right + 1)

    combinations = []
    backtrack('', 0, 0)
    return combinations

n = int(input())
valid_parentheses = generate_valid_parentheses(n)

for p in valid_parentheses:
    print(p)