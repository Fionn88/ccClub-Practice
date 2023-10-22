"""
字母轉數字
描述

我們想要寫個字母轉文字的程式。

我們希望 a 對應到 1，b 對應到 2 ，...，y 對應到 25，z 對應到 26。


輸入
輸入為一行，包行一個字串


輸出
輸出為一行，包含數個數字，數字間用逗號分割。


輸入範例 1 
apple

輸出範例 1
1,16,16,12,5

輸入範例 2 
ccclub

輸出範例 2
3,3,3,12,21,2

輸入範例 3 
mac

輸出範例 3
13,1,3

來源
ccClub Judge
"""

start_value = ord("a")
end_value = ord("z")

my_dict = {chr(value): value - start_value + 1 for value in range(start_value, end_value+1)}

s = input()
for index,value in enumerate(s):
  if index == len(s) - 1:
    print(my_dict.get(value))
  else:
    print(my_dict.get(value),end=',')
