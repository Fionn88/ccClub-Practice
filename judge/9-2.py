"""
9-2：字串反轉排序

Description
給定一個 list ，內容物皆為字串(str)，排序規則：依照字串反轉的結果（ex：'abc' 反轉後是 'cba' ），由小到大排並輸出。

Input
給定一行輸入，包含數個字串以空白間隔，請將之轉換成一個 list

Output
請輸出排序後的串列

Sample Input 1 
apple btc python

Sample Output 1
['btc', 'apple', 'python']

Sample Input 2 
btc eth cob mith

Sample Output 2
['cob', 'btc', 'eth', 'mith']

Source
ccClub Judge
"""

l = input().split()
toAns = []
ans = []
for i in l:
  toAns.append(i[::-1])
forans = sorted(toAns)
for j in forans:
  ans.append(j[::-1])
print(ans)
