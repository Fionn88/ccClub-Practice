"""
省錢小作戰

描述
古時候木蘭為了準備上戰場，東市買駿馬，西市買鞍韉，南市買轡頭，北市買長鞭。現代人買東西為了省錢，也會在網路上查同一商品在不同的商店的價格和折扣，以找出最便宜的商店來下單或去現場買。勤儉持家的小明很節制，不會因為多買有更多折扣而多買，他同一種商品一定只會買 1 個。
現在有 4 間商店，小明調查好了想要買的東西在每一家的貨量、價格、信用卡回饋金、運費和折扣方案，寫成以下格式：
貨量 價格 信用卡回饋金 運費 折扣方案1,折扣方案2,折扣方案3
例如商品A 在 S商店的狀況寫成：6 600 5% 運費10 滿990打7折,滿400打85折,滿590打8折
在這個例子中，最後的金額為  
====
請至 judge 上查看
====
 
小明記錄的格式包含以下四種情況：
A. 如果該商店沒進這個商品或是現在沒有貨，貨量寫 0，且後面空白
0
B. 如果沒有信用卡回饋金，跳過不寫
6 600 運費10 滿990打7折,滿400打85折,滿590打8折
C. 如果網路商店免運費，或是實體商店不用運費，寫免運
6 600 5% 免運 滿990打7折,滿400打85折,滿590打8折
D. 如果沒有折扣方案，跳過不寫
6 600 5% 運費10

輸入
輸入為 4 行，4 行依序為商品在S商店、C商店、P商店、M商店的貨量、價格、信用卡回饋金和折扣方案。各項參數之間的分隔方式如下：
貨量 價格 信用卡回饋金 運費 折扣方案1,折扣方案2,折扣方案3

輸出
輸出為 1 行，為小明要去的賣最便宜的商店、多少錢，商店和金額之間以空白分隔。

輸入範例 1
99 2050 免運
0
5 1999 2.05% 免運
5 2000 運費120

輸出範例 1
P商店 1958

輸入範例 2
81530 99 免運 滿90打99折
6 599 2.5% 運費100 滿590打8折,滿300打79折,滿400打9折
6 100 運費100 滿590打8折
6 600 5% 運費10 滿300打6折,滿400打75折,滿5900000000打1折

輸出範例 2
S商店 98

提示
折扣只有 1 種格式，為「滿 x 打 y 折」
回饋金是根據商品售價折扣後再加上運費的數值來計算
請運算過程都先不要進位，算出最後數值之後再用 round() 奇進偶捨到整數位
保證沒有最後金額同樣數字的狀況
"""