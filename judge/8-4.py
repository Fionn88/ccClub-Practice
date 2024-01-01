"""
8-4：最大公因數

Description
給定兩個串列 l1 和 l2 ，內容物皆為整數(int)。
實作一個函式 gcd() ，參數為兩串列 l1 以及 l2，請找出兩串列中相同 index 兩個數字的最大公因數，並儲存在串列(list)中回傳。

Input
輸入有兩行，包含數個整數，以空白分隔，請將他們轉換成串列 l1 和 l2 ，內容物皆為整數(int)。

Output
輸出有一行，包含一個內容為整數的串列

Sample Input 1 
2 12 24
4 6 15

Sample Output 1
[2, 6, 3]

Sample Input 2 
10 30
20 600

Sample Output 2
[10, 30]

Source
ccClub Judge
"""

import math
def gcd(l1,l2):
    ans = []
    for i in range(len(l1)):
      ans.append(math.gcd(int(l1[i]), int(l2[i])))
    return(ans)

l1 = input().split()
l2 = input().split()
print(gcd(l1,l2))
