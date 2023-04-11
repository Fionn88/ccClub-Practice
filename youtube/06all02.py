"""
[6-綜合] 取出特定物件
Description

給定一個串列 lst = ['p', 'y', 't', 'h', 'o', 'n']

取出該串列中，位在奇數位置的物件，並以串列形式輸出


Input
此題無輸入。


Output
輸出為一個串列。


Sample Input 1 

 
Sample Output 1
['p', 't', 'o']

Hint
範圍取值方式為：串列[起始值:結束值:間隔值]。
取奇數位置的物件，亦即由第一個物件開始取，取值的間隔為 2。

Source
ccClub Judge
"""

lst = ['p', 'y', 't', 'h', 'o', 'n']

# your code here
i = 0
ans = []
while i < len(lst):
  ans.append(lst[i])
  i = i + 2
print(ans)

