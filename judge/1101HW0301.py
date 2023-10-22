"""
檢查學號
描述

小明舉辦講座收到了很多報名表，然而好多學生不好好填學號，請你幫他清一下資料吧！流程如下：

有些沒看清楚的傢伙把學號填成學校信箱了，因此若看到學號以 “@ntu.edu.tw” 結尾，請好心幫他刪掉 “@ntu.edu.tw”，但如果以"@NTU.EDU.TW"結尾，刪除該報名資料
學號開頭第一碼若是小寫英文字母，將第一碼轉成大寫英文字母，其他碼不改變大小寫。
由於防疫規定，講座只開放校內學生報名，因此學號開頭不是 “B”，“R”，“D”，“F” 的，刪除該報名資料
學號不是剛好 9 碼的，刪除該報名資料
檢查是否有重複的學號，若有則保留重複學號中第一筆報名資料

輸入
輸入有若干行。
第一行包含一個數字 n，代表收到的報名表數量。
接下來 n 行，每行代表一個學號。


輸出
輸出包含若干行，請依照輸入的順序，輸出清理後的學號資料，每行包含一個學號。


輸入範例 1 
5
B07303992
B07902348
B067033233
f99201111
b07303992

輸出範例 1
B07303992
B07902348
F99201111

輸入範例 2 
5
r09201543@ntu.edu.tw
r08323999
b10000000
B11000000
R99999999@ntu.edu.tv

輸出範例 2
R09201543
R08323999
B10000000
B11000000

提示
可以試試看利用函式讓清理的過程更清楚易讀！
"""

def validateEmail(student_id):
    if '@' in student_id:
        student_list = student_id.split('@')
        if student_list[1] == 'ntu.edu.tw':
            return (True,student_list[0])
        else:
            return [False]
    else:
        return (True,student_id)

def validateTitle(student_id):
    if student_id[0].islower():
        student_id = ' '.join(sub[:1].upper() + sub[1:] for sub in student_id.split(' '))
        return student_id
    else:
        return student_id

n = int(input())
res = []
for i in range(n):
    student_id = input()
    if student_id == "":
        continue
    ansList = validateEmail(student_id)

    if ansList[0]:
        student_id = ansList[1]
    else:
        continue

    student_id = validateTitle(student_id)
    if len(student_id) != 9:
        continue
    if student_id[0] == 'B' or student_id[0] == 'R' or student_id[0] == 'D' or student_id[0] == 'F':
        res.append(student_id)
    else:
        continue

if res:
    res = list(dict.fromkeys(res))
    for i in res:
        print(i)
else:
    print('')
