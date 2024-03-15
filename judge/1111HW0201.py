"""
阿偉辦卡拉OK大賽

描述
阿偉升上大二，擔任友會卡拉OK大賽的總召，請幫他製作一個卡拉OK大賽的參賽者名單，記錄參賽者的報名資訊，包含姓名、性別、年齡、科系、分組等，讓他能快速找到各種需要的資料

輸入
輸入有數行
首先會輸入每個參賽者的基本資料，包含 Name, Gender, Age, Dep, Group 五種，Name 一定為第一個資料，但後續的次序可能會不同，例如：
Name:Alice,Gender:F,Age:18,Dep:FIN,Group:8
Name:Alice,Age:18,Dep:FIN,Group:8,Gender:F
Name:Alice,Dep:FIN,Gender:F,Group:8,Age:18
均為可能出現的輸入
參賽者資料輸入完畢後有一行"competitorEND"
接著為不定行輸入，為阿偉想要查找的資料，共有 5 種可能
如果輸入為人名，例如Alice，則輸出該位參賽者的基本資料，型態為 list，輸出時依照「Gender,Age,Group,Dep」的順序排序，其中 Age 和 Group 的資料型態為 int，且科系及性別均為大寫字母，如果參賽者不在名單中，則輸出None
如果輸入為年齡，例如Age 20，則輸出該年齡的所有參賽者，按照姓名字母順序排序，如果沒有該年齡的參賽者，則輸出None
如果輸入為組別，例如Group 2，則輸出該組別的所有參賽者，按照姓名字母順序排序，如果沒有該組別的參賽者，則輸出None
如果輸入為科系，例如Dep fin，則輸出該科系的所有參賽者，按照姓名字母順序排序，如果沒有該科系的參賽者，則輸出None
如果輸入為性別，例如Gender F，則輸出該性別的所有參賽者，按照姓名字母順序排序，如果沒有該性別的參賽者，則輸出None
查找資料時，如果指令不全，則輸出 None
此題保證參賽者的名稱不會重複，且參賽者至少有一人
輸入時，科系及性別不論大小寫均視為相同，舉例：科系 Fin=FIN=fin，性別 F=f

輸出
輸出為若干行，依照上述的規定輸出
詳細的輸出格式可參考 sample output

輸入範例 1
Name:Alice,Gender:F,Age:18,Dep:FIN,Group:8
competitorEND
Alice

輸出範例 1
[('Gender', 'F'), ('Age', 18), ('Group', 8), ('Dep', 'FIN')]

輸入範例 2
Name:Alice,Gender:F,Age:18,Dep:FIN,Group:8
Name:Ben,Age:22,Group:1,Gender:M,Dep:fin
Name:Cindy,Group:1,Dep:EE,Age:20,Gender:f
competitorEND
Dep fin
Gender m
Ben
Group 4
Age 22

輸出範例 2
['Alice', 'Ben']
['Ben']
[('Gender', 'M'), ('Age', 22), ('Group', 1), ('Dep', 'FIN')]
None
['Ben']
"""

from collections import defaultdict

def custom_sort(item):
    order = {'Gender': 1, 'Age': 2, 'Group': 3, 'Dep': 4}
    return order.get(item[0], 0)

dict_of_information = defaultdict(list)
while True:
    input_of_string = input()
    if input_of_string == "competitorEND":
        break
    information = input_of_string.split(",")

    name = ""
    for index,element in enumerate(information):
        element_of_string = element.split(":")
        if index == 0:
            name = element_of_string[1]
        else:
            if element_of_string[0] == "Group" or element_of_string[0] == "Age":
                dict_of_information[element_of_string[0]+element_of_string[1]].append(name)
                dict_of_information[name].append((element_of_string[0],int(element_of_string[1])))
            else:
                dict_of_information[element_of_string[0]+element_of_string[1].lower()].append(name)
                dict_of_information[name].append((element_of_string[0],element_of_string[1].upper()))
    dict_of_information[name] = sorted(dict_of_information[name], key=custom_sort)

ans = []
while True:
    try:
        question = input().split()
        if len(question) > 1:
            if question[0] == "Group" or question[0] == "Age":
                ans.append(dict_of_information.get(question[0]+question[1]))
            else:
                ans.append(dict_of_information.get(question[0]+question[1].lower()))
        else:
            ans.append(dict_of_information.get(question[0]))

    except:
        break

def is_list_of_tuples(variable):
    return isinstance(variable, list) and all(isinstance(item, tuple) for item in variable)

for elementAns in ans:
    if is_list_of_tuples(elementAns):
        print(elementAns)
    elif type(elementAns) is list:
        print(sorted(elementAns))
    else:
        print(elementAns)