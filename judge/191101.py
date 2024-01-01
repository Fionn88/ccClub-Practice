"""
檢查密碼

描述
為了使用者帳戶安全，我們會檢查使用者的密碼是否包含數字和英文字母。

輸入
輸入為一行，包含一個字串。

輸出
輸出為一行，若密碼中是數字和英文字母的組合，則輸出 True。否則，輸出 False。


輸入範例 1 
abc123

輸出範例 1
True

輸入範例 2 
ccClub

輸出範例 2
False

輸入範例 3 
3345678

輸出範例 3
False

輸入範例 4 
qefjo382+&3219@

輸出範例 4
False

來源
ccClub Judge
"""

s = input()
j = 0
alpha = False
digit = False
for i in s:
  if i.isdigit():
    j += 1
    digit = True
  if i.isalpha():
    j += 1
    alpha = True
  
print(j == len(s) and digit and alpha)
