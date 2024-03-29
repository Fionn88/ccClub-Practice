"""
改考卷

描述
強強是一個認真的老師，每一次的考試，為了了解學生有哪些不懂的地方、以及評估題目的難度，他會將學生所有的作答都記錄在電腦上，並用程式改考卷，以自動計算出每個同學的成績，和每一題的正確率。
所有的考卷滿分為 100 分，題目有 x 題，每一題佔 100 / x 分。為了讓分數好看，100 必定整除 x。
題目皆為單選題，每題有 4 個選項。由於是選擇題，就算學生有不會寫的題目也必然會猜一個選項。
每一題的正確率奇進偶捨到小數點下 2 位。

輸入
輸入為 2+n 行
第 1 行為標準答案，每 5 題一個空格。
第 2 行為同學人數。
後面 n 行為同學的名字及作答，名字和作答之間以空格分隔、每 5 題一個空格。

輸出
輸出為 n+1 行
前 n 行為每個同學的名字及成績，名字和成績之間以空格分隔。
最後 1 行為每一題的正確率，每一題之間以空格分隔。

輸入範例 1
33333 22222
2
小明 13322 22222
小華 32311 22222

輸出範例 1
小明 70
小華 70
50.0% 50.0% 100.0% 0.0% 0.0% 100.0% 100.0% 100.0% 100.0% 100.0%

輸入範例 2
ABCB
3
泱泱 ABCB
小迪 CBAA
國國 ABCB

輸出範例 2
泱泱 100
小迪 25
國國 100
66.67% 100.0% 66.67% 66.67%

提示
奇進偶捨類似四捨五入但更精確，使用 round() 即可實作，更多說明請看這裡
"""

answerN = list(input().replace(" ", ""))
studentN = int(input())
length = len(answerN)
studentGradeD = {}
accuracy = {i: 0 for i in range(1, length+1)}

for _ in range(studentN):

    student = input().split()
    name = student[0]
    problem = list(''.join(student[1:]))
    correct,problemN = 0,0

    for correctAnswer, studentAnswer in zip(answerN,problem):
        problemN += 1
        if correctAnswer == studentAnswer:
            correct += 1
            accuracy[problemN] += 1

    studentGradeD[name] = int(100/length*correct)

for key, value in studentGradeD.items():
    print(key,value)
for index in range(1,length+1):
    percent = round(round(accuracy.get(index)/studentN,4)* 100,2)
    if index == length:
        print(f"{percent}%")
    else:
        print(f"{percent}%",end=' ')
