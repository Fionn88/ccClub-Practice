"""
小仔與怪奇商店

描述
小仔進到一家是以 26進位為標示價格的商店，全部皆以字母作為位數標示(A -> 1, z -> 26)，大小寫代表的數字相同，所以舉例來說，A = 1 元、B = 2 元、Aa = 27 元、AbA = 729 元，已知小仔最後購買商品的價格為三位數，小仔手上有面額 1000、500、100、50、10、1 的紙鈔與硬幣，請你以付出最少紙鈔或硬幣個數的付款方式，告訴小仔要如何付款給店家吧～

輸入
輸入共一行，包行一字串，由三個字母組成

輸出
輸出共一行
依 1000, 500, 100, 50, 10, 1 元的順序輸出小仔要付出的個數，中間以逗號相隔，如果不須付出就輸出 0

輸入範例 1 
ABC

輸出範例 1
0,1,2,0,3,1

輸入範例 2
BED

輸出範例 2
1,0,4,1,3,6

提示
以 sample 1 為例，
1(A) * 26^(2) + 2(B) * 26 + 3(C) = 731 (元)
最少紙鈔或硬幣個數的付款方式為
1000 元 0 個
500 元 1 個
100 元 2 個
50 元 0 個
10 元 3 個
1 元 1 個
"""

s = input().upper()
amount = 0

def calculate_min_payment(amount):
    denominations = [1000, 500, 100, 50, 10, 1]

    payment_counts = []

    for denomination in denominations:
        count = amount // denomination
        amount -= count * denomination
        payment_counts.append(count)

    return list(map(str,payment_counts))

for num,i in enumerate(reversed(s)):
    amount += (ord(i) - ord('A') + 1) * (26 ** num)

print(','.join(calculate_min_payment(amount)))
