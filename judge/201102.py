"""
小明查單字

描述
小明最近在寫一個英文字典程式，他希望搜尋欄可以支援前綴(prefix)匹配的功能。
比如當小明在搜尋欄中輸入 c 的時候，顯示開頭為 c 的單字 coding
co-working
club
ccClub
...
你能幫他完成這個功能嗎？

輸入
共有兩行，第一行為複數個單字，用空白隔開
第二行為數個字母所形成的前綴

輸出
印出所有符合前綴的單字，不改變原本的順序，以空白分開

輸入範例 1 
apple microsoft OSX windows good bad approve disprove
app

輸出範例 1
apple approve

輸入範例 2 
innocuous specious conventional rationale iconoclastic
i

輸出範例 2
innocuous iconoclastic

提示
前綴（prefix）
在語言學裡，前綴（英語：Prefix）又稱字首或詞頭，屬於一種前置於其他詞素的詞綴，由於其無法以單字的方式獨立存在，故亦為一種附著詞素；此外在歐洲語言裡，前綴也幾乎都屬於衍生語素（屈折變化則多以後綴表達）。

來源
ccClub Judge
"""

words = input().split()
prefix = input()
res = []
for word in words:
    if len(word) >= len(prefix) and word[0:len(prefix)] == prefix:
            res.append(word)

for ans in res:
      print(ans,end=' ')
    