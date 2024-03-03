"""
開學加簽

描述
每個學期的開學前兩週，都是大家忙於加簽不同課的時間，而有一堂「程式設計」通識課採積分高者優先加簽，積分規則如下：
台大電資學院學生禁修(bXX9XXXXX)，積分永遠為 0
大四學生(學號開頭 b06 的學生)積分加 3，大三學生(學號開頭 b07 的學生)積分加 1
若尾號後三碼為 3, 5, 7 的倍數，加積分 2 ，2 的倍數加 1
後五碼非零數字相乘，取該數的位數，加入積分，十位數加 1、百位數加 2，以此類推
題目給定 3 個學號，請輸出積分最高者和此人積分，若最高分不止 1 人，輸出學號位置在前者。

輸入
共一行，包含 3 個字串，分別為 3 個學生的學號，中間以空格隔開。

輸出
共一行，請輸出積分最高者和此人積分，中間以半形逗號隔開。

輸入範例 1
b09303542 b10203797 b07507909

輸出範例 1
5,b07507909

輸入範例 2
b06999999 b08402906 b11478532

輸出範例 2
6,b11478532
"""

students = input().split()
points = []
for student in students:
    if student[0] == "b" and student[3] == "9":
        points.append("0")
        continue
    point = 0
    if student[:3] == "b06":
        point += 3
    elif student[:3] == "b07":
        point += 1
    
    if int(student[-3:]) % 3 == 0 or int(student[-3:]) % 5 == 0 or int(student[-3:]) % 7 == 0:
        point += 2
    
    if int(student[-3:]) % 2 == 0:
        point += 1

    s = student[-5:].replace("0", "")
    product = 1
    for j in s:
        product *= int(j) 
    point += (len(str(product)) - 1)
    points.append(str(point))

res = sorted(list(zip(points, students)), key=lambda x: int(x[0]), reverse=True)
print(",".join(res[0]))
