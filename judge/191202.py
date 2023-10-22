"""
字母總和排序
描述

請實作一個函式sort_dict

def sort_dict(s):
    # do something
    return lst
請依照字典序和(ex. car = 3+1+18 =22)，由小而大排列給定的詞並排序

PS 本題只需實作函式，並不用自行處理 input()


輸入
函式有一個參數：

s: 型態為 str，包含數個詞，詞和詞之間以空格分割

輸出
函式有一個回傳值：

型態為 list，串列中的每個元素型態為 str

輸入範例 1 
sort_dict("It is a myth")

輸出範例 1
['a', 'is', 'It', 'myth']

輸入範例 2 
sort_dict("band zip car")

輸出範例 2
['band', 'car', 'zip']

輸入範例 3 
sort_dict("budget branch beware bargain boast beneath")

輸出範例 3
['branch', 'bargain', 'beware', 'beneath', 'boast', 'budget']

提示
備註：
大寫 A 和小寫 a對應的字典序皆為 1 ，大寫 B和小寫 b 對應的字典序皆為 2，依此類推，大寫 Z 和小寫 z 對應的字典序皆為 26

來源
ccClub Judge
"""

def sort_dict(s):
  sorted_words = sorted(s.split(), key=get_word_value)
  return sorted_words

def get_word_value(word):
    total = sum(ord(c.lower()) - ord('a') + 1 for c in word)
    return total
