"""
NTU等第

描述
台大成績採等第制，百分制和等第制約略依照以下對照表計分。
在這題中，我們希望用戶輸入一個百分制的成績，依照下方對照表計算出該分數的等第制成績。

輸入
輸入為一行，包含一個數字，代表百分制成績。


輸出
輸出為一行，包含一個字串，代表等第制成績。


輸入範例 1 
72

輸出範例 1
B-

輸入範例 2 
0

輸出範例 2
X

輸入範例 3 
59

輸出範例 3
F

來源
ccClub Judge
"""

grade = int(input())
if grade >= 90:
  print('A+')
elif grade >= 85 and grade <= 89:
  print('A')
elif grade >= 80 and grade <= 84:
  print('A-')
elif grade >= 77 and grade <= 79:
  print('B+')
elif grade >= 73 and grade <= 76:
  print('B')
elif grade >= 70 and grade <= 72:
  print('B-')
elif grade >= 67 and grade <= 69:
  print('C+')
elif grade >= 63 and grade <= 66:
  print('C')
elif grade >= 60 and grade <= 62:
  print('C-')
elif grade > 0 and grade <= 59:
  print('F')
elif grade == 0:
  print('X')
