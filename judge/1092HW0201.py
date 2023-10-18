"""
配對問題
描述

嘻嘻幼幼班與咚咚幼幼班要一起出去玩了，有鑑於希望人數一樣多的兩班小朋友可以多多認識，嘻嘻幼幼班與咚咚幼幼班的老師決定讓兩班的小朋友兩兩交錯排隊，但由於現在老師們的手上只有一份兩班的長名單。給定一份兩班小朋友的名單，可以請你幫忙輸出兩班小朋友交錯的對列嗎？

以範例測資一為例，名單為：

小華 小明 小國 小鐘

則前半段名單為嘻嘻幼幼班，後半段名單為咚咚幼幼班，配對結果為：

小華 小國 小明 小鐘


輸入
共一行，包含一字串，數個名字中間以空白分隔


輸出
共一行，包含一字串，數個名字中間以空白分隔


輸入範例 1 
小華 小明 小國 小鐘

輸出範例 1
小華 小國 小明 小鐘

輸入範例 2 
2 5 7 1 3 4

輸出範例 2
2 1 5 3 7 4
"""
name_list = input().split()

middle = len(name_list) // 2

result_list = []
for i in range(middle):
    result_list.append(name_list[i])
    result_list.append(name_list[i + middle])

result = ' '.join(result_list)

print(result)
