"""
[5-1] 阿緯換折價券
Description

本題為填空題。

cc 商店週年慶舉辦集點活動，集滿 10 點就可以換取 100 元的折價券。阿緯是 cc 商店的忠實顧客，手上有一些週年慶點數，請你幫阿緯算一下總共可以換得多少金額的折價券，以及最後剩餘的點數。


Input
輸入為 1 行，為阿緯有的點數數量


Output
輸出為 1 行，分別為阿緯可以換得的折價券金額與剩餘的點數，中間請用逗號隔開


Sample Input 1 
20

Sample Output 1
200,0

Sample Input 2 
17

Sample Output 2
100,7

Hint
請於作答區底線處，填入正確內容，完成題目要求。
作答時請將底線移除，替換成正確內容。
先計算手上的點數可以換得幾張折價券
每張折價券為100元，因此可以計算折價券的總金額
點數未滿10點，無法兌換折價券，即為剩餘點數

Source
ccClub Judge
"""

# 請在 __ 分別填入對應的運算符號
# points = int(input())
# coupon = points __ 10 * 100
# remain = points __ 10

# print(coupon, remain, __ = ',')

points = int(input())
coupon = points // 10 * 100
remain = points % 10

print(coupon, remain, sep = ',')





