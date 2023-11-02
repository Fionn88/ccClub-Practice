"""
凱凱堆積木 II
描述

凱凱的姪子嘻嘻升上國小後，簡單的規則已經難不倒他了，凱凱決定設計更複雜的堆積木方式。

積木上有著英文字母和數字，嘻嘻必須依照凱凱的需求，把積木堆成凱凱想要的樣子。

每一次堆積木之前，凱凱會跟嘻嘻說希望堆幾層的積木，以及最上面那層的積木數量 k（1<= k）。

對於一個 N 層的積木塔，從上數下來的第 i 層（1<= i <= N），必須要有 i+k-1 個積木。

舉例來說，一個三層的積木塔，k = 2 的情況下，第一層（最上面那層）會有 2 個積木，第二層（中間那層）會有 3 個積木，第三層（最下面那層）會有 4 個積木。

此外，為了要讓自己輕鬆一點，凱凱希望增加堆積木的困難度，讓嘻嘻需要多花費和精力在堆積木上，自己才能在一旁滑手機上 PTT 和 Dcard。積木排列的方式必須依照大寫字母順序（A, B, C, ..., X, Y, Z）、小寫字母順序（a, b, c, ..., x, y, z）、數字順序（1, 2, 3, ..., 9, 0），從最上面那層開始，如果層數除 3 於 1 則堆大寫英文字母的積木，層數除 3 於 2 則堆小寫英文字母的積木，層數除 3 於 0 則堆數字積木。

如果是英文字母的積木，堆到 Z 之後，下一個要從 A 開始（堆到 z 之後，下一個從 a 開始），並且繼續依序往下堆。若是數字的積木，堆到 9 之後，下一個要從 0 開始，並且繼續依序往下堆。

關於堆積木的例子可參考下面範例測資。


輸入
輸入有兩行。

第一行包含一個正整數，代表需要堆的積木層數 N。

第二行包含一個正整數，代表最上面那層的積木數量 k。


輸出
輸出有 n 行。

每一行包含一個字串，代表該層依序使用的積木種類。


輸入範例 1 
1
1

輸出範例 1
A

輸入範例 2 
5
1

輸出範例 2
A
ab
123
BCDE
cdefg

輸入範例 3 
6
3

輸出範例 3
ABC
abcd
12345
DEFGHI
efghijk
67890123

輸入範例 4 
23
3

輸出範例 4
ABC
abcd
12345
DEFGHI
efghijk
67890123
JKLMNOPQR
lmnopqrstu
45678901234
STUVWXYZABCD
vwxyzabcdefgh
56789012345678
EFGHIJKLMNOPQRS
ijklmnopqrstuvwx
90123456789012345
TUVWXYZABCDEFGHIJK
yzabcdefghijklmnopq
67890123456789012345
LMNOPQRSTUVWXYZABCDEF
rstuvwxyzabcdefghijklm
67890123456789012345678
GHIJKLMNOPQRSTUVWXYZABCD
nopqrstuvwxyzabcdefghijkl

提示
前 10 筆測資為 k = 1 的狀況，可先考慮簡化後的情形。
"""

N = int(input())
k = int(input())
sum_num = 0
sum_bigstr = 0
sum_smallstr = 0
for i in range(1,N + 1) :
    if k == 0 :
        print()
        continue
    for j in range(1,k + i) :
        if i % 3 == 0 :
            sum_num += 1
            sum_num %= 10
            print(chr(ord('0')+ sum_num),end = '')
        else :
            if i % 3 == 1 :
                print(chr(ord('A') + sum_bigstr),end = '')
                sum_bigstr += 1
                sum_bigstr %= 26
            if i % 3 == 2 :
                print(chr(ord('a')+ sum_smallstr),end = '')
                sum_smallstr += 1
                sum_smallstr %= 26  
    print()
