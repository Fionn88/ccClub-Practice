"""
[5-4] 3 的倍數
Description

給定一個正整數，請試著判斷該整數是否為 3 的倍數，如果是 3 的倍數輸出 True，不是則輸出 False。


Input
輸入為一行，為一個正整數。


Output
輸出為一行，為一布林值，如果是 3 的倍數輸出 True，不是則輸出 False。

Sample Input 1 
3

Sample Output 1
True

Sample Input 2 
10

Sample Output 2
False

Hint
判斷是否為 3 的倍數，可計算該數字除以 3 的餘數，若餘數為 0 則表示為 3 的倍數
使用 % 可計算相除之後的餘數

Source
ccClub Judge
"""
i = int(input())
if i % 3 == 0:
  print(True)
else:
  print(False)