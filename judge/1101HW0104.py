"""
小仔拿魔法石
描述

在雷文克勞的小仔與同伴為了阻止黑巫師拿到魔法石，所以想搶先黑巫師前拿到魔法石，他們從活板門經過層層關卡，最後來到石內卜設下的關卡，這關考的並不是魔法，而是邏輯推理的能力，給定密文和加密文，請你依照提示幫他們反推明文是什麼吧！

輸入會有一段密文和一段加密文，全部都是由 3 個英文字母組成，密文和加密文都用字母序數值進行加密(a -> 1、z -> 26)，請依照以下規則進行解密

先將密文反轉

將同位置的密文和加密文數值相加，如果是偶數，就將密文數值乘加密文數值除以26取餘數，為大寫字母，如果是奇數，就將密文數值除加密文數值取餘，為明文的小寫字母，請注意，餘 0 代表字母 z


輸入
共兩行

第一行，包含一字串，由 3 個英文字母組成，為密文

第二行，包含一字串，由 3 個英文字母組成，為加密文


輸出
共一行，輸出一字串，包含解密後的明文


輸入範例 1 
wed
sjf

輸出範例 1
dee

輸入範例 2 
Wcd
Afs

輸出範例 2
zcU

提示
以 sample 2 為例，

先將密文反轉 -> dcW

再將同位置密文與加密文相加
4(d) + 1 (A) = 5 為奇數
所以 4 % 1 = 0 且要小寫字母 -> z

3(c) + 6(f) = 9 為奇數
所以 3 % 6 = 3 且要小寫字母 -> c

23(W) + 19(s) = 42 為偶數
所以 (23 * 19) % 26 = 21 且要大寫字母 -> U
"""

secret = input()[::-1]
addSecret = input()
ans = []

length = len(secret)
for i in range(length):
    secretKey = ord(secret[i].lower()) - ord('a') + 1
    addSecretKey = ord(addSecret[i].lower()) - ord('a') + 1
    key = secretKey + addSecretKey
    if key % 2 == 0:
        index = (secretKey * addSecretKey) % 26
        if index == 0 or index == 26:
            ans.append('Z')
        else:
            ans.append(chr(index + ord('A') - 1))
    else:
        index = secretKey % addSecretKey
        if index == 0 or index == 26:
            ans.append('z')
        else:
            ans.append(chr(index + ord('a') - 1))

print(''.join(ans))
