"""
3-1：字串長度
Description

輸入一個字串s以及一個數字n，如果字串 s 的長度恰好為 n 則輸出 True，否則，輸出 false。


Input
輸入為兩行，第一行為字串 s，第二行為數字 n。


Output
輸出True或False


Sample Input 1 
Apple
5

Sample Output 1
True

Sample Input 2 
Python
7

Sample Output 2
False

Source
ccClub Judge
"""

s = input()
n = int(input())
if len(s) == n:
    print(True)
else:
    print(False)
    