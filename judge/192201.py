"""
檢查日期
描述

給定數個年月日所組成的字串，數量不一定，直到遇到「end」字串才結束。每遇到一個日期，請判斷該日期是否合法：若日期合法，輸出 OK；若不合法，請輸出 error。遇到 end 則結束程式，不用輸出。

每一行輸入的格式皆為：年, 月, 日

給定以下限制：

年月日皆為正整數
月份跟日期要合法
不用考慮閏年, 二月一律只有 28 天
note: 使用 while True


輸入
輸入不定行，每行皆為一個字串，格式為：「年, 月, 日」，其中年月日保證為整數（int）。最後一行為字串 "end"。


輸出
輸出與日期數量相同，內容依據日期是否合法為 "OK" 或是 "error"。


輸入範例 1 
2026, 47, 4
1997, 6, 4
end

輸出範例 1
error
OK

輸入範例 2 
1, 0, 1
8888, 8, 8
2019, 1, 32
2019, 2, 29
end

輸出範例 2
error
OK
error
error

來源
ccClub Judge
"""

date = []
while True:
    x = input()
    if x == 'end':
        break
    else:
        x = x.split(', ')
        date.append(x)

month2day = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

result = []
for d in date:
    if ((int(d[0]) > 0) and 1 <= int(d[1]) <= 12 and 1 <= int(d[2]) <= month2day[int(d[1])]) :
        result.append('OK')
    else:
        result.append('error')

for r in result:
    print(r)
