"""
[9-1] 字串擷取
Description

在進行自動化網路擷取資料的過程中，常常會遇到一串文字之中只有一部份是自己想要的，或是要把文字資料整理成表格的狀況。強強最近想要報名網路課程，如果課程額滿了就不能報名，課程的價格也是要考量的點，所以這些資料都需要記錄下來，舉例來說，他想要將'A課程 報名人數/招生人數/費用:60/100/600''B課程 報名人數/招生人數/費用:23/30/200'整理成字典{'A課程': [60, 100, '60%', '600'], 'B課程': [23, 30, '77%', '200']}其中，招生人數後面的百分比是報名的進度，100% 表示額滿。

以下是他的程式碼，請將程式碼的錯誤去除。


Input
無。


Output
輸出為 1 行，為字典內容。


Sample Input 1 

 
Sample Output 1
{'A課程': [60, 100, '60%', '600'], 'B課程': [23, 30, '77%', '200']}

Hint
注意TypeError、ValueError、IndexError

Source
ccClub Judge
"""
s = ['A課程 報名人數/招生人數/費用:60/100/600', 'B課程 報名人數/招生人數/費用:23/30/200']
course = {}

for i in range(len(s)):
#     sign_up_num = s[i].split(':')[1].split('/')[0]
#     admissions_num = s[i].split(':')[1].split('/')[1]
#     fee = s[i].split(':')[1].split('/')[3]
#     schedule = round(sign_up_num / admissions_num * 100) + '%'
    sign_up_num = int(s[i].split(':')[1].split('/')[0])
    admissions_num = int(s[i].split(':')[1].split('/')[1])
    fee = s[i].split(':')[1].split('/')[2]
    schedule = str(round(sign_up_num / admissions_num * 100)) + '%'

    course[s[i].split()[0]] = [sign_up_num, admissions_num, schedule, fee]
    
print(course)

