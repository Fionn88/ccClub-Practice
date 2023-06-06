"""
數字轉字母
描述

我們想要寫個數字轉字母的程式。

我們希望 1 對應 a， 2 對應 b，...，25 對應 y，26對應 z。


輸入
輸入為一行，包含數個數字，數字之前用逗號分割。


輸出
輸出為一行，包含一個字串，即轉換後的結果。


輸入範例 1 
1,16,16,12,5

輸出範例 1
apple

輸入範例 2 
3,3,3,12,21,2

輸出範例 2
ccclub

輸入範例 3 
13,1,3

輸出範例 3
mac

來源
ccClub Judge
"""

start_value = ord("a")
end_value = ord("z")

my_dict = {value - start_value + 1: chr(value) for value in range(start_value, end_value+1)}

s = input().split(',')
for index,value in enumerate(s):
  print(my_dict.get(int(value)),end='')
