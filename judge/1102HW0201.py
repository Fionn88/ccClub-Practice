"""
新年購起來

描述
新的一年就是要買！東！西！
於是小雷決定要來當團購主，幫群組裡的大家一起謀福利，不過由於大家太太太踴躍了，數學差又討厭麻煩的小雷在計算團購數量時遇到了大問題，能請你幫他計算最後總共要訂多少的數量嗎？

注意：
英文、符號及數字都一定是半形
每個人輸入的習慣不一樣，有些人品項、加減符號、數字三者間會有空格，但確定的是數字間不會有空格（ex, +11 不會寫成 + 1 1）
有些人會手抖，輸入的頭尾可能會含有空格；另外有些人會輸錯項目的名稱，不計入
有些人會不小心發現自己的荷包其實沒有這麽厚，所以會反悔減掉一些數量
有些人會在群組裡講講幹話，所以不一定會有一定需要加減的數字，但代表團購的數字前都一定會有'+'或'-'
有些人就是故意來鬧的，會減掉比現有還要多的數量，這些數量直接忽略即可

輸入
第 1 列為小雷決定要團購的物品（物品間一律以頓號隔開）
第 2 列到 end 為止為團購時間內，小雷的親朋好友對於特定團購物品加加減減的數量

輸出
訂購的東西,數量
（開多少項目的訂購，就會有幾列的 output，且輸出順序與輸入時一致）
（數量最少就是 0，不會有負的）

輸入範例 1
巧克力、蝦餅
巧克力   +10
蝦餅 +3   
 巧克力 +2
蝦餅+2 
香草巧克力雪餅
巧克力 -7
end

輸出範例 1
巧克力,5
蝦餅,5

輸入範例 2
DVD、EGG roll、flower
DVD+1
   DVD-3
    DVD+  9
EGG roll -10
EGG roll +19   
end

輸出範例 2
DVD,10
EGG roll,19
flower,0
"""

target = input().split("、")
listItem, listNumber = [],[]
ans = {}
for i in target:
    ans[i] = 0
while True:
    s = input().strip()
    if s == "end":
        break
    for item in target:
        if item in s:
            for index,character in enumerate(s):
                if character == "+" or character == "-":
                    specificItem = s[:index].strip()
                    if specificItem in target and specificItem[0] == item[0]:
                        specificNumber = s[index:]
                        listItem.append(specificItem)
                        listNumber.append(specificNumber)
                        break
                elif character == "＋" or character == "－":
                    break
            
for index in range(len(listItem)):
    if listNumber[index][0] == "+":
        ans[listItem[index]] += int(listNumber[index][1:])
    else:
        save = ans.get(listItem[index]) - int(listNumber[index][1:]) 
        if save < 0:
            continue
        ans[listItem[index]] -= int(listNumber[index][1:])

for key,value in ans.items():
    print(f"{key},{value}")
