"""
被刪除的字元

描述
有一只含有英文字母的字串
s（s[i]∈A⋯Z∪a⋯z），我們將s打亂，更動部分大小寫（對於某些字元c∈s，若c為大寫則改為小寫，反之亦然）後刪除一個字元成為字串t。現給定s以及t，試找出被刪除的字元。

輸入
輸入有多組測試資料。第一行為一個數字t，為測試資料的數量。每組測試資料有兩行，第一行為字串s，第二行為字串t。

輸出
對於每組測試資料，每筆測試資料佔一行。輸出一個字元c（固定小寫），代表c為t中被刪除的字元。

輸入範例 1
3
HELLOEXAM
xElAHoEL
thisisthesecondtestcase
shTAsiendTstEtEsocIsHC
UPPERlowerCaSe
pPlCewAESRUrO

輸出範例 1
m
e
e

輸入範例 2
5
gkOwqvrzbRryhROVQwnzrAJvCwqWDTwrTIJEDIDzYTPVBoQ
ObwRycRqhDqzEvVdwRnGBoOwIRzJziPTtQDRvVkwWQTRJy
qgjukDyzZfr
zygruzdqKj
IIvNXKwVLWqpTLcYZhEzblqmMMTWCDAVBunzWMdMSBjreKflQVsREzpCMzDEuVHDQPyiKRzpUx
KLfXUdIRpMvHzzplpcubzLNdENZMTTmJzhpXbWMrRkSMvCyDzucvMkvSIeWBaweqQIQqDlvWE
FPSdgAPScmcbSNqoWhbVhmRHyZmYFWKydwskZfseDDZiLKmrZxgbsBkbOpANxtDNTWQAbrSjTTCXtfACmMDY
dbyHBNDCqYgWCdYBhkhSfzbceKsrDmonrwaWFsstQIrXvmjzmxCTAPKxdLTAZfOPTMNZTdSmbpgKBmSYsAF
fxpgKWZPMGAatTXyNnfVZRbsgWDcEGuEHbXyKTJoVWchsvzDbJEFMFOboeCcYKrKdpAtFQS
GcENCFSGzmsbBKXJAFdGucECzfyphAVdNgDjFPZsbOrQhfXWKobTTywmPYWTKKtVXOEAeV

輸出範例 2
a
f
y
w
r

提示
5≤t≤20
s[i],t[i]∈A⋯Z∪a⋯z
1≤∣s∣≤100,∣s∣=∣t∣+1

"""