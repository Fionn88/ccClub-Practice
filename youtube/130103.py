"""
[13-1] 詞頻計算
Description

強強想要計算一個文本中各個詞彙出現的次數，所以他想要寫一個程式，你可以幫他寫嗎？


Input
輸入為 1 + n 行，第 1 行為句子數，後面 n 行皆為一個斷好詞的句子，詞彙之間以空白分隔。


Output
輸出為 1 行，為字典中的內容。


Sample Input 1 
3
不要 重複 造 輪子
檔 不可以 沒有 註解
Keep It Simple and Stupid

Sample Output 1
{'不要': 1, '重複': 1, '造': 1, '輪子': 1, '檔': 1, '不可以': 1, '沒有': 1, '註解': 1, 'Keep': 1, 'It': 1, 'Simple': 1, 'and': 1, 'Stupid': 1}

Sample Input 2 
2
9487 94 狂
0 0 0 0 0 1

Sample Output 2
{'9487': 1, '94': 1, '狂': 1, '0': 5, '1': 1}

Source
ccClub Judge
"""
n = int(input())
sentence = []
for i in range(n):
    sentence.append(input().split())

d = {}

for i in sentence:
    for word in i:
        if word not in d:
            d[word] = 1
#             ___________
        else:
            count = d.get(word)
            count += 1
            d[word] = count
#             ____________

print(d)
