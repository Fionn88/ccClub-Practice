"""
仔仔鎖金庫I
描述

仔仔是台大學生，在被許多人出租後，真正的發大財了，賺的盆滿缽滿，疑心病重的他不敢把錢放在銀行，於是他把錢都鎖家裡的金庫，但他總覺得他設的密碼不牢固，所以想讓精通密碼學的你幫忙寫出一個加密程式提供他使用。

輸入會有一段明文和一段加密文，全部都是由小寫英文字母組成，請依照以下規則進行加密，

明文和加密文都用字母序數值進行加密，a -> 1、z -> 26
加密公式為：明文[index] + 加密文[index] + 加密文[index + 1] = 密文[index] mod 26
若 index 或 index + 1 ≥ 加密文長度，則用該數取 mod 加密文長度，以結果的 index 進行運算
舉例來說，明文為 bcd ，加密文為 efg ，b 的數值是 2、index 是 0，加密文用來加密的兩個 index 為 0, 1，字母分別為 e、f，所以加密過程為 2(b) + 5(e) + 6(f) = 13(m)，輸出密文 index = 0、字母是 m；再舉例， d 的數值是 4、index 是 2，所以加密文用來加密的兩個 index 為 2, 3，因為 3 ≥ 加密文長度 ，所以 3 取 mod 加密文長度 3 結果為 0，加密過程為 4(d) + 7(g) + 5(e) = 16(p)，其他以此類推。

在這題中，明文長度固定為 3，加密文長度可能為 2、3、4、5。


輸入
共 2 行，

第 1 行，包含 1 個由小寫英文字母組成字串，長度為 3，做為密碼的明文。

第 2 行，包含 1 個由小寫英文字母組成字串，長度可能為 2、3、4、5，做為密碼的加密文。


輸出
共 1 行，輸出密文字串，長度為 3。


輸入範例 1 
abc
cde

輸出範例 1
hkk

輸入範例 2 
acd
bc

輸出範例 2
fhi
"""

characters = input()
password = input()

for index,char in enumerate(characters):
    # 找到該 characters index
    # print(ord(characters[index]) - ord('a') + 1)
    # 找到該密文 index
    # print(ord(password[index % len(password)]) - ord('a') + 1)
    # 找到密文 index+1
    # print(ord(password[(index+1) % len(password)]) - ord('a') + 1)
    print(chr((ord(characters[index]) - ord('a') + 1 + ord(password[index % len(password) ]) - ord('a') + 1 + ord(password[(index+1) % len(password)]) - ord('a') + 1) % 26 + ord('a') - 1),end='')
