"""
五十二進位
描述

平常我們所使用的是十進位的數字系統，今天想請你幫忙將十進位的數字（保證是非負整數）轉為五十二進位制，並用 A~Z 代表 0~25，a~z 代表 26~51。

舉例來說：我們要將 5566 轉成五十二進位，5566 = 2 * 52^2 +3 * 52^1 +2 * 52^0 = CDC (C=>2，D=>3)。


輸入
輸入為一行，包含一個非負整數。


輸出
輸入為一行，包含一個字串。


輸入範例 1 
5566

輸出範例 1
CDC

輸入範例 2 
1590602615

輸出範例 2
EJcQfr
"""

def decimal_to_52_base(number):
    if number == 0:
        return 'A'

    digits = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

    converted = ''
    while number > 0:
        remainder = number % 52
        converted = digits[remainder] + converted
        if remainder != 0:
            number -= 1
        number //= 52
    return converted

n = int(input())
print(decimal_to_52_base(n))
