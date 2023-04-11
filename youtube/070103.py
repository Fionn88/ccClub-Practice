"""
[7-1] 小明出去玩
Description

小明喜歡出去玩，但如果下雨的話，不論何種狀況他都選擇「自己在家玩」。

如果沒有下雨，又有朋友陪的話，他就會「跟朋友出去玩」。

如果沒有朋友的話，就會選擇「自己出去玩」。

可能的天氣有 3 種: 晴天、陰天、雨天。


Input
輸入為 2 行，第 1 行為天氣，為晴天、陰天、雨天其中一種。

第 2 行為有空的朋友數量，必定大於或等於0。


Output
輸出為 1 行，為小明要在哪裡玩，可能是「跟朋友出去玩」、「自己出去玩」、「自己在家玩」。


Sample Input 1 
雨天
0

Sample Output 1
自己在家玩

Sample Input 2 
陰天
9

Sample Output 2
跟朋友出去玩

Source
ccClub Judge
"""
weather = input()
frind = int(input())
if weather == '雨天':
  print('自己在家玩')
elif weather == '陰天' or weather == '晴天':
  if frind > 0:
    print('跟朋友出去玩')
  else:
    print('自己出去玩')