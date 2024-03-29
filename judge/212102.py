"""
直角三角形

描述
我們知道，當三角形的三個邊 a、b、c 符合邊長 c^2 = a^2 + b^2，那麼這三個邊可以組成一個 ab 夾角為直角的三角形。

輸入
輸入為兩行，第一行包含一個正整數 c。第二行包含正整數 y 和正整數 z。請判斷範圍在 y 跟 z 之間（包含 y 和 z，y 可能小於或大於 z），是否存在兩個整數 a, b 滿足 c^2 = a^2 + b^2。(即 c 為三角形長邊)

輸出
若存在則輸出 True，不存在輸出 False

輸入範例 1 
13
5 12

輸出範例 1
True

輸入範例 2 
3
5 7

輸出範例 2
False
"""

c = int(input())
other = list(map(int,input().split()))
side = c * c

l = min(other)
r = max(other)
flag = False
while l <= r:
    if l * l + r * r > side:
        r -= 1
    elif l * l + r * r < side:
        l += 1
    else:
        flag = True
        break

print(flag)
