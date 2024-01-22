"""
QAQ

描述
QAQ

輸入
一字串s。

輸出
一數字，為字串s中，QAQ出現的數量。QAQ之間可不連續。

輸入範例 1
QAQAQ

輸出範例 1
4

輸入範例 2
QQAAGAGCAGAGQAGAGCAQ

輸出範例 2
29

提示
第一組測資中有四組QAQ：
QAQAQ
QAQAQ
QAQAQ
QAQAQ
（一般的解法可得15分，較有效率的解法可以拿滿20分。）
"""

# TLE
s = input()
ans = 0
for index,fistCharacter in enumerate(s):
    if fistCharacter != "Q":
        continue
    else:
        for second in range(index+1,len(s)):
            final = second + 1
            if s[second] != "A":
                continue
            while final != len(s):
                if s[final] == "Q":
                    ans += 1
                final += 1
print(ans)
