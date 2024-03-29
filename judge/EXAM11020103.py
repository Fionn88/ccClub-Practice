"""
凱凱玩 switch

描述
除了棒球和看海之外，工作之餘凱凱最愛的休閒活動就是玩 switch 了。
為了避免沈迷，凱凱想紀錄自己玩遊戲的時間，並把他製成儀表板，時時刻刻提醒自己，你能幫他完成這個程式嗎？

輸入
輸入有 d+1 行。
第一行為一個正整數 m，代表月份，該月份會有 d 天。
例如：一月有 31 天因此 m=1 時 d=31。為了方便，不考慮閏年，因此二月皆為 28 天。
第 2 至 d+1 行，每行包含兩個字串，分別代表遊戲名稱及遊玩時間，彼此間以逗號分開。
遊戲時間的格式為 HH:MM:DD 代表遊玩了 HH 小時 MM 分鐘 DD 秒，其中 0 <= MM, DD <= 60， 0 <= HH <= 100。

輸出
輸出有兩行。
第一行為一個整數 n，代表該月玩了幾款遊戲。
第二行為一個字串，代表該月的總遊戲時間。

輸入範例 1
8
eBASEBALL 實況野球 2020,00:26:31
eBASEBALL 實況野球 2020,01:13:13
eBASEBALL 實況野球 2020,00:40:16
eBASEBALL 實況野球 2020,02:34:16
集合啦！動物森友會,01:27:33
eBASEBALL 實況野球 2020,02:37:42
健身環大冒險,03:50:03
健身環大冒險,02:59:18
集合啦！動物森友會,01:57:38
eBASEBALL 實況野球 2020,01:00:05
eBASEBALL 實況野球 2020,01:26:40
健身環大冒險,02:50:45
eBASEBALL 實況野球 2020,02:45:03
eBASEBALL 實況野球 2020,02:06:06
eBASEBALL 實況野球 2020,02:31:24
集合啦！動物森友會,02:25:05
eBASEBALL 實況野球 2020,00:43:22
eBASEBALL 實況野球 2020,02:36:44
eBASEBALL 實況野球 2020,03:55:32
健身環大冒險,00:27:47
健身環大冒險,03:50:45
健身環大冒險,03:17:12
eBASEBALL 實況野球 2020,01:44:18
eBASEBALL 實況野球 2020,01:03:12
eBASEBALL 實況野球 2020,00:19:16
集合啦！動物森友會,03:24:53
eBASEBALL 實況野球 2020,00:32:31
健身環大冒險,01:47:36
eBASEBALL 實況野球 2020,01:28:56
eBASEBALL 實況野球 2020,00:05:47
eBASEBALL 實況野球 2020,02:01:57

輸出範例 1
3
60:11:26

輸入範例 2
4
eBASEBALL 實況野球 2020,02:54:10
eBASEBALL 實況野球 2020,03:15:19
Pokemon 阿爾宙斯,01:49:45
eBASEBALL 實況野球 2020,01:38:25
eBASEBALL 實況野球 2020,02:40:52
eBASEBALL 實況野球 2020,02:08:17
eBASEBALL 實況野球 2020,03:40:16
Pokemon 阿爾宙斯,00:06:14
eBASEBALL 實況野球 2020,01:32:17
集合啦！動物森友會,01:46:58
健身環大冒險,02:17:43
Mario Kart 8 Deluxe,00:55:50
eBASEBALL 實況野球 2020,01:28:42
Pokemon 阿爾宙斯,01:45:59
eBASEBALL 實況野球 2020,00:22:05
eBASEBALL 實況野球 2020,00:02:34
eBASEBALL 實況野球 2020,03:23:19
eBASEBALL 實況野球 2020,00:31:58
Pokemon 阿爾宙斯,01:31:27
健身環大冒險,03:47:14
eBASEBALL 實況野球 2020,02:52:39
Pokemon 阿爾宙斯,03:35:08
eBASEBALL 實況野球 2020,00:30:31
eBASEBALL 實況野球 2020,03:39:28
Mario Kart 8 Deluxe,01:25:07
eBASEBALL 實況野球 2020,01:50:37
Mario Kart 8 Deluxe,00:17:58
健身環大冒險,00:47:54
Mario Party Superstars,00:44:55
健身環大冒險,00:44:07

輸出範例 2
6
54:07:48

輸入範例 3
12
健身環大冒險,02:01:48
健身環大冒險,01:33:43
Pokemon 阿爾宙斯,00:30:43
Mario Kart 8 Deluxe,01:46:47
Pokemon 阿爾宙斯,01:27:31
Pokemon 阿爾宙斯,00:41:27
Mario Party Superstars,03:02:22
健身環大冒險,00:11:37
eBASEBALL 實況野球 2020,02:05:22
集合啦！動物森友會,02:50:40
Mario Kart 8 Deluxe,03:31:12
Mario Kart 8 Deluxe,03:04:25
健身環大冒險,03:15:41
eBASEBALL 實況野球 2020,03:39:50
集合啦！動物森友會,01:05:01
健身環大冒險,00:09:50
薩爾達傳說 曠野之息,02:57:00
集合啦！動物森友會,00:49:52
Pokemon 阿爾宙斯,02:18:40
世界遊戲大全 51,01:41:08
Mario Kart 8 Deluxe,00:25:51
寶可夢 晶燦鑽石,01:02:43
煮過頭 2,02:44:07
集合啦！動物森友會,02:28:32
Mario Kart 8 Deluxe,03:39:01
eBASEBALL 實況野球 2020,02:06:27
Mario Kart 8 Deluxe,01:09:31
世界遊戲大全 51,00:54:50
eBASEBALL 實況野球 2020,03:09:45
Pokemon 阿爾宙斯,00:01:59
Pokemon 阿爾宙斯,01:46:56

輸出範例 3
10
58:14:21

提示
1 月到 12 月每個月的天數分別為：31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
sample input 1 中，只出現了「eBASEBALL 實況野球 2020」、「集合啦！動物森友會」、「健身環大冒險」三款遊戲，因此輸出 3，並統計遊玩總時數輸出。
"""

