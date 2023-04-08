"""
[5-3] 設計密碼
Description

經過 cc 盜賊的洗劫後，設計密碼鎖的鎖匠很不服氣，決定再設計一個密碼鎖跟 cc 盜賊一決高下。鎖匠設計的密碼規則是取字串奇數位的字元成為密碼提示，可以請你幫年邁的鎖匠寫密碼提示的程式碼嗎？


Input
輸入為 1 個字串，表最終密碼。


Output
輸出為 1 個字串，表處理過後的密碼提示。


Sample Input 1 
I love programming

Sample Output 1
Ilv rgamn

Sample Input 2 
苟日新 日日新 又日新

Sample Output 2
苟新日新又新

Hint
請利用字串切割(Slicing) 字串[起始位置: 結束位置: 間隔值]
題目要求取奇數位的字元，第1個字元在字串中的位置為0，第3個字元在字串中的位置為2，以此類推

Source
ccClub Judge
"""