"""
打字機
描述

一個打字機除了可以輸入數字和英文字母之外，還有額外三種指令：

指令+：將剛剛輸出的最後一個字元（數字或英文字母）再次輸出，若沒有已經輸出的字元，則指令無效。
例如，當指令為「C+」，遇到第一個指令 C 時輸出「C」，遇到第二個指令 +，輸出剛剛輸出的最後一個字元（也就是C），最終打字機輸出結果為「CC」。
指令-：將剛剛輸出的最後一個字元刪除，若沒有已經輸出的字元，則指令無效。
例如，當指令為「abc-」，遇到第一個指令 a 時輸出「a」，遇到第二個指令 b 時輸出「b」，遇到第三個指令 c 時輸出「c」，遇到第四個指令 - 時，刪除剛剛輸出的最後一個字元（也就是 c），最終打字機輸出結果為「ab」。
指令*：複製已經輸出的所有字元，若沒有已經輸出的字元，則指令無效。
例如，當指令為「abc*」，遇到第一個指令 a 時輸出「a」，遇到第二個指令 b 時輸出「b」，遇到第三個指令 c 時輸出「c」，遇到第四個指令 * 時，輸出已經輸出的所有字元（也就是abc），最終打字機輸出結果為「abcabc」。

輸入
輸入為一行，包含一個字串。


輸出
輸出為一行，包含一個字串，即螢幕上顯示的結果。


輸入範例 1
C++

輸出範例 1
CCC

輸入範例 2 
+C+

輸出範例 2
CC

輸入範例 3 
C+-

輸出範例 3
C

來源
ccClub Judge
"""
s = input()
ans = []
for index,value in enumerate(s):
    if (value == '+' or value == '-' or value == '*') and index == 0:
        pass
    elif value == '+' and index > 0:
        try:
            ans.append(ans[-1])
        except:
            pass
        
    elif value == '-' and index > 0:
        try:
            del ans[-1]
        except:
            pass
        
    elif value == '*' and index > 0:
        for i in ans[:]:
            ans.append(i)
    else:
        ans.append(value)
print(''.join(ans))