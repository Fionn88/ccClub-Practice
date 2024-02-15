"""
綜合2-3：計算機
描述

給定一個字串 s，代表希望計算的運算式。內容包含加減乘除四種運算符號（先乘除，後加減）以及數字，數字與運算符號之間皆用一個空格隔開。

請計算運算式 s 的結果，並將其印出，輸出值的型態請使用 float。


輸入
輸入為一行，包含一個字串s


輸出
輸出為一行，包含一個浮點數


輸入範例 1 
0.1 + 0.2 * 0.3 / 0.4

輸出範例 1
0.25

輸入範例 2 
-1.5 + 2.5 - 3 * 4

輸出範例 2
-11.0

來源
ccClub Judge
"""

# 列出優先順序，讓他們比大小，把乘除的式子先 append 到 ans
def compareSpot(spot):
    theTwo = ['*', '/']
    theOne = ['+', '-']
    if spot in theTwo:
        return 2
    if spot in theOne:
        return 1

s = input().split(" ")
spot = []
digit = []
ans = []
delete = []
for index,value in enumerate(s):
    try:
        s[index] = float(value)
        digit.append(float(value))
    except:
        s[index] = value
        spot.append(value)

    # 感覺會出錯的地方，如果是 0.1 + 0.2 * 0.3 - 0.5 / 0.6 => 會出錯
    if len(spot) >= 2:
        if compareSpot(spot[-1]) > compareSpot(spot[-2]):
            ans.append(digit.pop())
            ans.append(spot.pop())

# 嘗試把 * / 式子 delete 掉 再 append 算好的數字
ans.append(digit.pop())
for i in ans:
    if i in s:
        s.remove(i)

# 處理第二個式子

# ansDigit = 0
# for index,value in enumerate(ans):
#     if value == '*':
#         if ansDigit == 0:
#             ansDigit = ans[index - 1]
#         ansDigit *= ans[index + 1]
        
#     if value == '/':
#         if ansDigit == 0:
#             ansDigit = ans[index - 1]
#         ansDigit /= ans[index + 1]

print(delete)
# for i in delete:
#     del ans[i]
print(ans)

# theTwoPoly = 0
# if digit and spot:
#     index = 0
#     for hotspot in spot:
#         index += 1
#         if hotspot == '+':
#             if not theTwoPoly:
#                 theTwoPoly = digit[index - 1]
#             if len(digit) >= 2:
#                 theTwoPoly += digit[index]

# print(ansDigit,theTwoPoly)

# if ansDigit and theTwoPoly:
#     hotspot = spot.pop()
#     if hotspot == '+':
#         ansDigit += theTwoPoly
#     if hotspot == '-':
#         ansDigit -= theTwoPoly

# print(ansDigit)


# print(spot)
# print(digit)
# print(ans)0.2 * 0.3 / 0.4 - 0.1 

        
        
