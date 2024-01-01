"""
綜合1-1：Three Sum

描述
給定一個由小至大且長度大於三的串列 lst，若其中三個數字的總和為 0 ，按照 index 大小由小到大將其輸出。

輸入
給定一行輸入，內容為三個以上的整數由小至大排列，整數間以空格分開，請轉換為串列 lst

輸出
輸出為數行，各包含三個整數，以空格分隔

輸入範例 1 
-5 -3 1 2 4 8

輸出範例 1
-5 -3 8
-5 1 4
-3 1 2

輸入範例 2 
0 0 0 0

輸出範例 2
0 0 0
0 0 0
0 0 0
0 0 0

來源
ccClub Judge
"""

nums = [int(num) for num in input().split()]

counter = 0
for i in range(0, len(nums)-2):
  for j in range(i+1, len(nums)-1):
    for k in range(j+1, len(nums)):
      if nums[i] + nums[j] + nums[k] == 0:
        counter += 1
        print(nums[i],nums[j],nums[k])
          