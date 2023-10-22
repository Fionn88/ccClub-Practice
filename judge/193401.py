"""
書碼編輯
描述

cc 圖書館有著許多館藏，我們需要為每一本書都編一個書碼，方便讀者查閱時能夠靠著書碼找到自己想要的書。

然而，有些書的書名會相同，因此我們用了一些特別的規則來編書碼（共十碼），規則如下：

該書名進館藏的順序（前三碼）
該書是館藏同書名中第幾本進書庫的（中間三碼）
該書進館藏的順序（末四碼）

輸入
輸入有 N+1 行。

第 1~N 行每行有一個字串，代表書名。

（書本依照順序進館藏，第一行先，再來是第二行，依此類推，最後一本進館藏的是第 N 行）

第 N+1 為 0 ，代表輸入結束。


輸出
輸出有 K 行。

每一行包含兩個部分，首先是書名，接著是該書名的所有書（依照進館藏的順序排列），書名、書碼之間都用空格分開。

（詳細說明請見 Hint）


輸入範例 1 
HarryPotter
HarryPotter
TheLordoftheRings
HarryPotter
HarryPotter
TheLordoftheRings
TheLordoftheRings
TheLordoftheRings
0

輸出範例 1
HarryPotter 0010010001 0010020002 0010030004 0010040005
TheLordoftheRings 0020010003 0020020006 0020030007 0020040008

輸入範例 2 
stretching
embedded
embedded
stretching
will
0

輸出範例 2
stretching 0010010001 0010020004
embedded 0020010002 0020020003
will 0030010005

提示
sample input1 的輸入為：

HarryPotter => 館藏一開始沒有書，HarryPotter 是第一個出現的書名，因此前三碼為 001；這本是第一本書名為HarryPotter的書，因此中間三碼為 001；這本書是館藏第一本書，因此後四碼為 0001。

HarryPotter => 館藏已有書名為HarryPotter 的書，前三碼為001；這本是第二本書名為HarryPotter 的書，因此中間三碼為 002；這本書是館藏第二本書，因此後四碼為 0002。

TheLordoftheRings =>館藏只有書名為HarryPotter 的書，TheLordoftheRings 是第二個出現的書名，因此前三碼為 002；這本是第一本書名為TheLordoftheRings的書，因此中間三碼為 001；這本書是館藏第三本書，因此後四碼為0003。

HarryPotter=> 館藏已有書名為HarryPotter 的書，前三碼為 001；這本是第三本書名為 HarryPotter 的書，因此中間三碼為 003；這本書是館藏第四本書，因此後四碼為 0004。

HarryPotter=> 館藏已有書名為HarryPotter 的書，前三碼為 001；這本是第四本書名為 HarryPotter 的書，因此中間三碼為 004；這本書是館藏第五本書，因此後四碼為 0005。

TheLordoftheRings=> 館藏已有書名為TheLordoftheRings的書，前三碼為 002；這本是第二本書名為TheLordoftheRings的書，因此中間三碼為 002；這本書是館藏第六本書，因此後四碼為 0006。

TheLordoftheRings=> 館藏已有書名為TheLordoftheRings 的書，前三碼為 002；這本是第三本書名為 TheLordoftheRings 的書，因此中間三碼為 003；這本書是館藏第七本書，因此後四碼為 0007。

TheLordoftheRings=> 館藏已有書名為TheLordoftheRings 的書，前三碼為 002；這本是第四本書名為 TheLordoftheRings 的書，因此中間三碼為 004；這本書是館藏第八本書，因此後四碼為 0008。

來源
ccClub Judge
"""

books = []

while True:
    user_input = input()
    books.append(user_input)

    if user_input == "0":
        break
books.pop()

# 取前三碼
bookmark = {}
j = 0
for i in range(len(books)):
  if books[i] not in bookmark:
    j += 1
    bookmark[books[i]] = str(j).zfill(3)


# 取後面三碼
order = {}
for i, value in enumerate(books):
    if value in order:
        order[value].append(i+1)
    else:
        order[value] = [i+1]

for i in range(len(bookmark)):
  g = 0
  for l in order.get(list(bookmark)[i]):
    g += 1
    if g == 1:
      print(list(bookmark)[i],end=' ')
      print(bookmark.get(list(bookmark)[i])+str(g).zfill(3)+str(l).zfill(4),end=' ')
    elif g != len(order.get(list(bookmark)[i])):
      print(bookmark.get(list(bookmark)[i])+str(g).zfill(3)+str(l).zfill(4),end=' ')
    else:
      print(bookmark.get(list(bookmark)[i])+str(g).zfill(3)+str(l).zfill(4))
