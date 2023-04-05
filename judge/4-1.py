"""
4-1：密碼強度
Description

很多網站對於密碼強度是有要求的，考量資訊安全，太短的密碼是不被允許的。

輸入一個密碼s，如果大於（含）八碼，則輸出 Success，否則輸出 Fail。


Input
輸入為一行，包含一個字串 s


Output
輸出為 Success 或 Fail


Sample Input 1 
Password

Sample Output 1
Success

Sample Input 2 
zxcvbnm

Sample Output 2
Fail

Source
ccClub Judge
"""

s = input()
if len(s) >= 8:
    print("Success")
else:
    print("Fail")