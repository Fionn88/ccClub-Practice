"""
[5-綜合] cc 文字獄
Description

cc 為了適當管理網路上不必要的仇恨言論，將一些字列為禁字。若有人不小心使用了禁字，系統會以星號(*)完全代替禁字，回傳禁字處理後的結果。


Input
輸入為兩行，第一行為禁字，第二行為待處理字串。


Output
輸出為一行，請輸出原字串與處理後的字串，兩字串間以等號作為間隔。


Sample Input 1 
病毒
病毒菜刀

Sample Output 1
**菜刀

Sample Input 2 
小熊維尼
小熊維尼是艾倫·亞歷山大·米恩為他的兒子創作的一隻熊造型卡通形象

Sample Output 2
****是艾倫·亞歷山大·米恩為他的兒子創作的一隻熊造型卡通形象

Hint
可由第一行禁字的字串長度，決定應該使用幾個星號。

Source
ccClub Judge
"""
ban = input()
s = input()
print(s.replace(ban,"*"*len(ban)))