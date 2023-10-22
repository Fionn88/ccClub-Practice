"""
幾A幾B
描述

阿緯跟朋友在玩猜數字的遊戲，進行方式是由謎底方先設定好數字組合，另一方猜；每猜一次，謎底方就要根據對方猜的數字給出 "xAyB" 的提示。其中 x 表位置正確的數的個數， y 表數字正確但位置不對的數的個數。

現在輪到阿緯當謎底方了，但阿緯覺得每次都要一個一個慢慢對很浪費時間，可以請你幫阿緯解決這個問題嗎？


輸入
輸入為兩行，第一行為阿緯的謎底，第二行為同學猜的數字


輸出
請根據遊戲規則，以 "xAyB" 的格式輸出正確的提示內容


輸入範例 1 
1807
7810

輸出範例 1
1A3B

輸入範例 2 
1
0

輸出範例 2
0A0B

輸入範例 3 
1123
0111

輸出範例 3
1A1B
"""

from collections import Counter
s1 = input()
s2 = input()
length = len(s1)
Acount = 0
Bcount = 0
answer_counter = Counter(s1)
guess_counter = Counter(s2)

for i,j in zip(s1,s2):
  if i == j:
    Acount += 1
Bcount = sum((answer_counter & guess_counter).values()) - Acount

print(Acount,'A',Bcount,'B',sep='')
