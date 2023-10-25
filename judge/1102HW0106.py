"""
金牌特務 ll
描述

寧寧也是隸屬金士曼特務集團的一員，但是因為有三高的問題，所以在職久久仍無法被外派，身為辦公室老屁股的他，早就對工作失去了熱情，為了要提高工作效率好早點結束這無聊的工作，他打算發明一種更簡單的打字機去幫完成加密文件，他需要的功能如下:

如果傳進來是數字的話:

如: 1234

@ 代表將其以十進位的方式表現，即為(1*1000+2*100+3*10+4)

# 代表歸零 ，即為 0

*  代表自己的平方 (例如: 1234**2)，即為 1522756

= 代表將數字倒轉 ，即為 4321

如果傳進來是文字的話

如: APP

@ 代表用字串的長度當作平移的量去做凱薩密碼的轉換，即 APP 的長度為 3，故將每個英文字母平移 3，即 DSS

# 代表清空

* 將字串重複一次，即 APPAPP



注意，文字只有三種指令，沒有 =，如果出現文字搭配 =，請回傳 "Error"
數字必在四位數以內，也就是(1～9999)
文字必為英文大寫字母可能由 1～3 個字母組成

輸入
共有 2 行，

第 1 行可能是數字或文字

第 2 行代表指令可能有(#*@=)


輸出
共 1 行，將數字獲字串依規則進行處理後輸出


輸入範例 1 
1234
@

輸出範例 1
1*1000+2*100+3*10+4

輸入範例 2 
AB
@

輸出範例 2
CD

輸入範例 3 
1234
#

輸出範例 3
0
"""