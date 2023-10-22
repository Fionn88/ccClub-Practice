"""
2-2：偶數
Description

輸入一個數字，如果為偶數輸出 True ，奇數輸出 False。


Input
輸入為一行，包含一個整數。


Output
輸出 True 或是 False


Sample Input 1 
20

Sample Output 1
True

Sample Input 2 
87

Sample Output 2
False

Source
ccClub Judge
"""

s1 = int(input())
if s1 % 2 == 0:
    print(True)
else:
    print(False)
