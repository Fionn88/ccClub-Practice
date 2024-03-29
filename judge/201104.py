"""
優惠券

描述
cc 超商最近發行了各式各樣卷面折價不等的優惠券，包含兩種不同的折價方式：
「$ a」：表示折價 a 元
「b」：表示打 b 折
每位客人都會依序使用五張優惠券，不限種類，在經過上述的五種折扣以後，得到的最終價格若有小數，採無條件捨去，若低於 0 元以 0 元計算，可以請你幫店員計算最後的結帳金額嗎？

輸入
輸入前五行為依序使用的優惠卷：
有 $ 開頭的行，若為[空格]a 表示折價 a 元，型態為字串以及整數。
沒有 $ 開頭的行，例：b，表示打 b 折，型態為整數。
第六行為原價，型態為整數。

輸出
輸出為一行，包含一個大於等於零的整數

輸入範例 1 
$ 27
7
8
3
$ 15
259

輸出範例 1
23

輸入範例 2 
$ 888
2
$ 572
$ 708
3
7957

輸出範例 2
40

來源
ccClub Judge
"""

sale = []
for _ in range(5):
    cost = input()
    sale.append(cost)

original_cost = int(input())
for price in sale:
    if "$" in price:
        price = price.split()
        original_cost -= int(price[1])
    else:
        original_cost = original_cost * int(price) / 10

if original_cost < 0:
    print(0)
else:
    print(int(original_cost))
