"""
[9-1] 移動平均
Description

移動平均是一種將時間序列資料消除雜訊以看清趨勢的方法。強強想要計算給定串列中，n 個數值的移動平均，例如在串列 [1,2,3,4,5] 中，取 3 個數值的移動平均是 [2.0, 3.0, 4.0]；在串列 [9,8,7,6,5,4,3,2] 中，取 5 個數值的移動平均是 [7.0, 6.0, 5.0, 4.0]。但是不知道為什麼程式計算有問題，你可以幫幫他嗎？


Input
輸入為 2 行，第一行為要取的資料範圍。第二行為給定的串列。


Output
輸出為 1 行，為移動平均的串列。


Sample Input 1 
0
[5,4,3,2,1]

Sample Output 1
[]

Sample Input 2 
1
[5,4,3,2,1]

Sample Output 2
[5.0, 4.0, 3.0, 2.0, 1.0]

Hint
注意ZeroDivisionError

Source
ccClub Judge
"""
output = []
n = int(input())
data = [int(i) for i in input().replace('[', '').replace(']', '').split(',')]
for i in range(len(data) - n + 1):
#     output.append(sum(data[i : i+n]) / n)
    if n != 0:
      output.append(sum(data[i : i+n]) / n)

print(output)
