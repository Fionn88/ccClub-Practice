"""
加簽大地 II
描述

每個學期的開學前兩週，都是大家忙於加簽不同課的時間，而有一堂CS系所開設的機器學習課程加簽規則如下：

1.優先順序為：台大資訊學群 (aXX902XXX) > 台大電機學群 (aXX901XXX) > 台大其他系所 (aXXXXXXXX)

2.在同一個優先順位內，大四的學生優先於其他年級的學生，在這裡我們規定為學號開頭為"a04"的學生（a04303XXX 優先於 a05303XXX 以及 a03303XXX）

3.除此之外，接續規則2的優先順序，如果在同個優先順位之內，該同學的學號末三碼是3, 5, 7其中一個數字的倍數，將優先於其他同學進行加簽 (a05502018 優先於 a05705019)

給定數量不等的學號，請依據加簽的先後順序將其輸出（若順位相同，請依照原先輸入的順序輸出）


輸入
輸入為一行，包含n個字串，內容為學號


輸出
輸出一共有n行，各包含一個字串，內容為學號


輸入範例 1 
a06901126 a05203071 a99204111 

輸出範例 1
a06901126
a99204111
a05203071

輸入範例 2 
a06106081 a99203134 a99703031 a98702033 a02203081 

輸出範例 2
a06106081
a98702033
a02203081
a99203134
a99703031

來源
ccClub Judge
"""

# ==================== Wrong Answer ====================
s = input().split()

def domain(department):
  department = department[3:6]
  if department == '902':
    return 200
  elif department == '901':
    return 100
  else:
    return 0

def level(grad):
  grad = int(grad[1:3])
  if grad == 4:
    return 10
  else:
    return 0

def factor(code):
  code = int(code[6:])
  if code%3==0 or code%5==0 or code%7==0:
    return 1
  else:
    return 0


sorted_priority = sorted(s,key=domain,reverse=True)
sorted_priority = sorted(sorted_priority,key=level,reverse=True)
sorted_priority = sorted(sorted_priority,key=factor,reverse=True)
print('\n'.join(sorted_priority))