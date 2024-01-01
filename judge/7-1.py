"""
7-1：長方星

Description
輸入兩個正整數 l 和 w，使用「*」輸出一個長寬分別為 l 和 w 的長方形。

Input
輸入有兩行，各包含一個整數

Output
請輸出一個長寬分別為 l 和 w 的長方形

Sample Input 1 
3
2

Sample Output 1
***
***

Sample Input 2 
4
3

Sample Output 2
****
****
****

Source
ccClub Judge
"""

l = int(input())
w = int(input())
for j in range(w):
  print('*'*l)
  