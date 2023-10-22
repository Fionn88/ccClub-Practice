"""
數字數
描述

給定一段文章，請計算當中包含的單字數和字母數，空白不計。


輸入
輸入為一段文章，單字間以空白分開，可能包含標點符號。


輸出
輸出第一行為單字數（意即該文章由幾個單字組合而成，同一單字出現複數次也以複數次計算，不理會標點符號）
輸出第二行為字母數（意即該文章由幾個字母所組成，計算字母個數）


輸入範例 1 
Hi kevin!

輸出範例 1
2
7

輸入範例 2 
Hello, world!

輸出範例 2
2
10

來源
ccClub Judge
"""

s = input().split()
word = 0
for i in s:
    for j in i:
        if j.isalpha():
            word += 1
print(len(s))
print(word)
