"""
小仔填志願
描述

最近高中學測放榜了，小仔心中有幾個想填的志願，給定小仔的國、英、數、社、自學測成績，成績以兩位數呈現並以逗號隔開，請你依照去年的最低錄取分數，幫他看看他輸入的科系有沒有機會錄取吧！


================
圖片 1.png
================

輸入
共 2 行，

第 1 行，包含一字串，依序為小仔國英數社自成績，中間以逗號分隔（測資的級分都是合理的）

第 2 行，包含一字串，需檢驗的科系


輸出
共 1 行，輸出是否有通過去年標準(有通過輸出 1，沒通過輸出 0)


輸入範例 1
14,15,15,13,11
經濟系

輸出範例 1
0

輸入範例 2 
08,15,15,13,12
資工系

輸出範例 2
1
"""
department = {"會計系":["國英數社",57,"國",15], "公衛系":["英數自",38], "經濟系": ["社自",26,"數",15],"資工系":["英自",27,"數",15]}
line = ["國","英","數","社","自"]
score = input().split(",")
target = input()
breakOrNot = False

for index,value in enumerate(department.get(target)):
    if index % 2 == 0:
        subject = value
    else:
        sumTheScore = 0
        for i in subject:
            sumTheScore += int(score[line.index(i)])
        if sumTheScore < value:
            print(0)
            breakOrNot = True
            break
if not breakOrNot:
    print(1)        