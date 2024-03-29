"""
轉生到古羅馬文明II

描述
在記賬過程中，城邦裡的人發現小明有自己的一套計數系統，而且看起來還蠻好用的，希望小明可以教他們這套神秘的系統。
請你協助小明教他們如何進行轉換吧！

輸入
輸入有一行，有一串字串代表一個在 1-3999 之間的羅馬數字，由 I, V, X, L, C, D, M 組成

輸出
輸出對應的整數

輸入範例 1
LVIII

輸出範例 1
58
"""

D = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':1000}
s = input()
ans = []
l,r,count = 0,1,0
for i in s:
    ans.append(D.get(i))
while r < len(ans):
    if ans[l] < ans[r]:
        ans[l] = -ans[l]
    l += 1
    r += 1
for i in ans:
    count += i

print(count)
