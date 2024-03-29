"""
二進位
描述

二進位是電腦電腦用來表示數字的方式，請寫一個程式，把給定的數字轉成二進位。

但在這題中，我們希望除了轉二進位之外還有些其他的要求。

備註：這題你需要寫一個名為 to_binary 的函式，並將結果回傳，你不需要自己處理輸入和輸出。


輸入
函式有一個參數 n，為一個十進位的數字。


輸出
回傳值為一個串列，串列中每個元素皆為數字。
你需要將參數 n 轉成二進位後，將連續的 1 和 0 移除掉（只保留一個），並將每個位元都放在串列中（詳細說明請見 hint）。


輸入範例 1
to_binary(16)

輸出範例 1
[1, 0]

輸入範例 2
to_binary(596350)

輸出範例 2
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

提示
sample input 1 中，16 轉為二進位為 10000，去掉連續的 1 和 0 之後為 10，因此需要回傳 [1, 0]。
sample input 2 中，596350 轉為二進位為 10010001100101111110，去掉連續的 1 和 0 之後為 10，因此需要回傳 [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]。

來源
ccClub Judge
"""

def to_binary(n):
    # do something to transfer n to binary, and return your answer
    # ans should be list of integers
    ans = []
    transform = bin(n)
    transform = list(transform[2:])
    for i in transform:
        if ans and i == ans[-1]:
            continue
        else:
            ans.append(i)
            
    return list(map(int,ans))

print(to_binary(16))
