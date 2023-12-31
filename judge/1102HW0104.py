"""
吃貨茜茜

描述
茜茜家附近的「大衛王吃到飽餐廳」永遠只提供 3 樣東西，每天都不一樣。
餐廳的計費規定如下:

每人收費 450 元，提供顧客 90 分鐘的吃到飽時間。
如果顧客單次到店，不論品項，只要總計吃超過 20 份( 含 )，即可打 8 折 ; 若超過 30 份 ( 含 )則會再贈送價值＄900 的龍蝦一隻。
茜茜是常客，然而他胃的容量有限，為了要吃到物超所值，茜茜決定從事以下吃法:
如果能吃的話就吃最貴的，如果胃的容量塞不下最貴，就跳過不吃，改吃次貴的 ; 再塞不下就改吃次次貴的，如果剩餘的胃容量塞不下任何東西那就只好走人了。
請你幫茜茜看看，依照他今天胃的容量，他應該各吃幾道這三樣料理，又，他在這間店「賺了多少」(茜茜實際吃這一餐花的錢-餐費)

輸入
共有 7 行，
第 1 行有一個正數，代表茜茜今天胃的容量
接下來六行的第 i*2 行 ，為第 i 份食物的"價格"(Pi) ; 而第 ( i*2+1) 行，為吃第 i 份食物"佔胃的容量"(Ci)，其中 P1 > P2 > P3
第 2 行有一個正數，P1
第 3 行有一個正數，C1
第 4 行有一個正數，P2
第 5 行有一個正數，C2
第 6 行有一個正數，P3
第 7 行有一個正數，C3

輸出
共 2 行，
第 1 行，以空白分隔依序輸出每道料理要吃幾份，如果無法吃就輸出 0
第 2 行，輸出茜茜物超所值的量

輸入範例 1 
720
180
7
140
7
100
1

輸出範例 1
102 0 6
19500.0

輸入範例 2 
100
150
30
50
5
10
10

輸出範例 2
3 2 0
100.0

提示
以 sample 1 來說，
茜茜胃的容量有 720 mL，餐廳今天提供的食物有:
干貝＄180 / 份，吃每顆干貝會佔掉 7 mL 的胃容量；明蝦＄140 / 份，吃每份明蝦會佔掉 7 mL 的胃容量；鮭魚片＄100 / 份，吃每份的鮭魚片會佔掉 1 mL 的胃容量
依照題目的規定，茜茜先從最貴的干貝開始吃，貴的吃越多越好，因此最多可以吃掉 102 份干貝，胃剩餘的容量為 720 - 102*7 = 6，因為剩餘的胃容量無法吃明蝦(需要 7 mL 的胃容量)
因此跳過不吃明蝦，最後的胃容量剛好可以點 6 份生鮭魚。因此，茜茜應該要吃 102 干貝、0 明蝦、6 鮭魚片，因為總份數 (102+6) 超過 30 盤，因此可以再獲得龍蝦一隻。
茜茜今天賺到的就是吃掉的總額 [ (102*180+100*6+額外獲得的龍蝦) - (450 再打 8 折) ]
"""

num = int(input())
out = []
cost = 0
meal_expenses = 450
for i in range(3):
    p = int(input())
    c = int(input())
    part = num // c
    out.append(part)
    if part > 0:
        cost += part*p
        num -= part*c
if sum(out) >= 20:
    meal_expenses *= 0.8
    if sum(out) >= 30:
        cost += 900

out = list(map(str,out))
print(" ".join(out))
print(float(cost-meal_expenses))
