"""
字母麥片
描述

小胖仔正值中二年華，常常有些奇怪的行為，像是走在人行道的時候只准自己走在導盲磚上、對著運轉中的電風扇吹氣又或是把冰箱門慢慢關起來看什麼時候燈會熄滅。

這天他在吃早餐的時候不小心倒了太多字母麥片，他看著一整碗的麥片突發奇想，決定把麥片一片片挑出來，如果有重複的字母他就不吃。

請問各位可以幫忙告訴他哪些麥片要吃嗎？


輸入
一行，皆為小寫字母，保證至少有一個單獨的字母，各自用”,” 分隔



輸出
一行，請將輸出的字母照原本順序排好，也用”,” 分隔


輸入範例 1 
a,a,c,b,a

輸出範例 1
c,b
"""

from collections import Counter

def get_unique_letters(s):
    letter_counts = Counter(s)  # 計算字母出現次數
    unique_letters = [letter for letter, count in letter_counts.items() if count == 1]  # 找出只出現一次的字母
    return unique_letters

s = input()
result = get_unique_letters(s)
print(','.join(result))
