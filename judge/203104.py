"""
小明買宵夜
描述

小明是個喜歡變化的強迫症患者，他喜歡在結束一天工作後，到他最喜歡的「天天不一樣」鹹酥雞攤，挑兩樣點心，恰恰好地把身上剩下的零錢花光，然後拎著恰恰好的鹹酥雞回家，完成美滿的一天。舉例來說，小明身上有 48 塊錢，菜單上有：

雞胗：8 元
雞冠：12 元
雞腿：40 元
雞屁股：14 元
則有強迫症的小明會想買一隻雞腿跟一個雞胗當作他的宵夜。

現在，給定小明身上剩下的零錢，以及「天天不一樣」鹹酥雞攤當日的菜單，請按菜單順序輸出他會點的兩樣點心。
注意：符合條件的點心組合會恰有一組。


輸入
輸入為三行。
第一行為菜單中各個點心名稱，以空格為分隔。
第二行為各點心對應的價錢，皆為正整數，以空格為分隔。
第三行包含一個整數，為小明身上的零錢總額。


輸出
輸出為一行，為小明會選擇的兩樣點心，以空格分隔。


輸入範例 1 
雞胗 雞冠 雞腿 雞屁股
8 12 40 14
48

輸出範例 1
雞胗 雞腿

輸入範例 2 
肉肉 菜菜 飯飯 菜飯 韓國魚
2 7 11 15 143
9

輸出範例 2
肉肉 菜菜
"""
# Time Limit Exceeded
# from itertools import combinations
# menu = input().split()
# prices = list(map(int,input().split()))
# budget = int(input())
# ans = []
# ansPrice = []
# for r in range(1, len(prices) + 1):
#     for combo in combinations(prices, r):
#         if sum(combo) == budget:
#             ansPrice = combo
#             break

# for result in ansPrice:
#     ans.append(menu[prices.index(result)])

# print(' '.join(ans))


# Time Complexity：O(nlogn)
# Space Complexity：O(1)
# Approach 1：Find the target price using Two Pointer.
menu = input().split()
prices = list(map(int,input().split()))
budget = int(input())

combined = list(zip(prices, menu))
sorted_combined = sorted(combined)
sorted_prices, sorted_items = zip(*sorted_combined)

l = 0
r = len(menu) -1
while l < r:
    if sorted_prices[l] + sorted_prices[r] == budget:
        indexLeft = prices.index(sorted_prices[l])
        indexRight = prices.index(sorted_prices[r])
        if indexLeft < indexRight:
            print(menu[prices.index(sorted_prices[l])],menu[prices.index(sorted_prices[r])])
        else:
            print(menu[prices.index(sorted_prices[r])],menu[prices.index(sorted_prices[l])])     
        
        break
    elif sorted_prices[l] + sorted_prices[r] < budget:
        l += 1
    else:
        r -= 1