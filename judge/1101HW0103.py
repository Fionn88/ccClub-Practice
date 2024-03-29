"""
小仔遊七福村

描述
小仔與兩個朋友到七福村遊玩，一般人的基本票價是 699 元，新竹市民(身分證開頭字母為 O)基本票價為 599 元，而七福村有兩種的門票優惠活動，兩個活動不能重複使用，題目給定三人的身分證字號，請你根據以下的活動資訊，幫他們計算他們入園總共最便宜要多少錢吧！
三人行團體優惠，若三人同性別，總金額可打八折，若三人不同出生地，總金額可打八折，兩者可同時使用，總金額無條件進位到整數位
好事七七，如果身分證字號中有每有一個 7 ，門票減 70 元，身分證字號後三位如果是 7 的倍數，門票減 77 元，兩者可同時使用

輸入
輸入共三行，
每行包含一字串，為身分證字號(一大寫字母＋九位數字)

輸出
輸出三人總共最少的入園價格

輸入範例 1
E234562347
E134234567
W212373219

輸出範例 1
1810

輸入範例 2
W134526774
A123465784 
O142333468

輸出範例 2
1279
"""

import math

def firstDiscount(idLst,cashLst):
    ans = sum(cashLst)
    if idLst[0][1] == idLst[1][1] == idLst[2][1]:
        ans = math.ceil(ans * 0.8)
    if idLst[0][0] != idLst[1][0] and idLst[1][0] != idLst[2][0] and idLst[0][0] != idLst[2][0]:
        ans = math.ceil(ans * 0.8)

    return ans

def secondDiscount(idLst,cashLst):
    ans = sum(cashLst)
    for id in idLst:
        if int(id[-3:]) % 7 == 0:
            ans -= 77
        for char in id:
            if char == "7":
                ans -= 70

    return ans
    
idLst = []
cashLst = []
for _ in range(3):
    id = input()
    if id[0] == "O":
        cashLst.append(599)
    else:
        cashLst.append(699)
    
    idLst.append(id)


print(min(firstDiscount(idLst,cashLst),secondDiscount(idLst,cashLst)))
