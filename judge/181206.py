"""
連四相乘
描述

給定 k 個（k >= 4）依數大小由小至大排序的整數，找出這些數中挑 4 個數字相乘的最大值。


輸入
輸入為一行，包含 k 個整數（k >= 4），數字以空白為間隔。


輸出
輸出為一行，包含一個整數。


輸入範例 1 
-7 -7 1 2 3 4 5 6 7 8

輸出範例 1
2744

輸入範例 2 
1 2 3 4

輸出範例 2
24

來源
ccClub Judge
"""
nums = list(map(int,input().split()))
n = len(nums)
print(max(nums[n-1]*nums[n-2]*nums[n-3]*nums[n-4], nums[0]*nums[1]*nums[n-1]*nums[n-2]))
