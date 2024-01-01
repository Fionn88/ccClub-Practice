"""
8-1：乘積最大值

Description
給定一個內容物皆為整數(int)的串列 l ，並且實作一個函式 max_mul()。函式的參數為整數串列l，回傳值為串列中「連續兩個相鄰乘積」的最大值，並請將回傳值印出。

Input
輸入為一行，包含數個整數，以空白為間隔。

Output
輸出為一行，包含一個整數。

Sample Input 1 
1 -1

Sample Output 1
-1

Sample Input 2 
1 -2 -3 4 -5 -6

Sample Output 2
30

Source
ccClub Judge
"""

def max_mul(l):
    s=[]
    for i in range(len(l)-1):
        multi_value=int(l[i]) * int(l[i+1])
        s.append(multi_value)
    max_value=max(s)
    return(max_value)

l = input().split()
print(max_mul(l))
