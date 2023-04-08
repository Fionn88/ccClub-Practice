"""
[5-3] 破解密碼
Description

cc 怪盜喜歡破解別人的密碼盜取收藏的寶物，最近得知一家人的密碼鎖有個 bug，要解鎖的話一開始會秀出一段字串，要立馬輸入字串的長度，否則裡面的寶物就會自動被銷毀。


Input
輸入為 1 個字串。


Output
輸出為 1 個整數，請輸出字串的長度


Sample Input 1 
大大大優惠!

Sample Output 1
6

Sample Input 2 
7777777777777777777777777

Sample Output 2
25

Source
ccClub Judge
"""
s = input()
print(len(s))