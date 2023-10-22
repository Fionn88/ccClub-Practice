"""
母音子字串
描述

給定一個字串，請找出該字串中，母音個數不變的最短子字串


輸入
輸入為一行，包含一個字串


輸出
輸出為一行，包含一個字串，也就是包含了輸入的字串當中所有母音的最短子字串


輸入範例 1 
app

輸出範例 1
a

輸入範例 2 
java

輸出範例 2
ava

輸入範例 3 
bbcc

輸出範例 3


提示
範例當中：
app 因為母音只有 a ，所以最短的母音子字串是 a
java 因為母音是 index 為 1 的 a 以及 index 為 3 的 a，故最短的母音子字串是 ava
bbcc 因為沒有母音，故最短的母音子字串不存在，此時請使用 print('')

來源
ccClub Judge
"""

word = ['a','e','i','o','u']
s = input()
index = [pos for pos, char in enumerate(s) if char.lower() == 'a' or char.lower() == 'e' or char.lower() == 'i' or char.lower() == 'o' or char.lower() == 'u']
length = len(index)
if length > 1:
    print(s[index[0]:index[-1]+1])
else:
    if length == 0:
        print("")
    else:
        print(s[index[0]])
        