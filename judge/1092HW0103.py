"""
小仔算成績

描述
小仔這學期修「程式設計與資料擷取」這門通識課，請依照他的成績幫他算算看最後拿的等第成績吧。
這門課程的評分包括作業、考試和期末專案。作業佔總成績 50%，有 6 次作業（取最高分 5 次作業平均)，若有某次作業成績標示為 -1，表示小仔被助教抓到該次作業為抄襲(小仔抄襲至多 1 次)，則該次作業以 0 分計算，且最後學期成績扣兩個等第分數(A- -> B、C -> F)，作業平均過後超過 100 分，以 100 分計；
有 2 次期中考試，較高分的考試成績佔總成績 15%，較低分的考試成績佔總成績 10%，兩次考試超過 100 分，皆以 100 分計；其期末專案成績佔總成績 25%。在算出學期成績後，依下表計算出該分數的等第制成績。

====
請至 judge 查看圖片
====

輸入
共 3 行，
第 1 行，包含 6 整數，分別為 6 次作業成績，中間以空白隔開。
第 2 行，包含 2 整數，分別為 2 次期中考成績，中間以空白隔開。
第 3 行，包含 1 整數，為期末專案成績。

輸出
共 1 行，輸出 1 整數和 1 字串，分別為學期百分制成績(四捨五入至整數)和等第成績，中間以空白隔開


輸入範例 1 
100 100 93 90 80 -1
110 60
85

輸出範例 1
89 B+

輸入範例 2 
50 80 67 49 100 100 
85 80
90

輸出範例 2
83 A-
"""

hwN = sorted([int(n) for n in input().split()])
middleTest = sorted([int(n) for n in input().split()])
finalTest = int(input())

def countHW(grade):
    if grade[1] == -1:
        isDownGrade = True
        return 0,isDownGrade
    else:
        if grade[0] == -1:
            isDownGrade = True
            answer = sum(grade[1:])/5
            if answer > 100:
                return 100 * 0.5
            else:
                return answer * 0.5,isDownGrade
        else:
            isDownGrade = False
            answer = sum(grade[1:])/5
            if answer > 100:
                return 100 * 0.5,isDownGrade
            else:
                return answer * 0.5,isDownGrade
        
def countMiddle(grade):
    upGrade,lowGrade = 0,0
    if grade[0] > 100:
        lowGrade = 100 * 0.1
    else:
        lowGrade = grade[0] * 0.1
    
    if grade[1] > 100:
        upGrade = 100 * 0.15
    else:
        upGrade = grade[1] * 0.15

    return lowGrade + upGrade

def countFinal(grade):
    return grade * 0.25

countHwGrade, isDownGrade = countHW(hwN)
final_score = round(countHwGrade + countMiddle(middleTest) + countFinal(finalTest))
if 90 <= final_score <= 100:
    ranking = 'A+'
    if isDownGrade:
        ranking = 'A-'
elif 85 <= final_score <= 89: 
    ranking = 'A'
    if isDownGrade:
        ranking = 'B+'
elif 80 <= final_score <= 84:
    ranking = 'A-'
    if isDownGrade:
        ranking = 'B'
elif 77 <= final_score <= 79:
    ranking = 'B+'
    if isDownGrade:
        ranking = 'B-'
elif 73 <= final_score <= 76:
    ranking = 'B'
    if isDownGrade:
        ranking = 'C+'
elif 70 <= final_score <= 72:
    ranking = 'B-'
    if isDownGrade:
        ranking = 'C'
elif 67 <= final_score <= 69:
    ranking = 'C+'
    if isDownGrade:
        ranking = 'C-'
elif 63 <= final_score <= 66:
    ranking = 'C'
    if isDownGrade:
        ranking = 'F'
elif 60 <= final_score <= 62:
    ranking = 'C-'
    if isDownGrade:
        ranking = 'X'
elif 0 < final_score <= 59:
    ranking = 'F'
    if isDownGrade:
        ranking = 'X'
elif final_score == 0:
    ranking = 'X'

print(final_score,ranking)
