"""
日期計算
描述

給定一個日期以及一個整數n，請計算從這個日期往後n天的日期。n可能為正也可能為負。


輸入
輸入為兩行，第一行包含一個日期，年月日以空白為間隔；第二行則是包含一個整數n


輸出
輸出為一行，包含一個日期，格式為 YYYY-MM-DD


輸入範例 1 
2020 1 23
7

輸出範例 1
2020-01-30

輸入範例 2 
1911 3 12
-51

輸出範例 2
1911-01-20

提示
建議使用 datetime 這個模組

來源
ccClub Judge
"""

# ================= 此做法未考慮到三個數字的西元年，會出現Runtime Error =====================
# from datetime import datetime, timedelta

# date_str = input()
# n = int(input())
# date = datetime.strptime(date_str, '%Y %m %d')
# new_date = date + timedelta(days=n)
# formatted_date = new_date.strftime('%Y-%m-%d')
# print(formatted_date)

from datetime import datetime, timedelta

year, month, day = map(int, input().split())
n = int(input())
date = datetime(year, month, day)
new_date = date + timedelta(days=n)
print(new_date.strftime('%Y-%m-%d'))
