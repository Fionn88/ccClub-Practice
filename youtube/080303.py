"""
[8-3] 單調遞增轉換
Description

給定一個單調遞增(monotonically increasing)數列，請將數值相等的部分去除，只留下嚴格遞增的部分，並輸出最後嚴格遞增的數列。輸入為一行，包含數個整數，整數間以空白作為間隔。


Input
輸入為一行，包含數個整數，整數間以空白作為間隔。


Output
輸出為一行，為一個整數串列。


Sample Input 1 
1 1 1 2 5 8

Sample Output 1
[1, 2, 5, 8]

Sample Input 2 
2 4 4 7 9

Sample Output 2
[2, 4, 7, 9]

Source
ccClub Judge
"""
l = map(int,list(set(input().split())))
print(sorted(l))
