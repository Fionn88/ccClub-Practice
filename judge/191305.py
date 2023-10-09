"""
串列切割
描述

給定數個以逗號分隔的浮點數，在將這些浮點數放入串列以後，請判斷是否有辦法將此串列切成兩半以後，左半邊的和等於右半邊的和。如果可以，請印出 "True"，若否請印出 "False"。

舉例來說，給定的數字串列為 [1, 2, 3]，由於可以將此串列切成 1, 2 和 3 兩部份，而且這兩部分的和都是 3，因此答案是 "True"。


輸入
輸入為一行，包含數個浮點數，以逗號分隔


輸出
輸出為一行，包含 "True" 或是 "False"


輸入範例 1 
1,2,3

輸出範例 1
True

輸入範例 2 
1,2,3,4

輸出範例 2
False

輸入範例 3
2,-2,1,-1,0,0

輸出範例 3
True

來源
ccClub Judge
"""
numbers = list(map(float,input().split(',')))

total_sum = sum(numbers)

left_sum = 0

for i in range(len(numbers)):
    left_sum += numbers[i]
    if left_sum == total_sum / 2:
        print("True")
        break
else:
    print("False")
