"""
凱凱的出門準備
描述

凱凱是一個討厭麻煩的人，他總是早上吃早餐看氣象預報時才決定出門要帶什麼，請依照不同的天氣狀況提醒他出門要帶的物品吧。



天氣預報會包含以下資訊：

1. 氣溫：包含當天攝氏氣溫的最高溫及最低溫。

2. 降雨機率：當天的降雨機率，若小於等於 20% 視為晴天，大於等於 70% 視為雨天，否則視為陰天。

3. 紫外線指數：當天的紫外線指數，0-2 為低量級，3-5 為中量級，6-7 為高量級，8-10 為過量級，11+ 為危險級。



根據氣象預報的結果，凱凱會考慮攜帶以下物品：

1. 若為雨天則攜帶「雨傘」。

2. 不論晴天、陰天、或雨天，若紫外線指數達高量級或更高量級，則攜帶「雨傘」。

3. 若為陰天且最低溫小於等於 20 度則攜帶「棒球帽」，若平均溫度（即最高溫和最低溫相加平均）小於等於 18 度，則攜帶「毛帽」。若攜帶毛帽則不帶棒球帽，只會帶一個帽子出門。

4. 若紫外線指數達中量級或更高量級且為晴天，則攜帶「太陽眼鏡」。



請根據凱凱訂下的條件，以及當天氣象預報的內容，提醒他該帶出門的物品。


輸入
輸入有三行。

第一行為兩個整數 H, L，數字間以空格分開，代表當天氣溫的最高溫及最低溫，保證 H >= L。

第二行為一個 0-100 間的整數，代表該天的降雨機率。

第三行為一非負整數，代表當天的紫外線指數。


輸出
輸出有一行，代表需要攜帶的物品。

請依照「雨傘」、帽子（「棒球帽」或「毛帽」）、「太陽眼鏡」順序輸出，物品間以空格分開。

若沒有需要帶出門的物品，則輸出「空手出門」


輸入範例 1 
30 20
90
10

輸出範例 1
雨傘

輸入範例 2 
34 21
20
10

輸出範例 2
雨傘 太陽眼鏡

輸入範例 3 
34 31
40
2

輸出範例 3
空手出門

輸入範例 4 
15 8
20
8

輸出範例 4
雨傘 毛帽 太陽眼鏡
"""

def sunglasses(rainrateAug,rayAug):
    if rainrateAug  <= 20 and rayAug >= 3:
        return True
    else:
        return False

def umbrella(rainrateAug,rayAug):
    if rainrateAug  >= 70 or rayAug >= 6:
        return True
    else:
        return False

def hat(rainrateAug,hAug, lAug):
    avg = (hAug + lAug) / 2
    if avg <= 18:
        return [True,"毛帽"]
    elif rainrateAug > 20  and rainrateAug < 70 and lAug <= 20:
        return [True,"棒球帽"]
    else:
        return [False]
    
h, l = map(int,input().split())
rainrate = int(input())
ray = int(input())
    
if umbrella(rainrate,ray):
    print("雨傘",end=" ")
if hat(rainrate,h, l)[0]:
    print(hat(rainrate,h, l)[1],end=" ")
if sunglasses(rainrate,ray):
    print("太陽眼鏡")
if not (umbrella(rainrate,ray) or hat(rainrate,h, l)[0] or sunglasses(rainrate,ray)):
    print("空手出門")
    