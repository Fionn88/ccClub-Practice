"""
阿偉辦卡拉OK大賽 II

描述
接續上題，阿偉需要一個計算分數的程式，
本次比賽邀請到 4 位評審，給出各種計分方式，請幫他計算所有參賽者的最終成績，並告訴他最佳女歌手，最佳男歌手以及最佳團體獎的得主分別是誰

輸入
第 1 行爲所有參賽者的資訊，資料型態為 json，格式為
{name1:{info1,info2, ...}, name2:{info1, info2, ...}, ...}
第 2 - 5 行為評審的資訊，包含評審編號、科系、年齡等
如果評分對象與評審同一個科系，則會比其他人多加 2 分
如果評分對象與評審相同年齡，則會比其他人多加 1 分
如果評分對象與評審同科系且同年齡，則該對象該次加分分數 1.5 倍，或是加 3 分，取其中分數較高的執行
第 6 行開始為評審的評分，格式為評審編號 加分對象:分數，共有 2 種可能
如果為G*:數字，例如G8:7代表第 8 組的所有成員加 7 分
如果為人名:數字，例如Alice:3代表 Alice 加 3 分
如果評審編號不在規定的評審中，或是評審加分的組不存在，則跳過本次加分
如果加分對象格式非以上兩種，則輸出ValueError 出現錯誤的資料，例如ValueError SSE:2

輸出
輸出共幾項，分別為
input 中遇到錯誤情形可能需要輸出的ValueError 出現錯誤的資料
最佳女歌手：總分最高且性別為 F 的參賽者，輸出格式為一行姓名，如果有多位同分，則依照姓名順序輸出，中間用'-'分隔如果沒有最佳女歌手，或是最高分為 0，則輸出None
最佳男歌手：總分最高且性別為 M 的參賽者，輸出格式為一行姓名，如果有多位同分，則依照姓名順序輸出，中間用'-'分隔如果沒有最佳男歌手，或是最高分為 0，則輸出None
最佳團體獎：Group 中所有成員分數加總後最高的 Group，如果有多個 Group 同分，則依照 Group 的編號順序輸出，每個 Group 一行，輸出每個 Group 後，接續寫上該Group 中所有成員的姓名，姓名依照字典序輸出，如果沒有最佳團體獎，則輸出None
範例：Group 5: Cindy
Group 8: Alice-Ben

輸入範例 1
{"Alice": {"Gender": "F", "Age": 18, "Dep": "FIN", "Group": 8}, "Ben": {"Age": 22, "Group": 1, "Gender": "M", "Dep": "FIN"}, "Cindy": {"Group": 1, "Dep": "EE", "Age": 20, "Gender": "F"}, "David": {"Gender": "M", "Age": 18, "Dep": "MATH", "Group": 5}}
1 fin 30
2 CSIE 22
3 Math 18
4 PT 25
1 G1:2
3 David:4

輸出範例 1
Cindy
David
Group 5: David

輸入範例 2
{"Alice": {"Gender": "F", "Age": 18, "Dep": "FIN", "Group": 8}, "Ben": {"Gender": "M", "Age": 18, "Dep": "FIN", "Group": 8}, "Cindy": {"Gender": "F", "Age": 18, "Dep": "FIN", "Group": 8}, "David": {"Gender": "M", "Age": 18, "Dep": "FIN", "Group": 8}, "Ella": {"Gender": "F", "Age": 18, "Dep": "MATH", "Group": 5}, "Fiona": {"Gender": "F", "Age": 20, "Dep": "BA", "Group": 5}, "Gina": {"Gender": "F", "Age": 19, "Dep": "EE", "Group": 5}, "Henry": {"Gender": "M", "Age": 21, "Dep": "EE", "Group": 4}}
1 fin 18
2 fin 20
3 math 18
4 CSIE 22
1 G8:5
2 Fiona:3
3 G5:3
4 Sherry:110
5 Alice:20
3 G2:7
2 G4:32

輸出範例 2
ValueError Sherry:110
Alice-Cindy
Henry
Group 4: Henry
Group 8: Alice-Ben-Cindy-David

輸入範例 3
{"Alice": {"Gender": "F", "Age": 18, "Dep": "FIN", "Group": 8}}
1 fin 30
2 CSIE 22
3 Math 18
4 PT 25
1 G1:2
3 Ben:4

輸出範例 3
ValueError Ben:4
None
None
None

提示
舉例：見 sample input 1 中，
第一個加分方式為1 G1:2，代表加分的為 1 號評審，對於 G1 中所有人加 2 分，
又因為 Ben 的科系是 fin，和 1 號評審一樣，所以會額外得到 2 分，因此第一次加分的分數是：Ben +4, Cindy +2
第二個加分方式為3 David:4代表加分的為 3 號評審，對於 David 加 4 分，
又因為 David 的科系和年齡都和 3 號評審相同，所以取 1.5 倍分數：4*1.5=6，以及加三分：4+3=7，兩個分數中較高者作為本次加分，因此執行後 David 的分數會增加 7
"""

