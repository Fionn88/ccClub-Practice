"""
小甜網購
描述

小甜是個喜歡在網路上逛街的少女，但由於她還是個窮學生，所以買東西幾乎都要湊優惠卷。但她最常逛的購物網的優惠卷都是限時限量的，所以他必需在算好時間搶優惠卷。然而她悲劇的發現，她的電腦和購物網的時間總是差了好幾秒，所以總是搶不到最好的優惠卷。但有一天她找到一個地方可以看到網站時間的 timestamp。請你幫她寫一個程式算算她應該在自己電腦的什麼時間搶票？


輸入
第一行為小甜電腦當前的時間，第二行為購物網會可以搶優惠卷的時間，第三行為小甜找到的購物網的當前 timestamp。


輸出
一行為小甜的電腦應該要搶優惠卷的時間。


輸入範例 1 
2022-06-06 06:56:50.420278+0800
2022-06-06 17:16:13.420278+0800
1654469806.209551

輸出範例 1
2022-06-06 17:16:17.631005+08:00

輸入範例 2 
2020-11-17 00:43:06.171063+0800
2020-11-17 05:11:04.171063+0800
1605545002.954017

輸出範例 2
2020-11-17 05:10:47.388109+08:00

提示
使用 datetime 中的 datetime, timezone, timedelta
datetime.datetime 中的 strptime, fromtimestamp
"""

# Wrong Answer
from datetime import datetime, timezone, timedelta

def compute_desired_time(computer_time, shopping_time, timestamp):
    computer_time = datetime.strptime(computer_time, "%Y-%m-%d %H:%M:%S.%f%z")
    shopping_time = datetime.strptime(shopping_time, "%Y-%m-%d %H:%M:%S.%f%z")
    website_time = datetime.fromtimestamp(timestamp, timezone.utc)
    time_difference = website_time - shopping_time
    
    desired_time = computer_time + time_difference
    desired_time_str = desired_time.strftime("%Y-%m-%d %H:%M:%S.%f%z")
    
    return desired_time_str

computer_time = input()
shopping_time = input()
timestamp = float(input())

print(compute_desired_time(computer_time, shopping_time, timestamp))
