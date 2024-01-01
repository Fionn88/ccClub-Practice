"""
凱凱打疫苗 II

描述
隨著全台疫苗覆蓋率逐漸升高，越來越多民眾皆已接種新冠疫苗第一劑。
由於政府對於不同廠牌的疫苗接種第二劑的規定不同，若為 AZ、moderna、BNT 接種間隔為 10 週，高端則為 4 週。
請你寫一個程式，幫已經接種第一劑的民眾，計算最早可以接種第二劑的日期。

備註：
1. 為方便實作，請不用考慮閏年的狀況，測資並不會有此情形。
2. 為方便實作，請不用考慮會有跨年的狀況，兩劑的施打年份必會在同一年。
3. 請勿使用 datetime 相關 module 作答，否則不予計分。

輸入
輸入有兩行。
第一行為接種的疫苗廠牌。
第二行為接種第一劑的時間，格式為 YYYY/MM/DD（即年/月/日）。

輸出
輸出有一行，為最早可以接種第二劑的日期。

輸入範例 1
BNT
2021/09/12

輸出範例 1
2021/11/21

輸入範例 2
AZ
2021/03/05

輸出範例 2
2021/05/14

輸入範例 3
moderna
2021/05/02

輸出範例 3
2021/07/11

輸入範例 4
高端
2021/09/05

輸出範例 4
2021/10/03
"""

shot = input()
date = input().split("/")
date[1] = int(date[1])
months = {1:31 ,2:28 ,3:31 ,4:30 ,5:31 ,6:30 ,7:31 ,8:31 ,9:30 ,10:31 ,11:30 ,12:31}

count = 0
monthAllDay = 0
monthOfDay = months.get(date[1])
rest = monthOfDay - int(date[2])
monthAllDay += rest
if not shot == "高端":
    
    while monthAllDay < 70:
        count += 1
        nextMothOfDay = months.get(date[1] + count)
        monthAllDay += nextMothOfDay
        
    print(date[0]+"/"+f"{date[1]+count:02d}"+"/"+f"{70 - (monthAllDay - months.get(date[1]+count)):02d}")
else:
    while monthAllDay < 28:
        count += 1
        nextMothOfDay = months.get(date[1] + count)
        monthAllDay += nextMothOfDay
        
    print(date[0]+"/"+f"{date[1]+count:02d}"+"/"+f"{28 - (monthAllDay - months.get(date[1]+count)):02d}")