import json
from collections import defaultdict

def selectFemale(point, participate_information):
    if not point:
        return None
    
    maxPoint = 0
    people = []
    for key,value in point.items():
        if participate_information.get(key).get("Gender") == "F":
            if maxPoint < value:
                maxPoint = value

    if maxPoint == 0:
        return None
    for key,value in point.items():
        if value != maxPoint:
            continue
        elif participate_information.get(key).get("Gender") == "F":
            people.append(key)
    
    if people:
        people = sorted(people)
        return '-'.join(people)
    else:
        return None
    
def selectMale(point, participate_information):
    if not point:
        return None

    maxPoint = 0
    people = []
    for key,value in point.items():
        if participate_information.get(key).get("Gender") == "M":
            if maxPoint < value:
                maxPoint = value
    if maxPoint == 0:
        return None
    for key,value in point.items():
        if value != maxPoint:
            continue
        elif participate_information.get(key).get("Gender") == "M":
            people.append(key)
            
    if people:
        people = sorted(people)
        return '-'.join(people)
    else:
        return None
    
def selectGroup(point, participate_information):
    if not point:
        return None
    
    group = defaultdict(int)
    for key,value in point.items():
        group[participate_information.get(key).get("Group")] += value
    
    maxPoint = max(group.values())
    maxGroup = {}
    
    for key,value in group.items():
        if maxPoint == value:
            maxGroup[key] = []

    if not maxGroup:
        return None
        
    for key,value in participate_information.items():
        if value.get("Group") in maxGroup:
            maxGroup[value.get("Group")].append(key)

    ans = []
    for id in sorted(maxGroup):
        maxGroup[id] = sorted(maxGroup[id])
        ans.append(f'Group {id}: {"-".join(maxGroup[id])}')
    
    return ans

participate_information = json.loads(input())
reviewer_information = {}
for _ in range(4):
    reviewer = input().split()
    reviewer_information[int(reviewer[0])] = (reviewer[1], int(reviewer[2]))

point = defaultdict(int)
error = []

while True:
    try:
        review, target = input().split()
        # 判斷評分者是否合法
        if int(review) not in list(reviewer_information):
            continue
        target = target.split(":")
        # 判斷被評分者是否合法
        if len(target[0]) != 2 and participate_information.get(target[0]) == None:
            error.append(f'ValueError {":".join(target)}')
            continue

        # 判斷是否為 群組
        if 'G' in target[0] and len(target[0]) == 2:
            # 尋找參賽者
            for key,value in participate_information.items():
                # 是否有符合的群組
                if value.get("Group") == int(target[0][1]):

                    # 如有符合比對是否有跟評審者相同科系或是相同年齡
                    if value.get("Dep") == reviewer_information.get(int(review))[0].upper() and value.get("Age") == reviewer_information.get(int(review))[1]:
                        point[key] = max(int(target[1]) * 1.5, int(target[1]) + 3)
                        continue
                    
                    point[key] += int(target[1])
                    if value.get("Dep") == reviewer_information.get(int(review))[0].upper():
                        point[key] += 2
                    elif value.get("Age") == reviewer_information.get(int(review))[1]:
                        point[key] += 1


        else:

            if participate_information.get(target[0]).get("Dep") == reviewer_information.get(int(review))[0].upper() and participate_information.get(target[0]).get("Age") == reviewer_information.get(int(review))[1]:
                point[target[0]] += max(int(target[1]) * 1.5, int(target[1]) + 3)
                continue

            point[target[0]] += int(target[1])
            if participate_information.get(target[0]).get("Dep") == reviewer_information.get(int(review))[0].upper():
                point[target[0]] += 2
            elif participate_information.get(target[0]).get("Age") == reviewer_information.get(int(review))[1]:
                point[target[0]] += 1

    
    except:
        break

if error:
    for errorElement in error:
        print(errorElement)

print(selectFemale(point,participate_information))
print(selectMale(point,participate_information))
listMaxGroup = selectGroup(point, participate_information)
if listMaxGroup:
    for group in listMaxGroup:
        print(group)
else:
    print(listMaxGroup)
