"""
[8-綜合] 數列三胞胎
Description

給定一正整數數列 nums ，請計算此數列中有幾組數字組合滿足以下條件：

0 <= i < j < k <= len(nums) - 1
nums[i] + nums[j] == nums[k]

Input
輸入為一行，包含 3 個以上的正整數，以空白作為間隔。


Output
輸出為一行，為一個整數。


Sample Input 1 
1 2 3 6

Sample Output 1
1

Sample Input 2 
1 3 4 8 2 6

Sample Output 2
2

Source
ccClub Judge
"""
nums = [int(num) for num in input().split()]

counter = 0
for i in range(0, len(nums)-2):
  for j in range(i+1, len(nums)-1):
    for k in range(j+1, len(nums)):
      if nums[i] + nums[j] == nums[k]:
        counter += 1
          
print(counter)