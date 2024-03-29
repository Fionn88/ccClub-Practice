"""
凱凱發授權碼

描述
每學期開學都是凱凱最頭痛的時候，要從想要加簽的同學篩出符合條件的同學，並把授權碼發給他們。
所幸經過助教的建議，凱凱決定讓同學們填寫表單，只要符合條件就發授權碼，直到額滿為止。
請你寫個程式來幫助凱凱處理加簽表單的資料，加簽的條件如下所述：
1. 資工系的同學不給加簽。
2. 電機系的同學僅給大一的同學加簽。
3. 資管系的同學僅給大一、大二的同學加簽。
4. 其餘同學有填表單皆符合資格。

輸入
輸入有 n+2 行。
第一行為正整數 n，代表有 n 個同學填寫加簽表單。
第二行為正整數 m ，代表共有 m 張授權碼需要發放。
第 3 至 n+2 行共 n 行，每一行皆包含兩個字串，字串之間用空格分開，分別代表學號及系所。

輸出
輸出至多有 m 行（若符合加簽名單的人數小於 m，則全數輸出）。
每一行包含一個字串，代表符合加簽資格的學號（所有英文字母請以小寫輸出）。

輸入範例 1
11
9
b10901036 電機系
b07202015 物理系
b10409090 職治系
b07705027 資管系
B09409098 職治系
b08607045 農經系
b09607018 農經系
b06202073 物理系
B09703091 財金系
b09607099 農經系
b09902031 資工系

輸出範例 1
b10901036
b07202015
b10409090
b09409098
b08607045
b09607018
b06202073
b09703091
b09607099

輸入範例 2
8
6
b08607043 農經系
b09613068 植微系
b09101071 中文系
B10902095 資工系
b10705065 資管系
B07613051 植微系
B08303015 經濟系
B07901047 電機系

輸出範例 2
b08607043
b09613068
b09101071
b10705065
b07613051
b08303015

輸入範例 3
31
27
b07902040 資工系
b08705034 資管系
b06101060 中文系
B08705016 資管系
b10901036 電機系
B09902088 資工系
b06101028 中文系
b08902065 資工系
B08202097 物理系
B07901078 電機系
B08901056 電機系
b06303056 經濟系
B08101063 中文系
B10303093 經濟系
b08202077 物理系
b07607090 農經系
b09409075 職治系
B09409058 職治系
b06303095 經濟系
B08705046 資管系
b06703095 財金系
b10303039 經濟系
b06902017 資工系
B09703020 財金系
b06303056 經濟系
b09303035 經濟系
b09902057 資工系
b09902017 資工系
b06613057 植微系
b09705015 資管系
b07902088 資工系

輸出範例 3
b06101060
b10901036
b06101028
b08202097
b06303056
b08101063
b10303093
b08202077
b07607090
b09409075
b09409058
b06303095
b06703095
b10303039
b09703020
b06303056
b09303035
b06613057
b09705015

提示
10 是 1 年級、09 是 2 年級、08 是 3 年級，以此類推
"""

ans = []
number_of_all = int(input())
number_of_ans = int(input())
for _ in range(number_of_all):
    if len(ans) == number_of_ans:
        break
    input_of_student = input().split()
    if input_of_student[1] == "資工系":
        continue
    elif input_of_student[1] == "電機系":
        if input_of_student[0][1:3] == "10":

            ans.append(input_of_student[0].lower())

    elif input_of_student[1] == "資管系":
        if input_of_student[0][1:3] == "10" or input_of_student[0][1:3] == "09":
            ans.append(input_of_student[0].lower())

    else:
        ans.append(input_of_student[0].lower())

for student in ans:
    print(student)
