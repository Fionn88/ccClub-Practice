"""
討債集團
描述

小明最近因為太常去旅遊、喝酒、吃火鍋、唱 KTV 之類的，搞得戶頭快見底了，無奈的他只好去地下錢莊兼職幫忙討債。
這個地下錢莊專門削外國人的錢，他們有一個英文姓名欠債資料庫，裡面記載了每個外國人欠了多少錢。
小明的任務是按照錢莊莊主元龍每天安排的催討順序，不斷的去叨擾名單上欠債的外國人，為了讓外國人不勝其擾，元龍會安排不定時的多次造訪，讓外國人們不勝其擾因此還錢。
現在，給定外國人的名字以及對應的欠債金額，你可以設計一個演算法，協助小明列出今天依序要催討的金額嗎？


輸入
輸入有 n+2 行。
第一行是欠債外國人的名字，以空格區隔。
第二行是每個外國人對應的欠款金額，以空格區隔。
最後 n 行中，每行包含一個外國人名字，代表莊主元龍安排的催討順序。


輸出
輸出有 n 行，代表小明依序要催討的金額。


輸入範例 1 
Ana Bumper Cindy David
100 200 300 400
Ana
Cindy
Ana
Cindy
Bumper
Ana

輸出範例 1
100
300
100
300
200
100

輸入範例 2 
Barn Obeng Seys Selia Pennebaker Panthea Allegra Lewanna Ben
52 32 90 22 10 1 10 6 39
Lewanna
Selia
Allegra
Pennebaker
Seys
Allegra
Allegra
Barn
Panthea
Allegra

輸出範例 2
6
22
10
10
90
10
10
52
1
10
"""
names = input().split()
debts = input().split()
D = {}
for name, money in zip(names, debts):
    D[name] = money
while True:
    try:
        n = input()
        print(D.get(n))
    except:
        break