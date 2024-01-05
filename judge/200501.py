"""
小明的單字卡

描述
因為想考好 GRE，小明想寫一個互動式單字卡程式來幫助記憶。以下是該程式該有的指令
I 指令:插入新的單字
C 指令:用中文查詢英文意思
E 指令:用英文查詢中文意思
Q 指令:結束程式你能幫他完成嗎？
note:
此題中假設所有中英單字對照都是一對一的，也就是說不會有兩個英文單字有同個中文意思，
同時也不會有兩個中文詞彙對照到同個英文單字。

輸入包含各種指令的組合
I 指令的格式為:I [中文] [英文]
C 指令的格式為:C [中文]
E 指令的格式為:E [英文]
Q 指令的格式為:Q

當輸入 I 指令時，若該單字不存在，則在單字卡加入該單字，並輸出[succeed]；
若該單字己經存在則輸出[fail]

輸入 C 指令時如果該單字存在，輸出其英文翻譯
輸入 E 指令時如果該單字存在，輸出其中文翻譯
若查不到單字，則輸出[fail]

輸入 Q 指令後結束程式

輸入
輸入有數行，格式如題幹，最後一行為一個字串 Q。

輸出
輸出有數行，各包含一個字串，為對應的翻譯或是[fail]。

輸入範例 1 
I 電腦 computer
C 電腦
E computer
C 大腦
E brain
I 電腦 computer
Q

輸出範例 1
[succeed]
computer
電腦
[fail]
[fail]
[fail]

來源
ccClub Judge
"""

C = {}
E = {}
while True:
    n = input()
    if n == 'Q':
        break
    n = n.split()
    if n[0] == 'I':
        if C.get(n[1]):
            print("[fail]")
        else:
            C[n[1]] = n[2]
            E[n[2]] = n[1]
            print("[succeed]")
    elif n[0] == 'C' :
        if C.get(n[1]):
            print(C.get(n[1]))
        else:
            print("[fail]")
    elif n[0] == 'E':
        if E.get(n[1]):
            print(E.get(n[1]))
        else:
            print("[fail]")
