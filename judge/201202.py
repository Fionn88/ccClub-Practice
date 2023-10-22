"""
小明打魯石
描述

魯石戰記是一款卡牌遊戲，每張卡片都有自己的素質包含 [攻擊力] 和 [生命值]。當兩張卡片戰鬥時，會對對方造成等同於自己攻擊力的傷害。

舉例來說：貪吃龍 4 4 和 小鬼老大 2 5 戰鬥後，貪吃龍的素質會變成 4 2，因為小鬼老大的攻擊力為 2；小鬼老大會變成 2 1，因為貪吃龍的攻擊力為 4。此時如果再發生一次戰鬥，會使得兩者的生命值都小於零，因此兩者都會死亡。

給定兩張卡片的素質，讓兩者戰鬥直到一方死亡。請找出勝利者和他戰鬥結束後的體質。若兩者同時死亡，請輸出 tie(平手)。


輸入
輸入為兩行，各包含一個字串以及兩個整數。


輸出
輸出為一行，若有其中一方得勝，則該行包含一個字串以及兩個整數；若兩方同時死亡，則包含一個字串 tie


輸入範例 1 
溫和的大蜥蜴 5 4
魚人班長 2 4

輸出範例 1
溫和的大蜥蜴 5 2

輸入範例 2 
溫和的大蜥蜴 5 4
暴躁的小蜥蜴 5 4

輸出範例 2
tie

來源
ccClub Judge
"""

player1 = input().split()
player2 = input().split()

namePlayer1 = player1[0]
namePlayer2 = player2[0]
attributePlayer1 = list(map(int,player1[1:]))
attributePlayer2 = list(map(int,player2[1:]))

while True:
    if attributePlayer1[1] <= 0 or attributePlayer2[1] <= 0:
        break
    attributePlayer1[1] = attributePlayer1[1] - attributePlayer2[0]
    attributePlayer2[1] = attributePlayer2[1] - attributePlayer1[0]

if attributePlayer1[1] <= 0 and  attributePlayer2[1] <= 0:
    print("tie")
elif attributePlayer1[1] > attributePlayer2[1]:
    attributePlayer1 = list(map(str,attributePlayer1))
    print(namePlayer1,' '.join(attributePlayer1))
else:
    attributePlayer2 = list(map(str,attributePlayer2))
    print(namePlayer2,' '.join(attributePlayer2))
