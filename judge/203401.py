"""
超商取貨
描述

在網拍大行其道的現在，去超商取貨已經成為現代人幸福的來源之一：在網路上下訂單之後，心心念念某天回家經過超商可以順便拿變成喜歡的樣子的工資。超商取貨多半靠手機後三碼找出按後三碼分門別類堆起來的商品後，再搭配身分證件確認取貨人身分。現在，給定商品進貨時的資訊與取貨人報的後三碼，你可以正確地指出誰買了什麼嗎？
保證不會出現姓名及電話後三碼都相同的情形，但有可能出現撞名（但後三碼不一樣），或電話後三碼一樣（但名字不同）的情況。


輸入
輸入包含 n + m + 1 行。
前 n 行是進貨資訊，每行包含 10 碼的電話號碼、取貨人姓名、物品，以逗號分隔。
接下來為 end，代表已經讀完進貨資訊了。
最後 m 行是取貨人資訊，每行包含取貨人電話後 3 碼、取貨人姓名，以空格分隔。


輸出
輸出有 m 行，為對應的取貨物品。
若查不到取貨人資訊，該行請輸出 Check again!


輸入範例 1 
0912345678,Kevin,Artis
0988123456,KT,white coat
0999123456,yeutong,sour map
0997846678,yuhsuan,ching goat
end
678 yuhsuan
678 Xiao ming

輸出範例 1
ching goat
Check again!

輸入範例 2 
0969322347,Krishna,Bird
0973644044,Krishna,Beaver
0993524003,Towney,Duck
end
347 Krishna
044 Tommy Lee

輸出範例 2
Bird
Check again!
"""
infoDic = {}
while True:
    user_input = input()
    if user_input == 'end':
        break
    else:
        info = user_input.split(',')
        name = info[2]
        muti_key = info[0][7:],info[1]
        infoDic.update({muti_key:name})
        
        muti_key = info[0][7:],info[2]
        name = info[1]
        infoDic.update({muti_key:name})

while True:
    try:
        user_input = input().split(' ',1)
        search = user_input[0],user_input[1]
        print(infoDic.get(search,'Check again!'))
    except:
        break