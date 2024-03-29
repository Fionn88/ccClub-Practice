"""
二十六進位

描述
平常我們所使用的是十進位的數字系統，今天想請你幫忙將十進位的數字（保證是非負整數）轉為二十六進位制，並用 A~Z 代表 0~25。舉例來說，若我們要將數字 259 轉換為二十六進位：259 = 9 26¹ + 25 26°= JZ ( J -> 9 、Z -> 25 )

輸入
輸入為一行，包含一個整數

輸出
輸出為一行，包含一個字串

輸入範例 1 
7957

輸出範例 1
LUB

輸入範例 2 
259

輸出範例 2
JZ

來源
ccClub Judge
"""

def decimal_to_26_base(number):
    if number == 0:
        return 'A'

    digits = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    converted = ''
    while number > 0:
        remainder = number % 26
        converted = digits[remainder] + converted
        if remainder != 0:
            number -= 1
        number //= 26

    return converted

n = int(input())
print(decimal_to_26_base(n))
