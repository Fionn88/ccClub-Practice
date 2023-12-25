"""
身分證字號II
描述

中華民國身分證字號共十碼，包含一個英文字母及九個數字，其編號的規則請參考：維基百科。

本題將輸入一個英文字母及數字部分後八碼，請依照編碼規則判斷此身分證字號的擁有者是男性或女性。

本題只需實作函式，不需要自己處理輸入和輸出


輸入
輸入有兩行。

第一行為一個英文字母，代表縣市。

第二行為身分證字號數字部分後八碼。


輸出
輸出為一行，字串 Male 或 Female


輸入範例 1 
ID_gender(city="A", num="87883299")

輸出範例 1
Male

輸入範例 2 
ID_gender(city="D", num="00466791")

輸出範例 2
Female

提示
sample input 1 中，若分別把代表男性（1）和女性（2）的數字代入後，可得 A187883299 和 A287883299 兩組身分證字號。
經由身分證字號規則驗證後會發現，A187883299 這組是合法的，而 A287883299 是不合法的身分證字號，因此可以判斷答案為男性（Male）。
"""

def ID_gender(city, num):
  number = list(map(int,num))
  index = 0
  amount = 0
  verify = [7, 6, 5, 4, 3, 2, 1, 1]
  authorizeDict = {'A': 1, 'B': 0, 'C':9, 'D':8,'E':7,'F':6,'G':5,'H':4,'I':9,'J':3,'K':2,'L':2,'M':1,'N':0,'O':8,'P':9,'Q':8,'R':7,'S':6,'T':5,'U':4,'V':3,'W':1,'X':3,'Y':2,'Z':0}
  for i in number:
    amount += i * verify[index]
    index += 1
  amount += authorizeDict.get(city)
  amount += 8
  if amount % 10 == 0:
    return "Male"
  else:
    return "Female"
