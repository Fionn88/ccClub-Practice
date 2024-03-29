"""
凱凱玩 switch II

描述
除了棒球和看海之外，工作之餘凱凱最愛的休閒活動就是玩 switch 了。
為了避免沈迷，凱凱想紀錄自己玩遊戲的時間，並把他製成儀表板，時時刻刻提醒自己。
儀表板需要紀錄每個遊戲的累積遊玩時間，並提示說該月玩最久的遊戲為何，你能幫他完成這個程式嗎？

輸入
輸入有 d+1 行。
第一行為一個正整數 m，代表月份，該月份會有 d 天。
例如：一月有 31 天因此 m=1 時 d=31。為了方便，不考慮閏年，因此二月皆為 28 天。
第 2 至 d+1 行，每行包含兩個字串，分別代表遊戲名稱及遊玩時間，彼此間以逗號分開。
遊戲時間的格式為 HH:MM:DD 代表遊玩了 HH 小時 MM 分鐘 DD 秒，其中 0 <= MM, DD <= 60， 0 <= HH <= 100。

輸出
輸出有兩行。
第一行為一個字串，代表該月玩最久的遊戲名稱（保證是唯一解，不會有兩款遊戲並列第一）。
第二行為一個字串，代表該遊戲該月累積遊玩時間，格式為HH:MM:DD。

輸入範例 1 
9
健身環大冒險,00:53:38
健身環大冒險,00:58:48
eBASEBALL 實況野球 2020,01:22:38
eBASEBALL 實況野球 2020,01:21:44
eBASEBALL 實況野球 2020,00:15:52
eBASEBALL 實況野球 2020,00:02:51
eBASEBALL 實況野球 2020,01:26:40
集合啦！動物森友會,01:56:31
eBASEBALL 實況野球 2020,00:00:38
健身環大冒險,02:50:47
eBASEBALL 實況野球 2020,01:34:39
健身環大冒險,02:07:38
eBASEBALL 實況野球 2020,02:32:08
eBASEBALL 實況野球 2020,02:32:24
健身環大冒險,00:44:22
健身環大冒險,02:14:02
集合啦！動物森友會,02:20:47
eBASEBALL 實況野球 2020,01:25:37
健身環大冒險,00:32:43
eBASEBALL 實況野球 2020,03:25:31
集合啦！動物森友會,00:08:13
健身環大冒險,01:18:23
eBASEBALL 實況野球 2020,01:46:40
集合啦！動物森友會,01:36:39
eBASEBALL 實況野球 2020,03:57:40
eBASEBALL 實況野球 2020,03:16:09
eBASEBALL 實況野球 2020,00:37:09
健身環大冒險,00:46:49
eBASEBALL 實況野球 2020,00:15:41
eBASEBALL 實況野球 2020,01:57:45

輸出範例 1
eBASEBALL 實況野球 2020
27:51:46

輸入範例 2 
11
Pokemon 阿爾宙斯,03:57:38
健身環大冒險,02:32:01
eBASEBALL 實況野球 2020,03:54:02
健身環大冒險,01:33:38
eBASEBALL 實況野球 2020,03:39:55
Mario Kart 8 Deluxe,01:16:16
eBASEBALL 實況野球 2020,02:58:32
健身環大冒險,03:19:35
eBASEBALL 實況野球 2020,01:35:00
健身環大冒險,03:47:59
eBASEBALL 實況野球 2020,00:47:37
eBASEBALL 實況野球 2020,01:56:48
eBASEBALL 實況野球 2020,00:11:12
集合啦！動物森友會,00:24:12
eBASEBALL 實況野球 2020,00:30:12
Pokemon 阿爾宙斯,03:34:19
Pokemon 阿爾宙斯,01:13:48
健身環大冒險,00:36:14
集合啦！動物森友會,03:56:44
eBASEBALL 實況野球 2020,02:52:18
健身環大冒險,02:28:09
集合啦！動物森友會,01:40:03
健身環大冒險,02:08:13
eBASEBALL 實況野球 2020,01:58:02
eBASEBALL 實況野球 2020,02:26:44
Mario Kart 8 Deluxe,00:53:43
世界遊戲大全 51,02:51:13
健身環大冒險,02:03:51
Mario Kart 8 Deluxe,00:44:06
Pokemon 阿爾宙斯,03:20:33

輸出範例 2
eBASEBALL 實況野球 2020
22:50:22

輸入範例 3
1
Pokemon 阿爾宙斯,02:47:31
集合啦！動物森友會,00:50:53
健身環大冒險,01:07:34
Mario Kart 8 Deluxe,00:42:20
Pokemon 阿爾宙斯,03:06:10
健身環大冒險,03:58:25
健身環大冒險,01:02:53
集合啦！動物森友會,03:03:00
煮過頭 2,02:14:14
健身環大冒險,00:54:15
健身環大冒險,02:20:59
Pokemon 阿爾宙斯,02:44:16
eBASEBALL 實況野球 2020,03:15:55
eBASEBALL 實況野球 2020,00:19:00
eBASEBALL 實況野球 2020,00:50:58
集合啦！動物森友會,03:25:52
eBASEBALL 實況野球 2020,00:15:54
健身環大冒險,00:08:47
Mario Kart 8 Deluxe,03:24:59
Pokemon 阿爾宙斯,01:11:53
健身環大冒險,03:04:08
集合啦！動物森友會,02:26:39
Mario Party Superstars,01:31:17
eBASEBALL 實況野球 2020,03:07:39
薩爾達傳說 曠野之息,01:51:54
寶可夢 晶燦鑽石,02:18:24
Pokemon 阿爾宙斯,02:36:22
集合啦！動物森友會,01:19:56
eBASEBALL 實況野球 2020,02:15:29
Pokemon 阿爾宙斯,03:41:36
eBASEBALL 實況野球 2020,03:21:50

輸出範例 3
Pokemon 阿爾宙斯
16:07:48

提示
1 月到 12 月每個月的天數分別為：31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
"""

from collections import defaultdict
from datetime import timedelta

# 加總各個遊戲的遊玩時間
def sum_times_and_convert_to_hours(time_dict):
    total_times = {}
    for key, times in time_dict.items():
        total = sum((timedelta(hours=int(t.split(':')[0]), minutes=int(t.split(':')[1]), seconds=int(t.split(':')[2])) for t in times), timedelta())
        total_times[key] = total

    return total_times


monthDay = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
month = int(input())
game = defaultdict(list)
for _ in range(1,monthDay.get(month)+1):
    gameAndTime = input().split(",")
    game[gameAndTime[0]].append(gameAndTime[1])


sumTimeConvertToHours = sum_times_and_convert_to_hours(game)
maxTimeGame = ""
maxTime = timedelta(hours=0,minutes=0,seconds=0)

for key,value in sumTimeConvertToHours.items():
    if value > maxTime:
        maxTime = value
        maxTimeGame = key
print(maxTimeGame)
# ConvertToHours
print(f'{maxTime.days * 24 + maxTime.seconds // 3600:02d}:{(maxTime.seconds % 3600) // 60:02d}:{maxTime.seconds % 60:02d}')
