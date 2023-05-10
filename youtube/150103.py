"""
[15-1] 末三個數字相加
Description

給定一個串列，若串列中末三個元素為整數，請輸出它們的整數和。若末三個元素有其中一個元素不是整數，請輸出 "資料型態不為整數" 的提示字串；若串列長度小於 3 ，請輸出 "串列長度不足" 的提示字串。


Input
輸入為一行，為數個數字，數字間以空白作為間隔。


Output
輸出為一行，請根據題目敘述輸出結果。


Sample Input 1 
9 4 8 7

Sample Output 1
19

Sample Input 2 
1 2

Sample Output 2
串列長度不足

Source
ccClub Judge
"""
try:
    digits = [int(d) for d in input().split()]  # 轉換成 List
    if len(digits) < 3:
      print('串列長度不足')
    else:
      print(digits[-1]+digits[-2]+digits[-3])
except:
	print("資料型態不為整數")