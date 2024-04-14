"""
阿偉的玩具店

描述
阿偉是玩具店的老闆，然而倉庫裡凌亂的陳設讓阿偉決定來個大整理，阿偉決定重新清點所有玩具的數量，並依據
[貨品數量(由多到少), 貨名長短(由短至長), 貨名第一次出現順序(由早至晚)] 來重新整理貨物，另外為了支持本土商家，舶來品(名字有英文者)一律放在本土玩具的後面，你可以幫阿偉規劃出新的商店陳設嗎？

輸入
輸入為n+1行
前n行為阿偉點到的玩具，每點到一次表示該商品數量+1
第n+1行為end，表示程式終止。

輸出
請依照
[['玩具1', 玩具1數量], ['玩具2', 玩具2數量], ...]
進行輸出，排序請依照上述指示。

輸入範例 1
Huggy Wuggy
Huggy Wuggy
Huggy Wuggy
Mommy Longlegs
Kissy Missy
波比
end

輸出範例 1
[['波比', 1], ['Huggy Wuggy', 3], ['Kissy Missy', 1], ['Mommy Longlegs', 1]]

輸入範例 2
DogDay
CatNap
PickyPiggy
CraftyCorn
BubbaBubbaphant
KickinChicken
HoppyHopscotch
end

輸出範例 2
[['DogDay', 1], ['CatNap', 1], ['PickyPiggy', 1], ['CraftyCorn', 1], ['KickinChicken', 1], ['HoppyHopscotch', 1], ['BubbaBubbaphant', 1]]
"""

from collections import defaultdict
import re

pattern = re.compile(r"[a-zA-Z]")
def custom_sort(lst):
    if pattern.search(lst[0]) is not None:
        return True
    else:
        return False
productDict = defaultdict(int)
productListSet = list()
while True:
    product = input()
    if product == 'end':
        break
    productDict[product] += 1
    if not productListSet:
        productListSet.append(product)
    elif product in productListSet:
         continue
    else:
         productListSet.append(product)

ans = []
productDict = dict(sorted(productDict.items(), key=lambda item: (-custom_sort(item[0]),item[1],-len(item[0])), reverse=True))

for key, item in productDict.items():
    ans.append([key,item])
print(ans)
