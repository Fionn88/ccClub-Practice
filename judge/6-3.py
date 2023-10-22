"""
6-3：母音種類個數
Description

輸入一個字串，輸出字串中母音種類個數（同樣字母大小寫視為不同）


Input
輸入有一行，包含一個字串


Output
輸出有一行，包含一個整數


Sample Input 1 
Zoo

Sample Output 1
1

Sample Input 2 
Eye

Sample Output 2
2

Source
ccClub Judge
"""

s = input()
L = ['a','e','i','o','u','A','E','I','O','U']
ansList = []
for i in s:
  if i in L:
    ansList.append(i)
print(len(set(ansList)))
