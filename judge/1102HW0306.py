"""
小明當班長

描述
台灣國中最近開學了，小明有幸被選中當班長。老師指派給他的第一個任務就是照男生女生的身高將升旗隊伍排出來
請問你能幫幫小明嗎？

輸入
輸入有兩行正整數
第一行為男生的身高（由矮到高），第二行為女生的身高（由矮到高）

輸出
輸出為一串列，將男女的身高由高到矮排好

輸入範例 1 
4 5 6
1 2 3

輸出範例 1
[6, 5, 4, 3, 2, 1]
"""

male = list(map(int,input().split()))
female = list(map(int,input().split()))

print(sorted(male + female, reverse=True))
