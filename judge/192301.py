"""
字串合併
描述

給定兩個字串s1和s2，請把兩個字串交叉合併在一起。

s1在前，s2在後，若兩者長度不一，長度超過的部分請直接加在字串後面。


輸入
輸入包含兩行，第一行為s1，第二行為s2，皆為字串


輸出
輸出為一行，包含一個字串


輸入範例 1 
UTLzEFl
rzNO

輸出範例 1
UrTzLNzOEFl

輸入範例 2 
CQeY
eANBXaRb

輸出範例 2
CeQAeNYBXaRb

來源
ccClub Judge
"""

s1 = input()  
s2 = input()  

merged_string = ''.join([x + y for x, y in zip(s1, s2)])

if len(s1) > len(s2):
    merged_string += s1[len(s2):]
elif len(s2) > len(s1):
    merged_string += s2[len(s1):]

print(merged_string)