from collections import defaultdict
from datetime import timedelta

# 加總各個遊戲的遊玩時間
def sum_times_and_convert_to_hours(time_dict):
    total_times = {}
    for key, times in time_dict.items():
        total = sum((timedelta(hours=int(t.split(':')[0]), minutes=int(t.split(':')[1]), seconds=int(t.split(':')[2])) for t in times), timedelta())

        total_hours = total.days * 24 + total.seconds // 3600
        total_minutes = (total.seconds % 3600) // 60
        total_seconds = total.seconds % 60
        total_times[key] = f"{total_hours:02d}:{total_minutes:02d}:{total_seconds:02d}"
    return total_times

# 加總所有遊戲的總時間
def sum_all_times(time_dict):
    total = timedelta()
    for time in time_dict.values():
        hours, minutes, seconds = map(int, time.split(':'))
        total += timedelta(hours=hours, minutes=minutes, seconds=seconds)

    total_hours = total.days * 24 + total.seconds // 3600
    total_minutes = (total.seconds % 3600) // 60
    total_seconds = total.seconds % 60
    return f"{total_hours:02d}:{total_minutes:02d}:{total_seconds:02d}"


monthDay = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
month = int(input())
game = defaultdict(list)
for _ in range(1,monthDay.get(month)+1):
    gameAndTime = input().split(",")
    game[gameAndTime[0]].append(gameAndTime[1])


sumTimeConvertToHours = sum_times_and_convert_to_hours(game)
sumAllTimes = sum_all_times(sumTimeConvertToHours)
print(len(sumTimeConvertToHours))
print(sumAllTimes)
