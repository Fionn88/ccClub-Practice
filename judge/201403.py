"""
出裝備
描述

在很多線上遊戲裡面，玩家都可以使用金幣來購買裝備，並且可以透過合成裝備來取得更強力的裝備。
舉例來說：玩家可以消費 350 金幣購買一個把長劍，消費 450 金幣購買一個抗魔斗篷，並且額外花費 600 金幣將兩者合成為吸魔劍，總共花費 1400 金幣。

給定數個取得公式，和數個道具名稱，請輸出購買這些裝備所需的金幣數量。
輸入的第一部分為取得公式，其中第一行n為取得公式的數量，以下為n行取得公式。
取得裝備的公式格式如下：[裝備] [金額] [所需裝備1] [所需裝備2]...
若該道具可以直接購買，則所需裝備的位置會留空。
輸入的第二部分為想取得的道具，其中第一行 m 為想取得的道具數量，以下 m 行各包含一個字串為道具名稱。
道具的取得之間是獨立的，每一次所要花費的金幣並不會因為你上一次取得了這次所需的道具而改變。
輸出包含m行，每行為各個想購買的道具的總價。

測資保證一個道具只會有一個取得公式，保證想取得的道具公式都存在，並且保證所有所需裝備的取得公式也存在。


輸入
輸入的第一部分為 n+1 行，其中第一行 n 為取得公式的數量，以下為 n 行取得公式。
取得裝備的公式格式如下：[裝備] [金額] [所需裝備1] [所需裝備2]...

輸入的第二部分為 m+1 行，其中第一行 m 為想取得的道具數量，以下 m 行各包含一個字串為道具名稱。


輸出
輸出包含m行，每行為各個想購買的道具的總價。


輸入範例 1
3
長劍 350
抗魔斗篷 450
吸魔劍 600 長劍 抗魔斗篷
2
長劍
吸魔劍

輸出範例 1
350
1400

輸入範例 2 
2
a 100 b b b
b 1
2
a
b

輸出範例 2
103
1

來源
ccClub Judge
"""

def calculate_cost(item, formulas):
    if item not in formulas:
        return 0

    formula = formulas[item]
    cost = formula[0]


    for required_item in formula[1:]:
        cost += calculate_cost(required_item, formulas)

    return cost

n = int(input())
s = [input().split() for _ in range(n)]
m = int(input())
items = [input() for _ in range(m)]

product,formulas = {},{}

# 轉變資料結構
for item_data in s:
    item = item_data[0]
    cost = int(item_data[1])
    requirements = item_data[2:]
    formulas[item] = [cost] + requirements

for item in items:
    total_cost = calculate_cost(item, formulas)
    print(total_cost)
    