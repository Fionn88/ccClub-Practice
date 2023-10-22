"""
ccClub 有 c 哈
描述

這個夏天，大陸有三檔嘻哈綜藝節目上檔，小明發現這些饒舌歌手們用英文的時候很喜歡用錢字號來代替 s ，好像很潮，所以他決定他也要這樣子，來顯得自己不那麼宅；他決定以後每次遇到 s ，不論大小寫，不管三七二十一都把他改成錢字號，你可以寫一個程式來幫小明做到這件事嗎？


輸入
輸入為一行，包含一段文字。


輸出
輸出為一行，為處理後的文字。


輸入範例 1 
gangster

輸出範例 1
gang$ter

輸入範例 2 
he has no chance

輸出範例 2
he ha$ no chance
"""

s = input()
for index,value in enumerate(s):
    if index == len(s)-1:
        if value == 's' or value == 'S':
            print('$')
        else:
            print(value)
    else:
        if value == 's' or value == 'S':
            print('$',end='')
        else:
            print(value,end='')
