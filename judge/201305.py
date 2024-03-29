"""
OO下載器

描述
OO下載器提供了許許多多的下載資源供大家選擇，每一個資源的名字和大小都會列在列表當中。
但用戶下載的時候只能依照下載器提供的組合來下載資源，要下載不能只下載單一個資源，要一次將同組合的資源下載下來才可以。
這時候用戶就要自己衡量網路傳輸速度來知道要下載這個組合要花多少時間了！

因此，我們會提供資源的列表，一共有 N 個，每個資源和其大小的格式如下：name1 size1 name2 size2...nameN sizeN
以及組合的數量共 M 個，每個組合都會用如右的格式呈現：group name1 name2...
最後是 K 個用戶選擇下載的組合，只會有一個，以及該用戶的網速，格式如右：group speed
請輸出這 K 個用戶要下載時所需的時間，時間的計算方式為組合的總大小 / 網速，格式為整數，請無條件捨去小數位。

輸入
第一行為總資源數 N。
第二行為下載資源r1 資源大小n1 r2 n2 .....rN nN 以空格分隔
第三行為總組合包數 M
第 4 ~ M+3 行為一群由空格分開的字串，每行第一個字串為組合包名，其後接著組合包內含的資源。
第 M+4 行為提出要求的使用者數 K
第 M+5 ~ M+K+4 行，每行為一項要求，包含要求的組合包和使用者的網速，以空格分開。

輸出
K 行，每行為預估使用者的下載時間。請無條件捨去至整數

輸入範例 1
4
西遊記 35 紅樓夢 50 哈利波特 21 暮光之城 43 
3
奇幻 西遊記 哈利波特
西洋 哈利波特 暮光之城
小說大全 紅樓夢 哈利波特 暮光之城 西遊記
2
小說大全 5
西洋 2

輸出範例 1
29
32

來源
ccClub Judge
"""

download,group = {},{}
answer = []
resourceCount = int(input())
resource = input().split()
for i in range(resourceCount):
    download[resource[i+i]] = resource[i+i+1]
groupCount = int(input())
for _ in range(groupCount):
    groupList = input().split()
    group[groupList[0]] = groupList[1:]
queryCount = int(input())
for _ in range(queryCount):
    query = input().split()
    nameList = group.get(query[0])
    speed = 0
    for name in nameList:
        speed += int(download.get(name))
    print(speed // int(query[1]))        
