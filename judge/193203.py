"""
二進位 II
描述

承上題（二進位），我們希望改變函式的功能。

備註：這題你需要寫一個名為 to_binary 的函式，並將結果回傳，你不需要自己處理輸入和輸出。


輸入
函式有一個參數 n，為一個十進位的數字。


輸出
回傳值為一個串列，串列中每個元素皆為數字。

你需要將參數 n 轉成二進位後，若有連續的 1 和 0 需要計算連續的次數，最後把結果放在串列中（詳細說明請見 hint）。


輸入範例 1
to_binary(27)

輸出範例 1
[1, 2, 0, 1, 2]

輸入範例 2 
to_binary(330)

輸出範例 2
[1, 0, 1, 0, 2, 1, 0, 1, 0]

提示
sample input 1 中，27 轉為二進位為 11011，一開始有連續兩個 1 ，因此處理過後會是 [1, 2] 代表 1 出現兩次，接下來是一個 0，串列變成 [1, 2, 0]，接著是連續兩個 1 ，處理過後串列變為 [1, 2, 0, 1, 2]，最後回傳 [1, 2, 0, 1, 2]。
sample input 2 中，330 轉為二進位為 101001010，前面的 101 分別都只出現一次，因此處理過後串列為 [1, 0, 1]，接下來有連續兩個 0，因此串列變為 [1, 0, 1, 0, 2]，接著是 1010，因此串列又變成 [1, 0, 1, 0, 2, 1, 0, 1, 0]，最後回傳 [1, 0, 1, 0, 2, 1, 0, 1, 0]。

來源
ccClub Judge
"""

def to_binary(n):
    transform = bin(n)
    binary = transform[2:]
    result = []
    count = 1
    for i in range(len(binary)):
        if i == 0:
            result.append(binary[i])
        elif binary[i] == binary[i-1]:
            count += 1
        else:
            if count > 1:
                result.append(count)
                result.append(binary[i])
                count = 1
            else:
                result.append(binary[i])
    if count > 1:
        result.append(count)

    return [int(i) for i in result]

# If the code is correct, it should print:
# [1, 2, 0, 1, 2]
# [1, 0, 1, 0, 2, 1, 0, 1, 0]

# print(to_binary(27))
# print(to_binary(330))
