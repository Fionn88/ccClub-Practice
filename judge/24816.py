"""
指數的力量

描述
指數的增長指一個函數的增長率與其函數值成比例。常見的指數關係例如著名的摩爾定律，英特爾的執行長提出說預計每 18 個月會將晶片的效能提高一倍。
日常生活中也處處都有指數函數的存在，像是複合利率的計算。
現在我們給定一個整數 x，想請各位判斷他是 2 的 n 次方，如果 n 為整數則回傳 True

輸入
輸入為一個整數

輸出
輸出為一個布林值

輸入範例 1 
4

輸出範例 1
True

輸入範例 2 
10

輸出範例 2
False
"""

n = int(input())
while n >= 1:
    n = n / 2

print(n == 0.5)
