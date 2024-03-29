"""
小明管倉庫

描述
小明是一位倉儲管理人員，其中一項工作內容是要確保公司的存貨數量可以隨時滿足出貨速度。因為公司客戶的需求量還蠻固定的，可以大致推算星期一至星期日的商品需求量，所以小明想寫個可以決定何時需要進貨的程式。已知初始存貨、商品下訂後所需的到貨天數以及商品周一至周日的出貨量，請算出小明該進貨的時間。

輸入
輸入為兩行，第一行為兩個正整數，分別為初始存貨與下訂後的到貨天數，數字間以逗號作為間隔；
第二行為七個正整數，代表周一至周日的出貨量，數字間也以一個逗號作為間隔

輸出
請輸出一個正整數，為小明該進貨的時間點（第一天固定為周一）

輸入範例 1 
100,3
30,10,8,7,10,15,15

輸出範例 1
5

輸入範例 2 
200,1
10,10,10,10,10,25,25

輸出範例 2
14

提示
若初始存貨 = 100，進貨天數 = 3，出貨量分別為 30,10,8,7,10,15,15
第一天結束存貨剩 70
第二天結束存貨剩 60
.
.
.
第八天存貨會小於出貨量（5 < 30）
所以小明該在第 5 天下訂，補足存貨
"""

stock, day = map(int,input().split(','))
spend = input().split(',')

res = 0
count = 0
index = 0
while res <= stock:
    res += int(spend[index])
    count += 1
    index += 1 

    if index >= len(spend):
        index = 0
count = count - day
print(count)
