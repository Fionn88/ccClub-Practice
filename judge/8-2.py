"""
8-2：最長字串

Description
給定一個內容物皆為字串(str)的串列l ，並且實作一個函式 longest_str()，參數為串列l。函式的輸出值為串列中長度最長的字串，若長度相同，則回傳 index 較小的。

Input
輸入為一行，包含數個字串以空白間隔，請將其轉換為一個串列

Output
輸出為一行，包含此串列中最長的一個字串

Sample Input 1 
apple python Plasma

Sample Output 1
python

Sample Input 2 
gg app eth rich

Sample Output 2
rich

Source
ccClub Judge
"""

def longest_str(l):
    MaxValue = 0
    ans = ""
    for i in range(len(l)-1,-1,-1):
      if len(l[i]) > MaxValue:
        MaxValue = len(l[i])
      if MaxValue == len(l[i]):
        ans = l[i]
      
    return(ans)

l = input().split()
print(longest_str(l))
