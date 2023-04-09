"""
[5-5] 標記關鍵字
Description

此題為填空題。

輸入一個關鍵字與一個字串，請在字串中找到關鍵字，並以雙引號(")標記起來。


Input
輸入有兩行，第一行為一個關鍵字，第二行為待處理字串。


Output
輸出為一行，請輸出標記過關鍵字的字串。


Sample Input 1 

Python
美國批踢踢 Reddit、以前做分組報告很依賴的 Dropbox 、號稱中國最優質社群但差點消失的知乎、你每天發限時動態的 Instagram ，都主要是由 Python 來寫的！

Sample Output 1
美國批踢踢 Reddit、以前做分組報告很依賴的 Dropbox 、號稱中國最優質社群但差點消失的知乎、你每天發限時動態的 Instagram ，都主要是由 "Python" 來寫的！

Sample Input 2 
像極了愛情
曖昧上頭的那幾秒，像極了愛情

Sample Output 2
曖昧上頭的那幾秒，"像極了愛情"

Hint
字串替換的用法為：字串.replace(舊字串, 新字串, 最大替換次數)
雙引號 " 為python中用來標示字串的特殊字，因此若輸出的內容中，希望包含雙引號，則需使用跳脫字元

Source
ccClub Judge
"""

# 輸入關鍵字與
keyword = input()
text = input()

# 標記關鍵字
marked_text = text.replace(keyword, '\"'+ keyword + '\"')

# 輸出結果
print(marked_text)
