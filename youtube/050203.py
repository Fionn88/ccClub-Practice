"""
[5-2] 阿能改考卷
Description

阿能每次考完小考老師都會要求交換改，但每次交換改阿能都覺得很無聊。因此突發奇想，想說如果作答方式改成線上作答，改起來就會相當地方便。想請你模擬一下改一題選擇題的程式碼。


Input
輸入為兩行，第一行為正確解答的選項，第二行為同學的答案。


Output
輸出為一行，若同學的答案與正確答案相同請輸出 True，否則請輸出 False。


Sample Input 1 
A
B

Sample Output 1
False

Sample Input 2 
C
C

Sample Output 2
True

Source
ccClub Judge
"""
correct = input()
student_ans = input()
print(correct == student_ans)