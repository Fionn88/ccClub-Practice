"""
字元強調
描述

為了要強調一個句子的某些英文字母，我們用大寫來表示他。

輸入一個英文句子，將需要強調的字母轉成大寫（只將詞的第一個字轉大寫），並將整個句子輸出。


輸入
輸入有兩行。

第一行為一個字元，代表需要強調的英文字母。

第二行為一個字串，代表一個句子。


輸出
輸出有一行，為將句子中需要強調的字母轉成大寫。


輸入範例 1 
a
I am a idiot.

輸出範例 1
I Am A idiot.

輸入範例 2 
y
So don't you worry your pretty little mind, People throw rocks at things that shine.

輸出範例 2
So don't You worry Your pretty little mind, People throw rocks at things that shine.

提示
Sample input 2 中，you會被轉成You，worry因為 y 不是在第一個字元，所以維持輸出worry。

來源
ccClub Judge
"""

key = input()
s = input().split()
for index,value in enumerate(s):
  if value[0] == key:
    if index == len(s)-1:
      print(value.title())
    if index != len(s)-1:
      print(value.title(),end=' ')
  else:
    if index == len(s)-1:
      print(value)
    else:
      print(value,end=' ')
