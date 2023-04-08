"""
[5-1] 阿能的段考
Description

此題為填空題。

阿能剛考完第一次段考，但因為剛考完腦袋還有點不太清楚，可以請你幫阿能算一下這次段考的總分和平均嗎？


Input
輸入為 5 行，為 5 個整數，分別為國文、英文、數學、社會和自然的段考分數。


Output
輸出為 2 行，第一行為總分，第二行為平均分數。


Sample Input 1 
80
92
93
84
88

Sample Output 1
437
87.4

Sample Input 2 
72
85
96
82
88

Sample Output 2
423
84.6

Hint
請於作答區底線處，填入正確內容，完成題目要求。
作答時請將底線移除，替換成正確內容。

Source
ccClub Judge
"""

# 輸入各科成績
chinese = int(input())
english = int(input())
math = int(input())
social = int(input())
science = int(input())

# 計算段考總分
# total = _________
total = chinese+english+math+social+science

# 計算段考平均
# average = __________
average = (chinese+english+math+social+science)/5

# 輸出
print(total)
print(average)
