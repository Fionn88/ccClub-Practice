"""
中位數
描述

給定數個已經依照大小排列好的整數，請輸出這個數列的中位數（請輸出浮點數）

輸入
輸入為一行，包含數個整數，以空白作為間隔


輸出
輸出為一行，包含一個浮點數


輸入範例 1 
1 3 5 7 9 11 13 15 17 19

輸出範例 1
10.0

輸入範例 2 
6 28 426

輸出範例 2
28.0

來源
ccClub Judge
"""
nums = list(map(int, input().split()))
n = len(nums)
if n % 2 == 0:
    median = (nums[n//2 - 1] + nums[n//2]) / 2
else:
    median = nums[n//2]
print(float(median))