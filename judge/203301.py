"""
推薦系統

描述
商務上，常常會依據顧客的消費行為，推薦該顧客消費行為跟他類似的客戶購買的產品。
現在，給定我們有判斷相不相似的閾值以及顧客的購買紀錄，你可以推薦他們購買沒買過的產品嗎？

說明：
以範例一為例子。對凱文來說，小明跟他的相似度是 3/4 = 75% >= 50%，小美是 0/4 = 0% < 50%，小華是 2/4 = 50% >= 50%。
因此，我們推薦凱文小明買過但他沒買過的卡片跟機車，還有小華買過但凱文沒買過的番茄。
在輸出的第一行，我們先輸出凱文，接著依照商品出現的順序依序輸出要推薦給凱文的卡片、機車、番茄。
對小明來說，只有凱文跟他的相似度 3/5 = 60% >= 50%，因此我們推薦他凱文買過但他沒買過的鑰匙。
阿小美就是個邊緣人，我們先不理他。
小華跟小明和凱文的相似度是 2/3 = 67% >= 50%，因此我們推薦他凱文跟小明有買但他沒買的錢包、鑰匙、卡片、機車。

輸入
輸入為 n + 2 行。
第一行包含一個整數，為判斷相不相似的閾值。
中間 n 行中，每一行包含數個詞，以空白區隔。
最後一行輸入 end，代表輸入結束。

輸出
輸出為 n 行，代表對 n 個顧客的推薦商品。

輸入範例 1
50
凱文 電腦 手機 錢包 鑰匙
小明 電腦 手機 錢包 卡片 機車
小美 香蕉 蘿蔔
小華 電腦 手機 番茄
end

輸出範例 1
凱文 卡片 機車 番茄
小明 鑰匙
小美
小華 錢包 鑰匙 卡片 機車

輸入範例 2 
50
r S F C D U Q Z
l Q D F S B Z
q Q F U C D
c Z D F U B S Q C
end

輸出範例 2
r B
l C U
q S Z B
c

提示
可以試試使用 set！
"""

import collections

threshold = int(input())
customers,recommendations = {},{}


while True:
    s = input()
    if s == 'end':
        break
    s = s.split()
    customers[s[0]] = s[1:]
for customer, purchases in customers.items():
    recommendations[customer] = []  

    for other_customer, other_purchases in customers.items():
        if customer == other_customer:
            continue  

        intersection = set(purchases).intersection(other_purchases)  

        other_purchases_orderDict = collections.OrderedDict.fromkeys(other_purchases)
        purchases_orderDict = collections.OrderedDict.fromkeys(purchases)

        similarity = len(intersection) / len(purchases)*100 
        if similarity >= threshold:
            if not recommendations[customer]:
                recommendations[customer].extend(list(collections.OrderedDict.fromkeys(x for x in other_purchases_orderDict if x not in purchases_orderDict)))  
            else:
                for i in list(collections.OrderedDict.fromkeys(x for x in other_purchases_orderDict if x not in purchases_orderDict)):
                    if i not in recommendations[customer]:
                        recommendations[customer].append(i)  
            
for customer, recs in recommendations.items():
    if recs:
        print(customer, " ".join(recs))
    else:
        print(customer)
        