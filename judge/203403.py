"""
資料比對
描述

小明最近在處理資料的問題，他手上有一份別人傳來處理過的資料。
每一行是一個資料點，每行以 TAB 區隔，TAB 之前是句子的分類，TAB 之後是去除過符號、全部轉成小寫的句子。
但今天小明因為看了達文西密碼，覺得符號也是重要的一件事。因此他想要取回符號去除前完整版的原始句子，同時又要讓標記好的分類不要遺失。
不過情況也不一定那麼理想，不是每個句子都可以找到還帶有符號的原始句子。因此如果對不上的話也沒有辦法，就繼續用沒有符號，清理過的句子。你可以利用程式幫他達成這件事嗎？

舉例來說，若輸入為：

label-data.tsv
label__1 i am a good boy
label__0 i am a bad boy
label__1 i am a good girl
raw-data.txt
I am a good boy!!!
I: am a good girl#$%^&?!
You should see THE SEA!
Kevin's Artis is very...large...
label-data.tsv 代表標註過後轉成小寫的資料，raw-data.txt 代表沒有經過任何處理的資料。其中，label-data.tsv 資料中的第一句跟第三句可以在 raw-data.txt 中找到，故輸出時按順序輸出找回符號的資料，搭配標記的標籤輸出；i am a bad boy 這句因為找不到，所以就輸出 label-data.tsv 中沒有符號的版本就可以了。


輸入
輸入有 n + m + 2 行。
第一行是 "label-data.tsv"，代表標記過的資料檔案名稱。
接下來 n 行是標記過的資料，每行以 TAB 區隔，TAB 之前是句子的分類，TAB 之後是去除過符號、全部轉成小寫的句子。
再來是 "raw-data.txt"，代表原始資料檔案名稱。
最後 m 行是原始資料。


輸出
輸出有 n 行，以 label-data.tsv 的資料讀取順序輸出，每行以 TAB 區隔分類及句子內容。


輸入範例 1 
label-data.tsv
label__1	i am a good boy
label__0	i am a bad boy
label__1	i am a good girl
raw-data.txt
I am a good boy!!!
I: am a good girl#$%^&?!
You should see THE SEA!
Kevin's Artis is very...large...

輸出範例 1
label__1	I am a good boy!!!
label__0	i am a bad boy
label__1	I: am a good girl#$%^&?!

輸入範例 2 
label-data.tsv
label__2	this is ccclub
label__3	not cclub
raw-data.txt
This is ccClub.
Not "cccclub"!

輸出範例 2
label__2	This is ccClub.
label__3	not cclub

輸入範例 3 
label-data.tsv
label__2	hi  good morning
label__3	im fine
label__7	goodbye
raw-data.txt
Hi.  Good morning!
I'm fine.
Good...Bye...

輸出範例 3
label__2	Hi.  Good morning!
label__3	I'm fine.
label__7	Good...Bye...

提示
本題可以嘗試看看用 python 套件 re 試試看！
google 關鍵字：python re replace symbol 之類的
"""

# ===================== Partial Accepted ====================
import re
label_data = []
label = []
raw_data = []
ans = []

while True:
    try:
        line = input()
        if line == "label-data.tsv":
            continue
        label.append(line.split("\t")[0].strip())
        label_data.append(line.split("\t")[1].strip())
    except:
        break

while True:
    try:
        line = input()
        if line == "raw-data.txt":
            continue
        raw_data.append(line)
    except:
        break

for index,i in enumerate(label_data):
    flag = False
    for j in raw_data:
        if re.sub(r'[^a-zA-Z0-9\s]+', '', i) == re.sub(r'[^a-zA-Z0-9\s]+', '', j.lower()):
            ans.append(label[index]+"\t"+j)
            flag = True
            break

    if not flag:
        ans.append(label[index]+"\t"+i)
for i in ans:
    print(i)
