"""
[6-2] 串列操作-3
Description

已知 my_lst 為一串列，保證不為空串列。請依照以下指令操作並輸出，輸出共有兩行：

將該串列反轉
反轉後，移除串列中的第一個物件，並輸出
將剛才移除的物件輸出

Input
輸入為一行包含數個字串以逗號分隔，經轉換後為一串列。


Output
輸出有兩行。

第一行為一串列，第二行為一字串。


Sample Input 1 
c,c,c,l,u,b

Sample Output 1
['u', 'l', 'c', 'c', 'c']
b

Sample Input 2 
Python

Sample Output 2
[]
Python

Hint
使用 lst.reverse() 可將串列中物件的順序反轉，lst 本身將被改變。
lst.pop(位置) 可將串列 lst 中指定位置的物件移除。
該指令執行時，除了將 lst 內的物件移除，也會將移除的物件回傳，因此可以再設定一個變數將移除的物件存起來，例如：item = lst.pop(0)，執行上述指令時不僅移除串列 lst 中的第一個物件，被移除的物件現在已存到變數 item 裡囉。

Source
ccClub Judge
"""
# 此段程式碼不需特別了解, 該功能為將輸入的資料轉換為串列
# 只需知道 my_lst 為一串列, 即可對 my_lst 進行操作完成本題
my_lst = input().split(",")
