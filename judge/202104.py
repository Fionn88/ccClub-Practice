"""
小明審報名表 2

描述
又到了半年一度的 ccClub 報名季節，由於報名人數眾多，小明想要設計自己的一套機制來篩選報名表，並且寫成程式來加快審報名表的速度，他心中的規則如下：
報名表可以打 1-10 分，小明以 5 分為基準，給定姓名、學校、系級、電子信箱、自我介紹、動機、每周願意花的時間、備註 8 個欄位，審核機制如下：

小明的情敵是小華，所以如果小華來報名，他一定給他最低分 1 分
小明覺得念哪個學校不重要，想學習的心才是最重要的，所以學校不管怎麼樣都不會影響到分數
小明覺得會計系的人學會計應該心很累，所以會需要程式的調劑，所以只要是會計相關的系所出現，小明都會多給 1 分
小明覺得忘記填電子信箱的人應該是來亂的，所以無論如何給最低分 1 分
小明覺得自我介紹寫的落落長很討人厭，所以大於 200 字他就扣 1 分；但寫太少少於 50 字太沒誠意也要扣 1 分
小明覺得動機很重要，所以如果用心寫大於 100 字就加 1 分
小明覺得如果一周只願意花不到 5 個小時學習寫程式也太懶散了，扣 1 分；但如果願意花 10-16 個小時就應該加 1 分；17 小時(含)以上充滿誠意，加 3 分
小明覺得會在備註刷存的人多半是有趣的，所以如果在備註有寫東西，只要多於 30 個字就加 1 分
給定一份報名表，你可以幫小明完成這樣的程式嗎？

補充說明：

會計相關系所的意思是系級中包含「會計」的字樣
信箱沒填代表該欄位為空字串
每週願意花的時間可能格式為：「n 小時 m 分鐘」或 「n 小時」
此題純屬虛構，請勿當真。

輸入
輸入為八行，分式是姓名、學校、系級、電子信箱、自我介紹、動機、每周願意花的時間、備註 8 個欄位的內容。

輸出
輸出為一行，包含一個數字，代表該報名表獲得的分數。

輸入範例 1 
小華
cc大學
會計四
123@example.com
挖細小華啦嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿
阿就想學咩
25 小時
無

輸出範例 1
1

輸入範例 2 
kevin
cc大學
會計四
123@example.com
挖細小華ㄟ冰有啦嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿黑
阿就想學咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗咩噗
17 小時 49 分鐘
嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿選我

輸出範例 2
10
"""

name = input()
school = input()
department = input()
email = input()
introduce = input()
motivate = input()
spend_time = input().split('小時')
notes = input()
breakOrNot = False

if name == "小華":
    print(1)
    breakOrNot = True
elif email == "":
    print(1)
    breakOrNot = True

count = 5
if not breakOrNot:
    if "會計" in department:
        count += 1
    if len(introduce) > 200 or len(introduce) < 50:
        count -= 1
    if len(motivate) > 100:
        count += 1

    timeToSpendInt = int(spend_time[0])

    if timeToSpendInt < 5:
        count -= 1
    elif timeToSpendInt >= 10 and timeToSpendInt <= 16:
        count += 1
    elif timeToSpendInt >= 17:
        count += 3

    if len(notes) > 30:
        count += 1

    if count > 10:
        count = 10
    
    print(count)
