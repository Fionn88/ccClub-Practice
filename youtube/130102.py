"""
[13-1] 偶像資料庫
Description

強強很喜歡 TPE48 的偶像，所以想要建一個資料庫，只要輸入偶像的名字，就會跳出偶像的其他資料。現在資料已經找好了，但資料庫還沒建，你能把資料庫建好並做出查詢的功能嗎?


Input
輸入為 2 行，

第 1 行為所有偶像的名字、身高、血型。同一偶像的資料以逗號分隔，不同偶像之間以空白分隔。

第 2 行為要查詢的偶像名字。


Output
輸出為 1 行，為一個串列，包含該偶像的身高和血型。


Sample Input 1 
陳詩雅,152,O 潘姿怡,157,AB 林亭莉,161,B
潘姿怡

Sample Output 1
['157', 'AB']

Sample Input 2 
藤井麻由,162,B 邱品涵,153,O 林倢,165,B
邱品涵

Sample Output 2
['153', 'O']

Source
ccClub Judge
"""
idol = input().split()
search = input()
idol_dict = {}
for idolItem in idol:
   name,tall,blood= idolItem.split(',')
   idol_array = []
   idol_array.append(tall)
   idol_array.append(blood)
   idol_dict[name] = idol_array
print(idol_dict.get(search))
