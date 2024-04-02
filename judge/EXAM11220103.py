"""
阿偉管監獄 I

描述
阿偉是監獄的典獄長，為了培養犯人友愛動物的心，阿偉特別允許犯人可以養貓。已知監獄裡只有貓、人兩種生物，阿偉會記錄監獄有幾隻貓，幾個人，你可以幫阿偉算看看現在監獄裡有幾顆頭，幾隻腳嗎？

輸入
輸入會用數字記錄現在有幾隻貓和幾個人，順序不定，格式如下：
x people, y cats.
或
x cats, y people.
x, y 為正整數，若只有一種動物，則不會記錄另一種。

輸出
輸出為：
m heads, n legs.
m, n 為正整數。

輸入範例 1
5 people, 3 cats.

輸出範例 1
8 heads, 22 legs.

輸入範例 2
1 cat, 10 people.

輸出範例 2
11 heads, 24 legs.

輸入範例 3
10 people.

輸出範例 3
10 heads, 20 legs.

提示
1. 請遵守單複數變化， people 的單數為 person 。
2. 貓只有一顆頭和四隻腳，犯人只有一顆頭和兩隻腳，監獄裡不存在違反規則的生物。
3. 監獄至少收容了一隻生物。
"""

s = input()
head = 0
leg = 0
if ',' in s:
    s = s.split(',')
    for char in s:
        if 'cat' in char:
            char = char.split()
            leg = leg + int(char[0]) * 4
            head += int(char[0])
        if 'people' in char:
            char = char.split()
            leg = leg + int(char[0]) * 2
            head += int(char[0])
        if 'person' in char:
            leg = leg + 2
            head += 1
else:
    if 'cat' in s:
        char = s.split()
        leg = leg + int(char[0]) * 4
        head += int(char[0])
    if 'people' in s:
        char = s.split()
        leg = leg + int(char[0]) * 2
        head += int(char[0])
    if 'person' in s:
        leg = leg + 2
        head += 1
if head == 1:
    print(f'{head} head, {leg} legs.')
else:
    print(f'{head} heads, {leg} legs.')
