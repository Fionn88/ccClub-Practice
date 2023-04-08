"""
[5-4] 小明跟哥哥差幾歲
Description

給定小明和哥哥今年的年紀，請以範例形式輸出小明跟哥哥的歲數差


Input
輸入為兩行，第一行為小明今年的年紀，第二行為小明哥哥今年的年紀。


Output
輸出為一行，請輸出小明和哥哥差幾歲(已知小明和哥哥一定差 2 歲以上)。


Sample Input 1 
10
12

Sample Output 1
They are 2 years apart.

Sample Input 2
9
14

Sample Output 2
They are 5 years apart.

Hint
經計算可求得小明與哥哥相差的歲數，此歲數的資料型態為 int
依照題目輸出要求，請將該相差歲數進行資料型態轉換，以字串的形式重新組合成句子。
字串間可以使用加號進行連接

Source
ccClub Judge
"""
n1 = int(input())
n2 = int(input())
ans = n2 - n1
print("They are", ans, "years apart.")