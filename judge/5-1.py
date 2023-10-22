"""
5-1：翻箱倒櫃
Description

我們在課程中形容串列 list 就像是個櫃子，現在我們試著要找看看櫃子裡的東西。

輸入兩串列lst1、lst2以及一個字串s，如果能在 lst1 或 lst2 找到 s ，則輸出 True，否則輸出 False。


Input
輸入一共有三行。

前兩行包含了兩組字串，字串間皆以空格分開，請將其轉換成兩串列 lst1 和 lst2，而第三行則是一個字串 s


Output
輸出 True 或 False


Sample Input 1 
apple pen
pineapple pen
apple

Sample Output 1
True

Sample Input 2 
apple pen
pineapple pen
pen

Sample Output 2
True
Hint

請嘗試使用 string.split() 這個函式看看吧！

Source
ccClub Judge
"""

lst1 = input.split()
lst2 = input.split()
s = input()
if s in lst1 or s in lst2:
    print(True)
else:
    print(False)
    
