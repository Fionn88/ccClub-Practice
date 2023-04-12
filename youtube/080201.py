"""
[8-2] 和與階乘II
Description

接續上一題 和與階乘I ，請試著用影片介紹的 while 迴圈，完成正整數 1 到 正整數 num 的和與乘積的計算吧！


Input
輸入為一行，為一個正整數 num。


Output
輸出為兩行，第一行為整數 1 到整數 n 的和；第二行為整數 1 到整數 n 的乘積。


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

summation, product = 0, 1
n = 1
# while ______:
# 	summation += n
# 	product *= n
# 	n _____

while n < num+1:
	summation += n
	product *= n
	n += 1

# output
print(summation)
print(product)
