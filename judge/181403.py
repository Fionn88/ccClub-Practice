"""
最大時間

描述
給定四個數字，請將這四個數字排列成 hh:mm 的格式（24小時制），使其排出的時間最大。

輸入
輸入有一行，包含四個非負整數，數字間以空格分開。

輸出
輸出為一行，包含一個字串，格式為 hh:mm（24小時制）。
若無法排成時間格式則輸出 error。

輸入範例 1 
1 2 8 9

輸出範例 1
19:28

輸入範例 2 
1 2 0 8

輸出範例 2
21:08

輸入範例 3 
2 4 6 8

輸出範例 3
error

來源
ccClub Judge
"""

s = input().split()
backup_s = s.copy()
all_hour,all_minute = [],[]
posible_hour,posible_minute = [],[]
posiible_ans = []

for i in range(0,24):
    if len(str(i)) == 1:
        all_hour.append('0'+str(i))
    else:
        all_hour.append(str(i))

for i in range(0,60):
    if len(str(i)) == 1:
        all_minute.append('0'+str(i))
    else:
        all_minute.append(str(i))


def theMaxTime(number):
    for index1,j in enumerate(number):
        for index2,k in enumerate(number):
            if index1 == index2:
                continue
            else:
                if j+k in all_hour and j+k not in posible_hour:
                    posible_hour.append(j+k)
                if j+k in all_minute and j+k not in posible_minute:
                    posible_minute.append(j+k)
    posible_hour.sort(reverse=True)
    posible_minute.sort(reverse=True)
    for hour in posible_hour:
        for minute in posible_minute:
            s = backup_s.copy()
            count = 0
            for i in hour:
                try:
                    s.remove(i)
                except:
                    count += 1
                    break
            for j in minute:
                try:
                    s.remove(j)
                except:
                    count += 1
                    break
            if count == 0:
                posiible_ans.append(hour+":"+minute)
    if not posiible_ans:
        return "error"
    ans_hour = []
    for i in posiible_ans:
        ans_hour.append(i.split(":")[0])
    for index,i in enumerate(posiible_ans):
        if max(ans_hour) in i:
            return posiible_ans[index]

print(theMaxTime(s))
