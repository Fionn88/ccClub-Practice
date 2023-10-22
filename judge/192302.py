"""
小明去爬山
描述

小明是一個肥宅，可是一直以來小明的女朋友都對此感到很不滿，某一天下定決心叫他去踏青。小明當然是答應了，但是對於踏青的路線，他也有一些條件必須被滿足才會讓他願意去走，請根據他的要求選一條最適合的踏青路線，並輸出該路線的編號。他的要求如下：

1. 因為小明體力很差，走不了多久就需要在涼亭休息，所以從出發到第一個涼亭、或是兩個涼亭之間的距離都不能超過 300 公尺，若超過小明就不會選這條路線
2. 因為小明喝太多水，一下子就需要去上廁所，所以從出發到第一個廁所、或是兩個廁所之間都不能超過 300 公尺，不然小明就不會選這條路線
3. 因為小明有高山症，所以走完整條路線以後，這條路線的總爬升高度越少越好，不然容易不舒服
給定 n 個路線，每個路線會有數量不等的據點，據點跟據點之間的距離固定為 100 公尺，每個據點的資訊包含：

1. 在這 100 公尺所上升的高度（若為正值則上升，若為負值則下降）
2. 該據點是否有涼亭
3. 該據點是否有廁所
請替他找出適合的路線，並輸出路線編號（第一條路線的編號為 0）；如果給定的路線都不滿足小明的要求，請輸出 'stay at home'


輸入
輸入包含 ‌1+n+Σmi ‌ 行。(Σ上n，下i=1)

第一行為路線的數量 n，接下來有 n 個區塊。

每個區塊包含 ‌m_i + 1‌ 行，此區塊內的第一行為據點的數量 ‌m_i‌，接下來的 ‌m_i‌ 行為據點的資訊。

據點的資訊包含三個值，一個整數代表上升的高度、兩個布林值代表該據點涼亭以及廁所的有無。


輸出
輸出包含一行，包含一個整數，代表他選中的踏青路線。若小明沒有中意的踏青路線，請輸出字串 'stay at home'。


輸入範例 1 
1
12
30,True,True
3,False,False
0,True,True
3,True,True
-5,False,True
1,False,False
10,True,True
0,False,False
5,False,False
-3,False,False
2,False,True
-1,False,False

輸出範例 1
stay at home

輸入範例 2 
2
11
0,False,False
30,True,True
3,False,False
-5,False,True
-5,True,False
1,True,True
10,True,False
2,False,True
-3,False,False
2,False,False
-1,False,False
7
30,True,True
-3,False,False
3,True,True
0,True,True
2,False,False
10,True,True
5,False,False

輸出範例 2
1

來源
ccClub Judge
"""

route_dict,ans = {},-1
block = input()
for i in range(0, int(block)):
    route = input()
    tol_height,gazebo_distance,wc_distance = 0,0,0
    accept_flag = True
    for j in range(0, int(route)):
        info = input().split(",")
        tol_height += int(info[0])

        if info[1] == 'True':
            gazebo_distance = 0
        else:
            gazebo_distance += 100

        if info[2] == 'True':
            wc_distance = 0
        else:
            wc_distance += 100

        if gazebo_distance >= 300 or wc_distance >= 300:
            accept_flag = False
    route_dict [i] = {'height': tol_height, 'flag': accept_flag}
min = float("inf")
for i in range(0, len(route_dict)):
    if route_dict[i]['flag'] and route_dict[i]['height'] < min:
        ans = i
if ans == -1:
    print("stay at home")
else:
    print(ans)
