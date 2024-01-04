"""
字母接龍

描述
給定 20 個字母對應關係，如：A => V，代表字母 A 對應到字母 V。
請順著對應關係，找出由給定字母開始的循環。
詳細說明請見輸入/輸出格式。

輸入
輸入有 21 行。
前 20 行是一個字串，包含兩個字母，字母間用空格分開，代表著字母間的對應關係。
第 21 行為一個字串，包含一個字母，代表起始的字母。

輸出
輸出有一行，包含若干個字母，字母間用空格分割。
代表著從起始字母開始，依照對應關係會遇到的所有字母。


輸入範例 1
L S
G C
T P
E Y
I D
P I
Y T
C J
A R
O Z
F Q
J F
B V
D U
Q B
S A
U O
R E
V G
Z L
Q

輸出範例 1
Q B V G C J F

輸入範例 2
C O
D T
G N
M P
N I
W E
Y C
F F
I S
L X
A K
P V
V B
E M
O G
T D
S L
K A
B W
X Y
I

輸出範例 2
I S L X Y C O G N

提示
sample input 1 從 Q 開始，Q 會對到 B，B 會對到 V，V 會對到 G，G 會對到 C，C 會對到 J，J 會對到 F，F 會對到 Q。
因為回到起始字母 Q 了，我們可以知道從 Q 開始的接龍為 Q B V G C J F

來源
ccClub Judge
"""

D = {}
answer = []
for i in range(20):
    n = input().split()
    D[n[0]] = n[1]
query = input()
answer.append(query)
original = query
while True:
    getAnswer = D.get(query)
    if getAnswer == original:
        break
    answer.append(getAnswer)
    query = getAnswer
print(' '.join(answer))
