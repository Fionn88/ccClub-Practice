"""
小明的電話簿
描述

小明一直都沒有做紀錄的習慣，這也讓他常常想不起來別人的聯絡方式。

某一天，小明下定決心買了一本空白的電話簿，這本電話簿的功能只有兩種：

加入聯絡人，指令的代號為 'a' ，請在電話簿當中加入給定的名字以及其聯絡電話。
查詢聯絡人，指令的代號為 's' ，若給定名字請尋找其電話，若給定電話請尋找該聯絡人姓名，若電話簿中不存在該姓名或是電話，請輸出 'Cannot find [Name/Phone Number]'
請幫忙小明完成這個電話簿的建置。


輸入
輸入為數行，除最後一行為'end'外，若首字元為 'a' ，後面會包含兩個字串，各為姓名以及電話；若首字元為 's'，後面會包含一個字串，為姓名或是電話。


輸出
輸出為數行，與輸入為 's' 的數量相同。


輸入範例 1 
s MICHAEL
a JAMES 8942750136
a HANNAH 3658492071
s 8942750136
s 5239847016
a LAUREN 4857190632
end

輸出範例 1
Cannot find MICHAEL
JAMES
Cannot find 5239847016

輸入範例 2 
s BETHANY
end

輸出範例 2
Cannot find BETHANY

來源
ccClub Judge
"""

infoDic = {}
while True:
    user_input = input()
    if user_input == 'end':
        break
    else:
      user_input = user_input.split()
      if user_input[0] == 'a':
        infoDic[user_input[1]] = user_input[2]
        infoDic[user_input[2]] = user_input[1]
      elif user_input[0] == 's':
        if infoDic.get(user_input[1]) == None:
          print('Cannot find',user_input[1])
        else:
          print(infoDic.get(user_input[1]))
