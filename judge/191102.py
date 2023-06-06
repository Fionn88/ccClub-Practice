"""
十二生肖
描述

我們想要知道每一年主要的生肖是什麼。


輸入
輸入一個西元年


輸出
輸出主要的生肖


輸入範例 1 
2019

輸出範例 1
Pig

輸入範例 2 
1911

輸出範例 2
Pig

輸入範例 3 
2015

輸出範例 3
Goat

提示
十二生肖順序分別如下：
Rat
Ox
Tiger
Rabbit
Dragon
Snake
Horse
Goat
Monkey
Rooster
Dog
Pig

來源
ccClub Judge
"""
def calculate_zodiac(year):
    zodiacs = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]
    index = (year - 1900) % 12
    zodiac = zodiacs[index]
    return zodiac

year = int(input())

zodiac = calculate_zodiac(year)

print(zodiac)
