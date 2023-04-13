"""
[8-綜合] 嚴格遞增數列
Description

給定一串整數數列，請判斷此串數列是否為一個嚴格遞增數列。


Input
輸入為一行，為一串整數數列，整數間以空格作為間隔。


Output
輸出為一行，若為嚴格遞增數列請輸出 True，反之則輸出 False。


Sample Input 1 
1 2 9 4 13

Sample Output 1
False

Sample Input 2 
1

Sample Output 2
True

Source
ccClub Judge
"""

# 輸入input 轉成 int 
# 條件1. 判斷數列長度，1 就為 True
# 條件2. l[i] < l [i+1] 

nums = [int(num) for num in input().split()]
counter = 0
if len(nums) == 1:
  print(True)
else:
  for i in range(len(nums) -1 ):
    if nums[i+1] > nums[i]:
      counter += 1
  print(counter == len(nums) -1)