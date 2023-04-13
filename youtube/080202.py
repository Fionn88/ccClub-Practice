"""
[8-2] 二進位
Description

給定一個十進位的正整數 n，請試著用 while loop 轉換二進位，並輸出最後的二進位結果。


Input
輸入為一個十進位的正整數 n。


Output
請輸出轉換成二進位後的結果。


Sample Input 1 
5

Sample Output 1
101

Sample Input 2 
14

Sample Output 2
1110

Hint
Python 內建也有二進位的函式bin()，可以用這個函式檢查計算的結果是否正確。

Source
ccClub Judge
"""
# input
n = int(input())

# transform
res = ''
# while _____:
# 	res _______
# 	n _______
while n > 0:
	res += str(n % 2)
	n = n // 2

# output
print(res[::-1])
