"""
小明上菜啦 II

描述
受到疫情影響，小明餐廳的生意大受打擊。為了吸引新的客源，小明決定要開發新的餐點，但是粗心的小明現在卻有了新的問題，健忘的他常常在研發什麼新菜單的時候想到重複的料理名稱。小明決定請你幫忙想辦法檢查他的料理名稱是不是有重複，如果有重複的話要提醒他一下。
小明決定請你幫忙想辦法檢查他的料理名稱是不是有重複，如果有重複的話要提醒他一下。輸入只有一個部分，皆為新想出的料理名稱。若在建立菜單的過程中有重複出現過的料理名稱（大小寫視為同一道）或是新料理名稱重新排列後可以在菜單上被找到，請提醒一下小明。

輸入
若干行
每行為新料理的名稱

輸出
若干行
若是有料理名稱重複出現請輸出「<新料理名稱> already exists」，若是料理名稱重新排列之後是重複出現的請輸出「<新料理名稱> is <舊料理名稱>,  <舊料理名稱> already exists」，若沒出現過請輸出「Create <新料理名稱>」

輸入範例 1 
紙包雞
雞包紙
紙包雞包紙
紙包雞包紙包雞
紙包雞

輸出範例 1
Create 紙包雞
雞包紙 is 紙包雞, 紙包雞 already exists
Create 紙包雞包紙
Create 紙包雞包紙包雞
紙包雞 already exists

輸入範例 2 
abc ab
aabb c
aab,bc
aa,bbc
AA,BBC
aa bb c

輸出範例 2
Create abc ab
aabb c is abc ab, abc ab already exists
Create aab,bc
aa,bbc is aab,bc, aab,bc already exists
AA,BBC is aab,bc, aab,bc already exists
Create aa bb c

輸入範例 3 
abc
Abc
ABC

輸出範例 3
Create abc
Abc is abc, abc already exists
ABC is abc, abc already exists

提示
料理名稱是否重複的判斷可以用字典，在使用字典的時候判斷 key 是否重複比較省時的做法是 if key in dict
料理名稱是否重複可以藉由排序的方式來判斷
"""