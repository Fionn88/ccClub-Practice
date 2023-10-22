"""
8-3：及格門檻
Description

給定一個內容物皆為整數(int)的串列 l ，以及數字 t，實作一個函式 threshold()，參數為串列 l 以及整數t，函式的回傳值為串列。請判斷原始串列中每個值是否大於或等於門檻，再將此函式回傳的串列印出。


Input
給定兩行輸入，第一行包含數個整數，以空白為間隔，請轉換為一個內容物皆為整數(int)的串列 l 。第二行包含一個數字 t。


Output
輸出為一行，包含一個串列，內容為數個 bool 值。


Sample Input 1 
50 70 90
60

Sample Output 1
[False, True, True]

Sample Input 2 
1 2 3 4 5 6 7
4

Sample Output 2
[False, False, False, True, True, True, True]

Source
ccClub Judge
"""

def threshold(l,t):
    ans = []
    for i in l:
      if t <= i:
        ans.append(True)
      elif t > i:
        ans.append(False)
      
    return(ans)

l = map(int,input().split())
t = int(input())
print(threshold(l,t))
