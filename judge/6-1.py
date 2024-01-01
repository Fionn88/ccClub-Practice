"""
6-1：因數

Description
輸入一個正整數，輸出其所有因數。

Input
輸入為一行，包含一個正整數

Output
請輸出這個整數的所有因數，以換行為區隔

Sample Input 1 
10

Sample Output 1
1
2
5
10

Sample Input 2 
19

Sample Output 2
1
19

Source
ccClub Judge
"""

N = int(input())
for i in range(1,N+1):
    if N % i == 0:
        print(i)
        