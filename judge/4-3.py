"""
4-3：三角形
Description

輸入三個正整數 a、b、c，如果可以組成一個三角形，輸出 True，否則輸出 False。


Input
輸入有三行，各包含一個整數


Output
輸出為一行， 請輸出 True 或 False


Sample Input 1 
3
4
5

Sample Output 1
True

Sample Input 2 
1
2
3

Sample Output 2
False

Source
ccClub Judge
"""

a = int(input())
b = int(input())
c = int(input())
if a+b>c and b+c>a and a+c>b:
    print(True)
else:
    print(False)
    