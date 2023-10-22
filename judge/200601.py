"""
塞背包
描述

給定背包的最大承重，和數個物品的價值、重量，要找出一個不超過最大承重，
並且裝有最大總價值物品的裝填方式，是一個無法在多項式時間內處理的問題，
因此通常在處理這種問題的時候，會使用貪婪搜索法來找到一個可能不是最佳解，
但是還不錯的解答。

貪婪搜索法的精神在於，在每一步驟，都做當下可以獲得最大利益的的決定。在上述
這個問題中，我們當下最好的決定是選擇CP值（價值/重量）最高且不會造成過重
的物品放入背包。

舉例來說，如果最大承重=5,
物品A的價值/重量為18/4, CP值4.5
物品B的價值/重量為12/3, CP值4
物品C的價值/重量為7/2, CP值3.5
物品D得價值/重量為100/10, CP值為10

在這個範例下，雖然最佳解為選擇BC，剛好放滿書包，裝有總價值19的物品。
但當使用貪婪法時，在第一步會選擇A物品（雖然D物品CP值比較高但是放不下），
並且因為下一步無法再裝入其他物品，所以演算法結束。

這本題中，請你實作貪婪演算法，多個物品具有相同CP值則選輕的。
請照順序輸出每輪s選擇的物品名稱，以換行分開。


輸入
輸入第一行為書包最大承重w
第二行為物品數量n
以下n行為物品[名稱] [價值] [重量]以空白分開


輸出
輸出為數行，包含其所選擇的物品名稱字串


輸入範例 1 
5
3
A 18 4
B 12 3
C 7 2

輸出範例 1
A

輸入範例 2 
10
7
0 7 4
1 97 10
2 58 13
3 50 1
4 25 5
5 77 3
6 47 9

輸出範例 2
3
5
4

來源
ccClub Judge
"""

def sortCP(item):
  cpItem = int(item[1])/int(item[2])
  return cpItem


w = int(input())
n = int(input())
item = []
ans = []
currentW = 0
for _ in range(n):
    values = input().split()
    if int(values[2]) <= w:
        item.append(values)
sortItem = sorted(item,key=sortCP,reverse=True)
for i in sortItem:
  currentW += int(i[2])
  if currentW < w:
    ans.append(i[0])
  else:
    currentW -= int(i[2])

for i in ans:
  print(i)
