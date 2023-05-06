"""
[12-1] 階乘
Description

請完成函式fact，使得輸入 n ，請輸出 n! 的值。

0! = 1，1! =1，n! = n*(n-1)!


Input
輸入有一行，包含一個正整數n。


Output
請輸出一個整數，值為n!。


Sample Input 1 
2

Sample Output 1
2

Sample Input 2 
5

Sample Output 2
120

Source
ccClub Judge
"""
def fact(m):
    # if m == 0 or _________:
    if m == 0 or m == 1:
        # return ____ 
        return 1 
    else:
        # return ____ * ____ 
        return m * fact(m-1)             

num = int(input())
print(fact(num))
