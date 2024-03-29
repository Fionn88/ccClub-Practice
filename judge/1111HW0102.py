"""
阿偉當助教 II

描述
承上題，阿偉登記小寫字母表示發言一次加一分，若是登記大寫字母表示發言內容很有價值加兩分。
老師一共有四個指令：
若輸入'\'表示已經加分的同學通通分數加倍
若輸入'/'表示已經加分的同學通通再加一分
若輸入'@'表示上一個發言同學回答該題的分數加倍
若輸入'?'表示上一個發言同學回答錯誤，酌扣一分，不論上一次是加一分還是兩分
已知'?'和'@'不出現在第一個字，且'?'和'@'不連續出現(不會出現'??'... 等狀況)，若前面為符號則再往前找到第一個出現的字母進行指令。
此外記錄已經加分的同學時，不算入被扣到變成 0 分的同學。
請幫阿偉算出所有人的成績吧。

輸入
輸入只有 1 行，出現的字有可能是英文字或特殊符號。長度不定。

輸出
輸出為一個 list
第一個 list 紀錄每個人的分數，形式為[['小寫字母', 分數], ...]。按照字母序排序，若那個人總和分數為 0 則不印出。
若上述 list 為空則印None。

輸入範例 1
slxdvlGTFVBczlrvgwn\hqv//csuaei?

輸出範例 1
[['a', 1], ['b', 6], ['c', 5], ['d', 4], ['e', 1], ['f', 6], ['g', 8], ['h', 3], ['l', 8], ['n', 4], ['q', 3], ['r', 4], ['s', 5], ['t', 6], ['u', 1], ['v', 11], ['w', 4], ['x', 4], ['z', 4]]

輸入範例 2
\\//

輸出範例 2
None
"""

from collections import defaultdict

def zero():
    return 0

ansD = defaultdict(zero)
s = list(input())
ansCharList = []
for index in range(len(s)):
    if s[index].isalpha():
        if s[index].islower():
            ansD[s[index]] += 1
        else:
            ansD[s[index].lower()] += 2
    else:
        tag = False
        if ansD:
            if s[index] == "\\":
                for key,value in ansD.items():
                    if value > 0:
                        ansD[key] += ansD.get(key)
            elif s[index] == "/":
                for key,value in ansD.items():
                    if value > 0:
                        ansD[key] += 1
            elif s[index] == "@":
                while not s[index].isalpha():
                    index -= 1
                    if index == -1:
                        tag = True
                        break
                if not tag:
                    if s[index].islower():
                        ansD[s[index]] += 1
                    else:
                        ansD[s[index].lower()] += 2
            elif s[index] == "?":
                while not s[index].isalpha():
                    index -= 1
                    if index == -1:
                        tag = True
                        break
                if not tag:
                    ansD[s[index].lower()] -= 1

for key,value in ansD.items():
    if value > 0:
        ansCharList.append([key,value])
if ansCharList:
    print(sorted(ansCharList, key=lambda x: x[0]))
else:
    print(None)
