"""
字首學習法 II

描述
小明最近在準備指考7000單，背得很辛苦的他看到了別人推薦使用字根字首來記憶。
你能幫他整理一下他單字本裡面的單字有哪些共同字首嗎？
請實作一個 function，來完成這個任務吧！
本題只需實作函式，不需要自己處理輸入和輸出

輸入
請實作一個函式 find_prefix。
函式包含一個參數word_lst，為一個串列，包含數個字串（即要記憶的英文單字）。

輸出
函式有一個回傳值。
若word_lst 中有共同字首，則回傳該字首。
若word_lst 中無共同字首，則回傳 None。

輸入範例 1 
find_prefix(["statue", "stand", "student"])

輸出範例 1
st

輸入範例 2 
find_prefix(["dog", "cat", "does"])

輸出範例 2
None
"""

def find_prefix(word_lst):
    answer = ""
    if not word_lst:
        return answer
    word_lst_sort = sorted(word_lst)
    length = len(word_lst_sort[0])
    for i in range(length):
        if word_lst_sort[0][i] == word_lst_sort[-1][i]:
            answer += word_lst_sort[0][i]
        else:
            break
    if not answer:
        answer = None
    return answer

print(find_prefix(["statue", "stand", "student"]))
print(find_prefix(["dog", "cat", "does"]))
