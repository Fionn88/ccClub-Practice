"""
小明來造句

描述
小明在寫英文造句作業，但是他覺得自己造很累，於是他想到一個好方法：
只要找到幾個主詞(S)、動詞(V)、受詞(O)，然後選一個組合起來就可以輕鬆完成作業了！
依照順序，先選好主詞，再選擇動詞，最後選擇受詞，選擇的順序依照輸入的順序，同一個主詞動詞組合，在配對完所有的受詞以後，才會換下一個動詞，進行下一輪配對；同樣的，在同一個主詞對應完所有動詞受詞組合以後，才會換下一個主詞。你可以幫他找出所有組合嗎？

輸入
輸入包含三行：
第一行為數個主詞以空白分開，資料型態為字串
第二行為數個動詞以空白分開，資料型態為字串
第三行為數個受詞以空白分開，資料型態為字串

輸出
輸出為所有造句組合，依序使用不同的主詞、動詞、受詞，每個造句都換行

輸入範例 1 
Kevin Wayne
likes buys
donuts coffee

輸出範例 1
Kevin likes donuts
Kevin likes coffee
Kevin buys donuts
Kevin buys coffee
Wayne likes donuts
Wayne likes coffee
Wayne buys donuts
Wayne buys coffee

輸入範例 2 
aa bb cc dd
11 22 33
xx yy

輸出範例 2
aa 11 xx
aa 11 yy
aa 22 xx
aa 22 yy
aa 33 xx
aa 33 yy
bb 11 xx
bb 11 yy
bb 22 xx
bb 22 yy
bb 33 xx
bb 33 yy
cc 11 xx
cc 11 yy
cc 22 xx
cc 22 yy
cc 33 xx
cc 33 yy
dd 11 xx
dd 11 yy
dd 22 xx
dd 22 yy
dd 33 xx
dd 33 yy

來源
ccClub Judge
"""

s = input().split()
v = input().split()
o = input().split()
for i in s:
    for j in v:
        for k in o:
            print(i, j, k)
            