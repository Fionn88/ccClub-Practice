"""
又是喵球
描述

喵球寫英文字時有個特別的習慣，依照 a~z 的順序，如果是 m 或排序在 m 以前的字母，那麼喵球會習慣總是寫成大寫，而在 n 或 n 之後的字母則一律寫成小寫(不論看到的時候是大寫還是小寫)，你能幫喵球把看到的字串轉換成慣用的寫法嗎？


輸入
一行，輸入為一個字串，只會出現大小寫的 a~z 和空格


輸出
一行，輸出為一個字串


輸入範例 1 
ccClub

輸出範例 1
CCCLuB

輸入範例 2 
ABCXYZ

輸出範例 2
ABCxyz
"""

s = input()
for i in s:
    if ord(i.lower()) <= ord('m'):
        print(i.upper(),end='')
    else:
        print(i.lower(),end='')
