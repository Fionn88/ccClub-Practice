"""
小明幾歲
描述

給定兩個數字，A 是小明的年紀，B 是小明哥哥跟他的年紀差

請以範例的格式輸出小明跟哥哥的年紀


輸入
輸入為兩行，各包含一個整數


輸出
輸出為兩行，各為一個字串


輸入範例 1 
5
7

輸出範例 1
I'm Little Ming, I'm 5 years old.
I'm Little Ming's brother, I'm 12 years old.

輸入範例 2 
20
23

輸出範例 2
I'm Little Ming, I'm 20 years old.
I'm Little Ming's brother, I'm 43 years old.

來源
ccClub Judge
"""
ming_age = int(input())
age_difference  = int(input())
print(f"I'm Little Ming, I'm {ming_age} years old.")
print(f"I'm Little Ming's brother, I'm {ming_age+age_difference} years old.")