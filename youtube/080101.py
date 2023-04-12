"""
[8-1] 和與階乘I
Description

給定一個正整數 num，請試著用迴圈，計算出從正整數 1 到 整數 num 的和與乘積


Input
輸入為一行，為一個正整數 num


Output
輸出為兩行，第一行為整數 1 到整數 n 的和；第二行為整數 1 到整數 n 的乘積


Sample Input 1 
4

Sample Output 1
10
24

Sample Input 2 
10

Sample Output 2
55
3628800

Source
ccClub Judge
"""
# input
num = int(input())

# calcuation
summation = 0
product = 1

for n in range(1,num+1):
	summation += n
	product *= n
  

# output
print(summation)
print(product)
