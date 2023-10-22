"""
轉生到古羅馬文明
描述

小明最近時光穿越到了古羅馬文明，聰明的他很被城邦裡的人收留，並且被請去記帳

記帳的過程他發現他們的計數系統跟現在不太一樣，請問你能幫他做一些轉換嗎？

羅馬數字規則可參閱`https://zh.wikipedia.org/wiki/%E7%BD%97%E9%A9%AC%E6%95%B0%E5%AD%97`，數字沒有上限（可允許多個 M）


輸入
輸入為一正整數


輸出
輸出為一串字串代表對應的羅馬數字，由 I, V, X, L, C, D, M 組成


輸入範例 1 
3

輸出範例 1
III

輸入範例 2 
58

輸出範例 2
LVIII

輸入範例 3 
1994

輸出範例 3
MCMXCIV
"""

def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    roman_num = ''
    i = 0
    while  num > 0:
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1
    return roman_num

number = int(input())
roman = int_to_roman(number)
print(roman)
