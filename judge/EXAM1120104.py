"""
月餅檢測

描述
中秋節快到了，某家月餅工廠生產了許多盒月餅禮盒。其中，月餅禮盒可能會有
3顆一盒、6顆一盒、9顆一盒、12顆一盒裝四種數量；每顆月餅的單價有可能為
60,70,80元。月餅禮盒的售價即是數量乘以單價。
接著，每盒月餅皆有保存期限。若保存期限在
2023/10/14（含）以後，則表示月餅尚可保存，可以以原價賣出。若保存期限在
2023/10/7（含）以後但不滿足前述條件，則以8折賣出。若保存期限在 2023/9/27（含）以後但不滿足前述條件，則以6折賣出。若此盒月餅已過期，則不可賣出。
工廠在生產時會給每盒月餅「ID、保存期限、單顆月餅售價、月餅數量」的標籤。但保存期限、單顆月餅售價、月餅數量可能會被誤植，如保存期限並不是實際合理日期，單顆月餅售價並不是 60,70,80元或一盒月餅的數量不是 3,6,9,12顆等等。
你的需求是對於每盒月餅，若此盒月餅的保存期限、單顆月餅售價、月餅數量有誤植的情況，則將其回報，否則計算出此盒月餅的定價

輸入
輸入有多組測試資料。第一行為一個數字
t，為測試資料的數量。每組測試資料有一行，為{pack_id},{exp_date},{single_price},{amount}的格式，分別為一盒月餅的ID、保存期限、單顆月餅售價、月餅數量。其中pack_id為一字串，exp_date為一日期，格式為
y−m−d，single_price及amount為一非負整數。

輸出
對於每組測試資料輸出一行。

若月餅的標籤有誤植，則輸出{pack_id} has labeling problem!
若月餅標籤沒有誤植，且月餅已過期，則輸出{pack_id} has expired, it should not be sold.
若月餅標籤沒有誤植，且月餅未過期，則輸出{pack_id} should be sold at price {pack_price}.
其中pack_id為月餅的ID，pack_price為一盒月餅的售價，為一正整數。

輸入範例 1 
8
pack0,2023-9-26,80,7
pack1,2023-10-3,60,9
pack2,2023-10-25,65,9
pack3,2023-9-25,60,6
pack4,2023-10-7,80,6
pack5,2023-10-12,70,6
pack6,2023-10-3,60,12
pack7,2023-10-22,60,6

輸出範例 1
pack0 has labeling problem!
pack1 should be sold at price 324.
pack2 has labeling problem!
pack3 has expired, it should not be sold.
pack4 should be sold at price 384.
pack5 should be sold at price 336.
pack6 should be sold at price 432.
pack7 should be sold at price 360.

提示
1≤t≤8
y,m,d≥0
single_price,amount≥0
"""

import datetime

n = int(input())
originalDate = datetime.date(2023,10,14)
percent_eightDate = datetime.date(2023,10,7)
percent_sixDate = datetime.date(2023,9,27)

for index in range(n):
    s = input().split(",")
    pack_id = s[0]
    exp_date = s[1]
    single_price = int(s[2])
    amount = int(s[3])
    if amount not in [3, 6, 9, 12] or single_price not in [60, 70, 80]:
        print(f'{pack_id} has labeling problem!')
        continue

    date = exp_date.split('-')
    try:
        optimize_expdate = datetime.date(int(date[0]), int(date[1]), int(date[2]))
    except:
        print(f'{pack_id} has labeling problem!')
        continue
    price = single_price * amount
    if originalDate > optimize_expdate >= percent_eightDate:
        price *= 0.8
    elif percent_eightDate > optimize_expdate >= percent_sixDate:
        price *= 0.6
    elif percent_sixDate > optimize_expdate:
        print(f'{pack_id} has expired, it should not be sold.')
        continue

    print(f'{pack_id} should be sold at price {int(price)}.')
