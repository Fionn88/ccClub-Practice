"""
小小終端機

描述
在終端機裡面，ls指令可以顯示當前的目錄內容，而如果使用ls -l的話，則可以照順序一行行的列出。他的順序是按照第一個字母排序。如果第一個英文字母一樣，我們就比較第二個，依序比較下去。如果兩個詞彙不一樣長，我們會將比較短的排在前面。比方說 b.txt、ab.txt、a.txt ，列出的順序將依序是a.txt、ab.txt、b.txt。請根據此規則，重新整理一串正整數數列。

輸入
輸入為一正整數 n

輸出
輸出為一行，為一串整理過的正整數串列從 1 開始一直到 n（包含 n )

輸入範例 1
15

輸出範例 1
[1, 10, 11, 12, 13, 14, 15, 2, 3, 4, 5, 6, 7, 8, 9]

輸入範例 2
23

輸出範例 2
[1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 21, 22, 23, 3, 4, 5, 6, 7, 8, 9]

提示
正整數 n 介於 1-3000000 之間
請讓時間複雜度維持在 O(n)
"""

n = int(input())
lst = list(map(str,list(range(1, n+1))))
print(list(map(int,sorted(lst))))
