"""
小仔可不可
描述

小仔喜歡喝一分糖紅茶和奶茶，一杯紅茶含咖啡因 50 mg 和含糖 10 g，一杯奶茶含咖啡因含 20 mg 和含糖 30 g，小仔的營養師建議他一天的咖啡因攝取不超過 300 mg，三天不超過 700 mg，糖一天攝取不超過 60 g，三天不超過 150 g，小仔一天只會喝一種飲料但杯數不定(最多 99 杯)，他提出了他後三天的喝飲料計畫，請你幫他看可不可吧！


輸入
共三行

每行包含一字串，第 1 位 "M" 表示奶茶、"B" 表示紅茶，後面數位代表喝的杯數


輸出
共一行，包含一字串

如果計畫可行輸出可

反之，輸出不可


輸入範例 1 
B2
M1
B5

輸出範例 1
可

輸入範例 2 
B4
M2
M20

輸出範例 2
不可
"""

content = {"B":[50,10],"M":[20,30]}
sugar_total = 0
caffeine_total =0

for i in range(3):
    caffeine = 0
    sugar = 0
    drinkAndCup = input()

    cup = int(drinkAndCup[1:])
    drink = drinkAndCup[0]

    caffeine += content.get(drink)[0] * cup
    sugar += content.get(drink)[1] * cup

    if caffeine > 300 or sugar > 60:
        print("不可")
        exit()

    sugar_total += sugar
    caffeine_total += caffeine

if caffeine_total > 700 or sugar_total > 150:
    print("不可")
    exit()

print("可")
