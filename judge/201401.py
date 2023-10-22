"""
小甜的少女時代
描述

小甜暗戀隔壁的同學很久了，最喜歡在陽台看他打球的英姿。
她知道隔壁同學習慣看氣象預報，都會在他預計要打的「整段時間內都不下雨的機率」最高的時間去打球。
因為小甜跟他同班，所以知道他每天可以花多少時間打球。
給定她估計的有空時間及氣象預報中的每小時降雨機率，請幫她算一算她的偶像隔壁同學大約會在什麼時候去打球（去打球的起始時間）。


輸入
第一行為一個整數，代表隔壁同學當天有空的時間長度。
第二行為 24 個數字，為氣象局公布的 24 小時降雨機率(%)。


輸出
輸出為一個整數，代表隔壁同學會去打球的時間點


輸入範例 1 
3
14 67 35 38 37 41 77 97 9 57 99 77 100 91 56 46 57 82 27 34 19 34 4 7

輸出範例 1
21

輸入範例 2 
22
54 42 77 63 87 72 73 44 99 88 19 89 87 33 33 87 77 87 67 61 13 65 20 69

輸出範例 2
1

提示
考慮到大家離學機率的時間有點久了，此處「整段時間內都不下雨的機率」指的是每個小時不下雨的機率的乘積。

來源
ccClub Judge
"""

period = int(input())
possibility = [100-int(i) for i in input().split()]
max_cumulative_probability_period = (0, 0)
for i in range(24-period+1):
    cumulative_probability = 1
    for j in range(period):
        cumulative_probability *= possibility[i+j]
    if cumulative_probability > max_cumulative_probability_period[1]:
        max_cumulative_probability_period = (i, cumulative_probability)

print(max_cumulative_probability_period[0])
