"""
停車位順位

描述
社區停車位有限，因此若登記的住戶太多，將依照以下優先序分發車位：
住戶棟別：A棟 > B棟 > C棟
承上，若棟別相同，則依照居住年資：10年以上(含) > 5年以上(含)，未滿10年 > 未滿5年
承上，若再相同，則依照門牌號碼：奇數 > 偶數
承上，若以上條件皆相同，則依照登記順序，先登記的優先序較高
給定住戶資料，請依照車位分發順序輸出住戶名單。

輸入
輸入有 n+1 行，第一行為正整數 n，代表總共有多少住戶登記。
接下來 n 行為這 n 個住戶的資訊，包含住戶ID、居住棟別、居住年資、門牌號碼，彼此間用空格分開。

輸出
輸出有 n 行，請依照優先序分別輸出住戶ID，優先序高的在前，優先序低的在後。

輸入範例 1
3
abc B 9 74
bcd B 15 31
ghe A 2 40

輸出範例 1
ghe
bcd
abc

輸入範例 2
4
01ik8kxdco A 2 152
pmbkf3t671 C 8 94
m416t50y5z C 5 176
uavyf8gohd C 10 110

輸出範例 2
01ik8kxdco
uavyf8gohd
pmbkf3t671
m416t50y5z

來源
ccClub Judge
"""

def sorting(lst):
    return (
        ord(lst[1]),
        int(lst[2]) < 5,
        int(lst[2]) < 10,
        int(lst[2]) >= 5,
        int(lst[2]) >= 10,
        int(lst[3]) % 2 == 0,
        int(lst[3]) % 2 == 1,
    )

membersNum = int(input())
lst_of_members = [[n for n in input().split()] for _ in range(membersNum)]
ordered_list = sorted(lst_of_members, key=sorting)
res = [str(i[0]) for i in ordered_list]

for ans in res:
    print(ans)
