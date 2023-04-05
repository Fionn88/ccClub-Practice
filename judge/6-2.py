"""
6-2：完全平方數
Description

輸入一個正整數，輸出比他小的完全平方數。


Input
輸入有一行，包含一個整數


Output
請輸出比他小的所有完全平方數。，以換行為分隔


Sample Input 1 
10

Sample Output 1
1
4
9

Sample Input 2 
9

Sample Output 2
1
4

Source
ccClub Judge
"""
N = int(input())
for i in range(1,N):
    if i*i < N:
        print(i*i)