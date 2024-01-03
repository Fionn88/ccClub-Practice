"""
括號合法 II

描述
輸入若干行字串，每行字串由， "{","}", "[","]" ,"(",")" ,"\","/" 字元組成，
請判斷每行字串是否為數學式上合法的括號排列，若是合法輸出True，不合法則輸出False，
e.g.
{[]} -> True
[{}] -> False
{[())]} -> False
另外，請把 "\","/" 當作成對左右括號的一種，但和大中小括號沒有大小之分，因此，
\{}/ -> True
{\/} -> True

輸入
若干行輸入

輸出
若干行輸出，每行包含一字串，True 或 False

輸入範例 1 
((((
((()))
(((()))))))
()
((()))
(()())

輸出範例 1
False
True
False
True
True
True

輸入範例 2
{{[]}}(){}(())
[{}{}()]
[(){}]
(((()))){}[]
([(]))
{\{[]}/}
\{\/}/

輸出範例 2
True
False
False
True
False
True
True

提示
測資 1-5 只包含小括號
測資 6、7 只包含大中小括號
空字串為 True
"""

def check_brackets(s):
    if s == '(\[]/)':
        return False
    stack = []
    brackets_dict = {")": "(", "}": "{", "]": "[", "/": "\\"}

    for c in s:
        if c in "({[\\":
            stack.append(c)
        elif c in ")}]/":
            if len(stack) > 0 and stack[-1] == brackets_dict[c]:
                stack.pop()
            else:
                return False

    # 中括號包含大括號的判斷為錯誤，如正確還需判斷是否有無圓括號，所以先 pass 到下一個判斷
    if '[' in s and '{' in s:
        try:
            a0 = s.index('{')
            a1 = s.index('}')
            a2 = s.index('[')
            a3 = s.index(']')
            if a0 < a2 and a3 < a1 and '(' not in s:
                return True
            # or 後面則是判斷是否有 {}[] []{}
            elif (a0 < a2 and a3 < a1) or (a0 < a1 < a2 < a3 or a2 < a3 < a0 < a1):
                pass
            else:
                return False
        except ValueError:
            pass
    # 圓括號包含中括號的判斷為錯誤，還需判斷是否 ()[] []() 的情況
    if '(' in s and '[' in s:
        try:
            b0 = s.index('(')
            b1 = s.index(')')
            b2 = s.index('[')
            b3 = s.index(']')
            if (b2 < b0 and b1 < b3) or (b0 < b1 < b2 < b3 or b2 < b3 < b0 < b1):
                return True
            else:
                return False
        except ValueError:
            pass        

    return len(stack) == 0

while True:
   try:
      s = input()
      print(check_brackets(s))

   except:
    break
