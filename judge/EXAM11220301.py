"""
阿偉包禮物

描述
阿偉是禮品部門作業員，輸送帶有一串禮物，但今天店長忘了告訴阿偉要包成幾份。阿偉只能從禮物的排列大致推估。
禮物依序出現，每份禮物需要有一樣的內容物，請幫阿偉找出可以包出最多份的禮物組合吧。

輸入
輸入為一串長度不定的字串

輸出
輸出要求兩個資訊，分別為
'最多禮物份數', '每份禮物數量'

輸入範例 1
123123123123

輸出範例 1
4, 3

輸入範例 2
AAAAAAAA

輸出範例 2
8, 1
"""

# Partial Accepted
s = input()
temp = ""
seen = set()
for element in s:
    if element not in seen:
        seen.add(element)
        temp += element
    else:
        break

s = s.split(temp)

print(str(len(s) - 1) + ",", len(seen))
