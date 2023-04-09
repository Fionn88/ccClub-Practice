"""
[6-2] 操作串列-1
Description

此題為填空題。

已知 num_lst 為一串列，該串列內都是數字。

請計算該串列中總共有幾個物件，以及該串列中 0 的數量。


Input
輸入為 5 個數字以逗號分隔，經轉換後為一串列。。


Output
輸出有兩行，第一行為該串列中總共有幾個物件，第二行為該串列中 0 的數量。


Sample Input 1 
1,2,3,4,5

Sample Output 1
5
0

Sample Input 2 
2,0,2,1,0,1,0,1

Sample Output 2
8
3

Source
ccClub Judge
"""
# 此段程式碼不需特別了解, 該功能為將輸入的資料轉換為串列
# 只需知道 num_lst 為一串列, 且該串列內都是數字, 即可對 num_lst 進行操作完成本題
num_lst = [int(i) for i in input().split(",")]

# print(_____(num_lst))
# print(num_lst._____(0))

print(len(num_lst))
print(num_lst.count(0))
