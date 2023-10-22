"""
4-2：及格分數
Description

輸入一個成績n，如果 60（含）以上，則輸出 Pass，不到 60 ，則輸出 Fail，若小於 0 或大於 100，則輸出 Error。


Input
輸入為一行，包含一個整數n


Output
輸出為一行，內容為 Pass 、 Fail  或  Error 


Sample Input 1 
59

Sample Output 1
Fail

Sample Input 2 
105

Sample Output 2
Error

Source
ccClub Judge
"""

n = int(input())
if n < 60:
    print("Fail")
elif n > 100:
    print("Error")
else:
    print("Pass")
    