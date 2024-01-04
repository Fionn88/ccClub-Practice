"""
子字串辨識

描述
請實作一個函式isSubStr，在給定兩字串 s 以及 t 的狀況下，請判斷字串 s 是否為字串 t 的子字串，並回傳True或False。子字串的定義為：我們可以由字串 t 刪去不特定數量的字元得到字串 s ，且不能更動字元的相對順序。舉例來說：
EX1: s = ‘ace’, t = ‘abcde’, t 只要刪掉 'b' 和 'd' 就可以變成指定的字串 s ，回傳True
EX2: s = ‘adc’, t = ‘abcde’, t 無論刪掉什麼 element 都無法變成 s，回傳False

輸入
函式有兩個參數 s 和 t，型態皆為字串。

輸出
函式有一回傳值 True 或 False。

輸入範例 1
ace
abcde

輸出範例 1
True

輸入範例 2
adc
abcde

輸出範例 2
False

來源
ccClub Judge
"""

def isSubStr(s, t):
    s_ptr = 0 
    t_ptr = 0 

    while t_ptr < len(t) and s_ptr < len(s):
        if s[s_ptr] == t[t_ptr]:
            s_ptr += 1 
        t_ptr += 1

    return s_ptr == len(s) 
