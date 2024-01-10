"""
Three sum 趴兔

描述
給定 k 個依照大小排序好的數，以及一個整數 n。
已知 len(lst) >= 3，找出 k 個數中，同時滿足以下條件的組合數量:
lst[i] + lst[j] + lst[k] < n
0 <= i < j < k < len(lst)

輸入
輸入為兩行。
第一行包含數個數字，數字間以空白為間隔
第二行為整數 n

輸出
輸出為一行，包含一個整數。

輸入範例 1
1 3 5 7 9 11
18

輸出範例 1
10

輸入範例 2
2 2 2 2
6

輸出範例 2
0

來源
ccClub Judge
"""

def threeSum(nums, n):
    counter = 0
    length = len(nums)
    
    for i in range(length - 2):
        j = i + 1
        k = length - 1
        
        while j < k:
            threesum = nums[i] + nums[j] + nums[k]
            if threesum < n:
                counter += (k - j)
                j += 1
            else:
                k -= 1

    return counter

nums = [int(num) for num in input().split()]
n = int(input())
print(threeSum(nums,n))
