"""
字首學習法

描述
小明最近在準備指考7000單，背得很辛苦的他看到了別人推薦使用字根字首來記憶。
你能幫他整理一下他單字本裡面的單字有哪些共同字首嗎？

輸入
輸入為一行，每個詞彙用逗號區分

輸出
輸出為一行，全部字串裡面的共同字首
如果沒有共同字首，請輸出 "No common"

輸入範例 1 
statue,stand,student

輸出範例 1
st

輸入範例 2 
dog,cat,does

輸出範例 2
No common
"""

def find_common_prefix(words):
    if not words:
        return "No common"
        
    min_word = min(words, key=len)
    
    for i, char in enumerate(min_word):
        if not all(word[i] == char for word in words):
            min_word =  min_word[:i]
    
    if min_word:
        return min_word
    else:
        return "No common"

input_words = input().split(",")
common_prefix = find_common_prefix(input_words)
print(common_prefix)


# ================ The Other Solution ================
import os
lst = input().split(',')
result = os.path.commonprefix(lst)
if result:
    print(result)
else:
    print('No common')
