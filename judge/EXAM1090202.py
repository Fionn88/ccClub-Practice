"""
凱凱買家具
描述

上大學後的凱凱為了體驗外宿生活，在學校附近跟同學分租了一個房間，為了讓租屋處變得更有家的感覺，凱凱決定買些家具好好佈置自己的房間。

由於很滿意房東附的家具，凱凱只需要再多買個桌子、電腦椅以及書櫃共三個品項的家具，這樣房間就完美了。

於是他上了北歐知名家具連鎖店的網站逛了一下，因為預算有限，他希望可以寫一個程式把符合預算的家具組合列出來，方便他做決定。


輸入
輸入有七行。

第一行為一個正整數，代表買家具的預算上限。

第二行為數個字串，代表桌子所有品項的列表，以空格分開。

第三行為數個正整數，代表每個桌子對應的價錢，以空格分開。

第四行為數個字串，代表電腦椅所有品項的列表，以空格分開。

第五行為數個正整數，代表每個電腦椅對應的價錢，以空格分開。

第六行為數個字串，代表書櫃所有品項的列表，以空格分開。

第七行為數個正整數，代表每個書櫃對應的價錢，以空格分開。


輸出
輸出有數行，包含所有符合預算的購買組合，購買組合的順序依照各品項列表的順序。

每一行代表一種購買組合，包含桌子名稱、電腦椅名稱、書櫃名稱、以及總和的價錢，格式為「<桌子名稱>/<電腦椅名稱>/<書櫃名稱>:<總和的價錢>」。


輸入範例 1 
17000
MICKE書桌 MICKE書桌 HILVER書桌
4990 9990 4990
MARKUS辦公椅 FLINTAN辦公椅
5390 2490
FINNBY書櫃 MORLIDEN書櫃
5490 5990

輸出範例 1
MICKE書桌/MARKUS辦公椅/FINNBY書櫃:15870
MICKE書桌/MARKUS辦公椅/MORLIDEN書櫃:16370
MICKE書桌/FLINTAN辦公椅/FINNBY書櫃:12970
MICKE書桌/FLINTAN辦公椅/MORLIDEN書櫃:13470
HILVER書桌/MARKUS辦公椅/FINNBY書櫃:15870
HILVER書桌/MARKUS辦公椅/MORLIDEN書櫃:16370
HILVER書桌/FLINTAN辦公椅/FINNBY書櫃:12970
HILVER書桌/FLINTAN辦公椅/MORLIDEN書櫃:13470

輸入範例 2 
41000
HILVER書桌 HEMNES書桌 HILVER書桌
2990 4990 9990
LIDKULLEN椅凳
5390
MORLIDEN書櫃
5990

輸出範例 2
HILVER書桌/LIDKULLEN椅凳/MORLIDEN書櫃:14370
HEMNES書桌/LIDKULLEN椅凳/MORLIDEN書櫃:16370
HILVER書桌/LIDKULLEN椅凳/MORLIDEN書櫃:21370

輸入範例 3 
33000
HEMNES書桌 MICKE書桌
4990 9990
MARKUS辦公椅 TROLLBERGET椅凳 LIDKULLEN椅凳
2790 5390 2490
LOMMARP書櫃 HEMNES書櫃 HEMNES書櫃 FINNBY書櫃 BILLY玻璃門書櫃 FINNBY書櫃 GERSBY書櫃 MORLIDEN書櫃
3490 12980 12980 5990 990 799 5990 5990

輸出範例 3
HEMNES書桌/MARKUS辦公椅/LOMMARP書櫃:11270
HEMNES書桌/MARKUS辦公椅/HEMNES書櫃:20760
HEMNES書桌/MARKUS辦公椅/HEMNES書櫃:20760
HEMNES書桌/MARKUS辦公椅/FINNBY書櫃:13770
HEMNES書桌/MARKUS辦公椅/BILLY玻璃門書櫃:8770
HEMNES書桌/MARKUS辦公椅/FINNBY書櫃:8579
HEMNES書桌/MARKUS辦公椅/GERSBY書櫃:13770
HEMNES書桌/MARKUS辦公椅/MORLIDEN書櫃:13770
HEMNES書桌/TROLLBERGET椅凳/LOMMARP書櫃:13870
HEMNES書桌/TROLLBERGET椅凳/HEMNES書櫃:23360
HEMNES書桌/TROLLBERGET椅凳/HEMNES書櫃:23360
HEMNES書桌/TROLLBERGET椅凳/FINNBY書櫃:16370
HEMNES書桌/TROLLBERGET椅凳/BILLY玻璃門書櫃:11370
HEMNES書桌/TROLLBERGET椅凳/FINNBY書櫃:11179
HEMNES書桌/TROLLBERGET椅凳/GERSBY書櫃:16370
HEMNES書桌/TROLLBERGET椅凳/MORLIDEN書櫃:16370
HEMNES書桌/LIDKULLEN椅凳/LOMMARP書櫃:10970
HEMNES書桌/LIDKULLEN椅凳/HEMNES書櫃:20460
HEMNES書桌/LIDKULLEN椅凳/HEMNES書櫃:20460
HEMNES書桌/LIDKULLEN椅凳/FINNBY書櫃:13470
HEMNES書桌/LIDKULLEN椅凳/BILLY玻璃門書櫃:8470
HEMNES書桌/LIDKULLEN椅凳/FINNBY書櫃:8279
HEMNES書桌/LIDKULLEN椅凳/GERSBY書櫃:13470
HEMNES書桌/LIDKULLEN椅凳/MORLIDEN書櫃:13470
MICKE書桌/MARKUS辦公椅/LOMMARP書櫃:16270
MICKE書桌/MARKUS辦公椅/HEMNES書櫃:25760
MICKE書桌/MARKUS辦公椅/HEMNES書櫃:25760
MICKE書桌/MARKUS辦公椅/FINNBY書櫃:18770
MICKE書桌/MARKUS辦公椅/BILLY玻璃門書櫃:13770
MICKE書桌/MARKUS辦公椅/FINNBY書櫃:13579
MICKE書桌/MARKUS辦公椅/GERSBY書櫃:18770
MICKE書桌/MARKUS辦公椅/MORLIDEN書櫃:18770
MICKE書桌/TROLLBERGET椅凳/LOMMARP書櫃:18870
MICKE書桌/TROLLBERGET椅凳/HEMNES書櫃:28360
MICKE書桌/TROLLBERGET椅凳/HEMNES書櫃:28360
MICKE書桌/TROLLBERGET椅凳/FINNBY書櫃:21370
MICKE書桌/TROLLBERGET椅凳/BILLY玻璃門書櫃:16370
MICKE書桌/TROLLBERGET椅凳/FINNBY書櫃:16179
MICKE書桌/TROLLBERGET椅凳/GERSBY書櫃:21370
MICKE書桌/TROLLBERGET椅凳/MORLIDEN書櫃:21370
MICKE書桌/LIDKULLEN椅凳/LOMMARP書櫃:15970
MICKE書桌/LIDKULLEN椅凳/HEMNES書櫃:25460
MICKE書桌/LIDKULLEN椅凳/HEMNES書櫃:25460
MICKE書桌/LIDKULLEN椅凳/FINNBY書櫃:18470
MICKE書桌/LIDKULLEN椅凳/BILLY玻璃門書櫃:13470
MICKE書桌/LIDKULLEN椅凳/FINNBY書櫃:13279
MICKE書桌/LIDKULLEN椅凳/GERSBY書櫃:18470
MICKE書桌/LIDKULLEN椅凳/MORLIDEN書櫃:18470
"""
budget = int(input())
deskItem = input().split()
deskPrice = [int(i) for i in input().split()]
chairItem = input().split()
chairPrice = [int(j) for j in input().split()]
shelfItem = input().split()
shelfPrice = [int(k) for k in input().split()]

    
for k in range(len(deskItem)):
    for j in range(len(chairItem)):
        for i in range(len(shelfItem)):
            if int(deskPrice[k]+chairPrice[j]+shelfPrice[i]) <= budget:
                print(deskItem[k]+'/'+chairItem[j]+'/'+shelfItem[i]+':'+str(deskPrice[k]+chairPrice[j]+shelfPrice[i]))