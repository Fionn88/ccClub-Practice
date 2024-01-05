"""
神奇翻譯機

描述
這是一個神祕的翻譯，在輸入完每個詞對應的翻譯詞語以後，就像是我們擁有了一本字典。
在擁有這本字典的情況下，我們可以對任何詞組進行轉換，保證這個這個詞組裡的每個詞都有對應的翻譯詞語。

輸入
第一行為字典字數 n。
第 2 ~ N+1 行為兩個字 source target，為字典當中，翻譯前的詞語對應到翻譯後。
最後一行為由空格分開的詞組，一個詞可能出現多次。

輸出
輸出為翻譯後的詞組，以空格分隔

輸入範例 1 
1
str asdf
str str str str

輸出範例 1
asdf asdf asdf asdf

輸入範例 2 
3
Kevin Wei
Wayne Huang
Toby Lee
Kevin Wayne Kevin Toby Wayne Toby Wayne Kevin Kevin

輸出範例 2
Wei Huang Wei Lee Huang Lee Huang Wei Wei

來源
ccClub Judge
"""

dInt = int(input())
D = {}
for _ in range(dInt):
    dKey,dValue = input().split()
    D[dKey] = dValue

searched = input().split()
for word in searched:
    print(D[word],end=' ')
    