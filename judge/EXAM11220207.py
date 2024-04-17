"""
阿偉蓋金字塔

描述
阿偉是古埃及的小苦工，法老要他從頭開始蓋金字塔，在有限的磚塊下，阿偉需要把金字塔蓋越高越好。
你能幫阿偉計算金字塔層數，並幫他完成這個建築工程嗎？

輸入
一個正整數，表示阿偉有的磚塊數量。

輸出
輸出分為兩組
前 n 行回傳金字塔的造型，n為塔高。
第 n+1 行回傳剩餘的磚塊數，若無剩餘磚塊則不回傳。
B為磚塊的代號，金字塔的最高層將在最右側置放一塊磚塊，之後每向下一層加一塊磚塊，沒有磚塊的地方則以空白紀錄。詳見Sample。

輸入範例 1
11

輸出範例 1
   B
  BB
 BBB
BBBB
1

輸入範例 2
15

輸出範例 2
    B
   BB
  BBB
 BBBB
BBBBB
"""

def right_triangle(n):
	for i in range(1, n + 1):
		print(f"{' ' * (n - i)}{'B' * i}")

Sn = int(input())

high = (-1 + (1 + 8 * Sn) ** 0.5) / 2
high = int(high)
sum = high * (high + 1) / 2
right_triangle(high)
remainder = int(Sn - sum)
if remainder != 0:
	print(remainder)
