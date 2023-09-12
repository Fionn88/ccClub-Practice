"""
小明審報名表
描述

因為ccclub讀書分成A,B兩班，小明想把報名表分成兩個班來審，
Ａ班為社科班，Ｂ班則是收其他系所跟校外的朋友。
請根據報名表學院（或校外）的資訊判斷學員的班級，學員的資訊可能為social science,NTU,external,undefined。
如果學員沒有填入資訊(undefine)，就先跳過這張報名表，輸出skip；如果學員的資訊為social science，就將他們分到 A 班；在這兩者之外的話，請將這些學員分到B班。


輸入
輸入為一行，包含一個字串


輸出
輸出為一行，包含一個字串


輸入範例 1 
social science

輸出範例 1
A

輸入範例 2 
NTU

輸出範例 2
B

來源
ccClub Judge
"""
s = input()
if s == 'social science':
    print('A')
elif s == 'undefined':
    print('skip')
else:
    print('B')