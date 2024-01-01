"""
來對發票囉

描述
領獎日期快要過ㄌ，小雷發現自己還沒對發票，但他是大大大懶蟲，覺得對發票很麻煩，可以請聰明的你們幫小雷製作一個對發票的機器嗎？在他輸完一連串的發票號碼後，跟他說哪幾張發票有中獎，並且總共中多少錢呢？

注意：

中獎獎項及金額的規定請參考Hint
中獎之統一發票，每張按其最高中獎獎別限領1個獎金
特別獎、特獎與頭獎的號碼不會完全一樣
增開六獎的號碼不會與頭獎的末三碼相同

輸入
共兩列，

第一列為「特別獎,特獎,頭獎1,頭獎2,頭獎3,增開六獎」（以 ',' 相隔，有六項）

第二列為小雷擁有的發票號碼，不確定有幾項（以 ',' 分隔）


輸出
1. 第一行為中獎的發票號碼，輸出要按照發票的號碼依首位數字大小排列，小在前，大在後，若首位數字大小相同，則比較第二位數字，若再相同，繼續向後比較數字大小；
若沒有中獎，則輸出 ''No match numbers''
2. 第二行為中獎的總獎金；若未中獎則總獎金為 0


輸入範例 1 
31150905,28564531,05754219,52891675,45327106,252
31150905,11115252,44434219,23191675,00299334,67384621

輸出範例 1
['11115252', '23191675', '31150905', '44434219']
10005200

輸入範例 2 
31150905,28564531,05754219,52891675,45327106,252
31150252,11115252,44434252,23191252,00299252,67384252

輸出範例 2
['00299252', '11115252', '23191252', '31150252', '44434252', '67384252']
1200

提示
以 sample input 1 為例:

====================
圖片至 judge 查看
====================
"""

prizeNumber = input().split(',')
potentialNumber = input().split(',')
res = []
prizes = 0
for i in potentialNumber:
    if i == prizeNumber[0]:
        prizes += 10000000
        res.append(i)
    elif i == prizeNumber[1]:
        prizes += 2000000
        res.append(i)
    elif i == prizeNumber[2] or i == prizeNumber[3] or i == prizeNumber[4]:
        prizes += 200000
        res.append(i)
    elif i[-7:] == prizeNumber[2][-7:] or i[-7:] == prizeNumber[3][-7:] or i[-7:] == prizeNumber[4][-7:]:
        prizes += 40000
        res.append(i)
    elif i[-6:] == prizeNumber[2][-6:] or i[-6:] == prizeNumber[3][-6:] or i[-6:] == prizeNumber[4][-6:]:
        prizes += 10000
        res.append(i)
    elif i[-5:] == prizeNumber[2][-5:] or i[-5:] == prizeNumber[3][-5:] or i[-5:] == prizeNumber[4][-5:]:
        prizes += 4000
        res.append(i)
    elif i[-4:] == prizeNumber[2][-4:] or i[-4:] == prizeNumber[3][-4:] or i[-4:] == prizeNumber[4][-4:]:
        prizes += 1000
        res.append(i)
    elif i[-3:] == prizeNumber[2][-3:] or i[-3:] == prizeNumber[3][-3:] or i[-3:] == prizeNumber[4][-3:]:
        prizes += 200
        res.append(i)
    elif i[-3:] == prizeNumber[5]:
        prizes += 200
        res.append(i)

if res:
    res.sort()
    print(res)
else:
    print("No match numbers")
    
print(prizes)
