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
