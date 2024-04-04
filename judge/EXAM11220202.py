"""
阿偉點技能樹

描述
阿偉是一個遊戲玩家，該遊戲有26個技能樹，分別對應26個字母。阿偉的目標是成為平均發展的26邊形戰士。
最近阿偉打怪得到了一串技能卷軸，捲軸上的字母代表獲得的技能，大小寫字母代表相同的技能。迫於資源有限，他需要決定技能的發展順序，規則為由點的少的技能優先於點的多的技能，若順位相同則由A到Z點技能，請幫阿偉排序出適合的點技能順序。

輸入
輸入為一串字串，字串內僅有英文字母，但大小寫、長度不等。

輸出
輸出為一個元素僅有大寫字母的list，依上述規定順序排序

輸入範例 1
AbacCbZ

輸出範例 1
['A', 'B', 'C', 'Z', 'A', 'B', 'C']

輸入範例 2
TheQuickBrownFoxJumpsOverTheLazyDog

輸出範例 2
['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'E', 'H', 'O', 'R', 'T', 'U', 'E', 'O', 'O']

提示
以Sample 1為例
AbacCbZ 整理後為 A A B B C C Z
點完A之後會優先點沒點過的B C Z
若所有技能的等級皆相同，如上述已點完A B C Z
目前已點技能皆為1級，就繼續往A的2級開始點。
"""

# TLE
n = sorted(input().upper())
ans = [-1]
indices_to_delete = []

while n:
    # 遍歷整個 list
    for char in n:
        # 如果上一個元素，跟這次的相同則跳過
        if ans[-1] == char:
            continue
        else:
            # 加入 ans list 也加入待刪除名單
            ans.append(char)
            indices_to_delete.append(char)
    # 遍歷待刪除名單，並把 n 裡的特定元素刪掉
    for i in indices_to_delete:
        # 如果為 -1 則跳過
        if i == -1:
            continue
        n.remove(i)
    # 初始化待刪除名單
    indices_to_delete = []

# 刪除掉 -1
del ans[0]
print(ans)
