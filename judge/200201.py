"""
小明來數數
描述

小明是一個剛學到等差數列的國中生，最近老師出了一個很麻煩的作業，要求小明在給定數列的首項、最大上限、以及差以後，從首項開始列出這個數列的每一項數值，直到下一項大於或等於最大上限為止（意即最後一項必定小於最大上限），並且同時計算出等差數列的和。
舉例來說，如果給定的數字是：1 10 2，1 是這個數列的首項、10 是最大上限、2 則是差。
要得到的輸出則如下：

1 3 5 7 9
25

輸入
輸入為一行，包含三個整數，以空白分隔，分別為等差數列的首項、最大上限、以及差。


輸出
輸出為兩行，第一行為該等差數列，包含數個整數，以空白分隔；第二行包含一個整數，為該等差數列的和。


輸入範例 1 
1 10 2

輸出範例 1
1 3 5 7 9
25

輸入範例 2 
55 77 3

輸出範例 2
55 58 61 64 67 70 73 76
524

來源
ccClub Judge
"""