"""
加簽大地
描述

每個學期的開學前兩週，都是大家忙於加簽不同課的時間，而有一堂CS系所開設的機器學習課程加簽規則如下：

1.優先順序為：台大資訊學群 (aXX902XXX) > 台大電機學群 (aXX901XXX) > 台大其他系所 (aXXXXXXXX)

2.在同一個優先順位內，大四的學生優先於其他年級的學生，在這裡我們規定為學號開頭為"a04"的學生（a04303XXX 優先於 a05303XXX）

3.除此之外，接續規則2的優先順序，如果在同個優先順位之內，該同學的學號末三碼是3, 5, 7其中一個數字的倍數，將優先於其他同學進行加簽 (a05502018 優先於 a05705019)

給定兩位同學的學號，請輸出加簽優先順位高的學號，若相同則輸出”tie”：


輸入
輸入為兩行，各包含一個字串ID1以及ID2


輸出
輸出為一行，包含一個字串


輸入範例 1 
a04902003
a04902014

輸出範例 1
tie

輸入範例 2 
a05303009
a05203017

輸出範例 2
a05303009

來源
ccClub Judge
"""



def domain(department):
  if department == '902':
    return 200
  elif department == '901':
    return 100
  else:
    return 0

def level(grad):
  if grad == 4:
    return 10
  else:
    return 0

def factor(code):
  if code%3==0 or code%5==0 or code%7==0:
    return 1
  else:
    return 0

s1 = input()
s2 = input()
domain_s1 = s1[3:6]
domain_s2 = s2[3:6]
grad_s1 = int(s1[1:3])
grad_s2 = int(s2[1:3])
code_s1 = int(s1[6:])
code_s2 = int(s2[6:])
score_s1 = 0
score_s2 = 0

score_s1 = domain(domain_s1) + level(grad_s1) + factor(code_s1)
score_s2 = domain(domain_s2) + level(grad_s2) + factor(code_s2)
if score_s1 == score_s2:
  print('tie')
elif score_s1 > score_s2:
  print(s1)
else:
  print(s2)