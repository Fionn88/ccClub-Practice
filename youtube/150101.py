"""
[15-1] 加法計算機
Description

小明想實作一個有加法功能的計算機，提供使用者輸入兩個整數，最後輸出兩個整數的和。小明想在最後附一個提醒的功能，如果使用者輸入的不是數字，則輸出 "請輸入阿拉伯數字" 的提示字串。請你幫小明實作這個計算機吧！


Input
輸入為兩行，分別為兩個整數。


Output
輸出為一行，若使用者輸入為兩個阿拉伯數字，輸出兩整數和；若輸入的不是阿拉伯數字，則輸出 "請輸入阿拉伯數字"。


Sample Input 1 
14
21

Sample Output 1
35

Sample Input 2 
hello
14

Sample Output 2
請輸入阿拉伯數字

Source
ccClub Judge
"""
num1 = input()
num2 = input()
try:
	num1 = int(num1)
	num2 = int(num2)
	print(num1 + num2)
except:
	print("請輸入阿拉伯數字")
