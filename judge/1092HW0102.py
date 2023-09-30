"""
小仔蛋糕店
描述

小仔正在台大經營一家蛋糕店，分別販賣巧克力蛋糕、草莓蛋糕和草莓巧克力蛋糕，小仔每周製作 x 個蛋糕，其中巧克力蛋糕生產 m 個、草莓蛋糕生產 n 個、草莓巧克力蛋糕生產 x-m-n 個。

巧克力蛋糕所需要的材料有麵粉 90 克、雞蛋 3 顆、可可粉 0.5 包，草莓蛋糕所需的材料有麵粉 50 克、雞蛋 2 顆、草莓 10 顆，草莓巧克力所需的材料有，麵粉 120 克、雞蛋 4 顆、草莓 6 顆、可可粉 1.25 包。各個食材的價格如下：

可可粉每包價格 300 元，只能每包購買。
麵粉每包有 220 克，價格 50 元，只能每包購買。
雞蛋每 8 顆一盒，價格 76 元。只能每盒購買。
草莓 1 顆 3 元，每 10 顆 25 元。
請幫小仔計算出他花在食材上的成本是多少錢吧!


輸入
共 3 行，

第 1 行，包含一正整數 x，每週製作總蛋糕數。

第 2 行，包含一正整數 m，巧克力蛋糕生產數。

第 3 行，包含一正整數 n，草莓蛋糕生產數。


輸出
共 1 行，輸出包含兩整數，食材成本和買了幾盒雞蛋，中間用逗號隔開。

輸入範例 1 
5
1
2

輸出範例 1
1233,2

輸入範例 2 
10
4
4

輸出範例 2
2135,4
"""
import math
all = int(input())
chocolateCake = int(input())
strawberryCake = int(input())
strachocolateCake = all - chocolateCake - strawberryCake

cocoa = math.ceil(chocolateCake * 0.5 + strachocolateCake * 1.25) * 300
flour = math.ceil((chocolateCake * 90 + strawberryCake * 50 + strachocolateCake * 120) / 220) * 50
egg = math.ceil((chocolateCake * 3 + strawberryCake * 2 + strachocolateCake * 4) / 8) 
strawberry = (strawberryCake * 10 + strachocolateCake * 6) // 10 * 25 + (strawberryCake * 10 + strachocolateCake * 6) % 10 * 3
print(cocoa+flour+strawberry+egg*76,egg,sep=',')
