"""
綜合1-4：括號合法

描述
輸入一個字串 s，如果括號組合合法（每一個左括號都對應一個右括號且位置正確），則輸出 True，否則，輸出 False。

輸入
輸入為一行，包含一個字串

輸出
輸出 True 或 False

輸入範例 1 
(()())

輸出範例 1
True

輸入範例 2 
)(

輸出範例 2
False

來源
ccClub Judge
"""

s = input()  # 讀入字串

stack = []  # 儲存左括號的堆疊

# 遍歷字串中的每個字符
for c in s:
    if c == '(':  # 如果是左括號
        stack.append(c)  # 把左括號壓入堆疊中
    elif c == ')':  # 如果是右括號
        if len(stack) > 0 and stack[-1] == '(':  # 如果堆疊不為空且頂部是左括號
            stack.pop()  # 將左括號彈出堆疊
        else:
            print(False)  # 如果上面兩個條件不滿足，則輸出 False
            exit()  # 終止程式

if len(stack) == 0:  # 如果堆疊為空
    print(True)  # 輸出 True
else:
    print(False)  # 否則輸出 False
