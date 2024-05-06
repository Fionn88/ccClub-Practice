"""
阿偉連連看

描述
阿偉是五歲小孩，他拿著哥哥的英文生字本亂連一通，意外發現某些字的字母可以形成一對一的連線
如 title 和 paper 的結構完全相同，可以將 t 連至 p， i連至 a， l連至 e， e連至 r 。
阿偉立刻發現這是一對一的函數映射轉換，於是決定找尋其他單字的映射關係，哥哥的生字本今晚難逃一劫。
給定兩個詞，請幫阿偉給出他們的映射關係。

輸入
輸入為兩行長度不定的字串，大小寫視為不同字樣。
字串一為 s ，字串二為 t

輸出
若兩字串無法成功一對一映射，請回傳
False
若可以成功映射，請回傳依字元序排序後， s 至 t 的映射，格式如下
[('s的字元1', 't的字元1'), ('s的字元2', 't的字元2'), ...]

輸入範例 1
title
paper

輸出範例 1
[('e', 'r'), ('i', 'a'), ('l', 'e'), ('t', 'p')]

輸入範例 2
apple
banana

輸出範例 2
False

輸入範例 3
APPLE1
apple2

輸出範例 3
[('1', '2'), ('A', 'a'), ('E', 'e'), ('L', 'l'), ('P', 'p')]
"""

def check_unique_first_elements(lst):
    seen = set()
    for tup in lst:
        if tup[0] in seen:
            return False
        seen.add(tup[0])
    return True

s = input()
t = input()
res = []
if len(set(s)) == len(set(t)):
    for i, j in zip(s,t):
        res.append((i,j))
    ans = sorted(list(set(res)))
    if not check_unique_first_elements(ans):
        print(False)
    else:
        print(ans)
else:
    print(False)
