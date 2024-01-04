"""
母音個數排序

描述
給定數個字串，請將這些字串依照字串中的母音個數排序，由小到大。

輸入
輸入有不定行，各包含一個字串

輸出
輸出有不定行，與輸入行數相同，各包含一個字串

輸入範例 1 
apple
bird
elephant

輸出範例 1
bird
apple
elephant

輸入範例 2 
ruby
c++
c
python
go
java

輸出範例 2
c++
c
ruby
python
go
java

來源
ccClub Judge
"""

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

voc = []
try:
    while True:
        s = input()
        voc.append((s, count_vowels(s)))
except EOFError:  
    pass

voc.sort(key=lambda x: x[1])

for item in voc:
    print(item[0])
