"""
小明上菜啦
描述

小明經營了一家餐廳，提供多種不同的料理。但小明最近遇到一個麻煩的問題 —— 常常做菜做到一半才發現材料不夠用。畢竟材料可能有辦法讓一道菜可以做一次，但沒辦法做第二次。因此小明決定寫一個程式，在每次收到點餐後先檢查庫存是否足夠，你能夠幫他完成嗎？

輸入包含三個部分：第一部分為食材數量、第二部分為餐廳菜單、第三部分為點餐單。其中第一部分的第1行為n，代表食材種類數，下一行為n個字串和n個數字用空白分開，代表食材的名稱跟數量，會以如下格式 [材料1] [個數] [材料2] [個數] 呈現。

第二部分的第1行為m，代表菜單上的料理種類數，以下m行包含所需材料的資訊。格式為： [料理名稱] [材料1] [個數] [材料2] [個數]材料的種類至少1種，個數至少1個。

第三部分第一行為k，代表點餐的數量，以下k行皆為單一字串，代表料理的名稱。

請幫小明管理上菜的流程，決定客人的點餐哪些可以完成哪些無法（每個點餐是否有足夠的食材），並輸出 True or False。


輸入
第 1 行為 n，代表食材種類數。下一行為n個字串和n個數字用空白分開，代表食材的名稱跟數量，會以如下格式 [材料1] [個數] [材料2][個數] 呈現。
第 3 行為整數 m，代表菜單上的料理種類數。以下 m 行包含料理名稱以及所需材料的資訊，每一行皆由字串及數字組成，第一個字串為料理名稱，再來是所需材料、所需個數。格式如右：[料理名稱] [材料1] [個數] [材料2] [個數]
第 m+4 行為整數 k ，代表點餐的數量。以下k行皆為單一字串，代表料理的名稱。


輸出
輸出為 k 行，各包含一個布林值（True/False）


輸入範例 1 
3
武藏 2 小次郎 1 喵喵 2
2
火箭隊 武藏 1 小次郎 1 喵喵 1
小智一行人 小智 1 小霞 1 小剛 1
3
火箭隊
小智一行人
火箭隊

輸出範例 1
True
False
False

來源
ccClub Judge
"""

n = int(input())
stock = input().split()
m = int(input())
menu = [input().split() for _ in range(m)]
k = int(input())

stockDic = {}
menuDic = {}
j = 0
ans = []
for _ in range(n):
  stockDic[stock[j]] = int(stock[j+1])
  j += 2
for i in range(m):
  menuDic[menu[i][0]] = menu[i][1:]

for _ in range(k):
  s = input()
  flag = True
  if menuDic.get(s) != None:
    for g,p in enumerate(menuDic.get(s)):
      if g % 2 == 0:
        stockItem = stockDic.get(p,0)
        currItem = p
      else:
        currItemCount = stockItem - int(p)
        if currItemCount < 0:
          flag = False
          break
  else:
    flag = False
    break
  if flag:
    item = menuDic.get(s)
    for g,p in enumerate(menuDic.get(s)):
      if g % 2 == 0:
        stockItem = stockDic.get(p,0)
        currItem = p
      else:
        currItemCount = stockItem - int(p)
      stockDic[currItem] = currItemCount
  ans.append(flag)
for i in ans:
  print(i)