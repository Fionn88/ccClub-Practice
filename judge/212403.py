"""
小仔解密碼

描述
小仔跟著魯夫一行人終於到達偉大航道的盡頭，眼前就只差一道門就能得到 ONE PIECE，但門的把手上有個四位數字的密碼鎖，而門上有一段由英文寫的文章，門旁邊擺放刻著古文字的石碑，通曉歷史本文的羅賓，立刻就知道門上的文章就是解出密碼的關鍵，只要依照石碑上的指示就能解出密碼，請你依照指示寫一段程式幫幫他們吧。
題目給定一篇由全英文組成的文章，請先將文章中全部的標點符號去除，再將文章中所有單字重新排序，排序規則為每個單字的奇數位依照 ASCII code 編碼相加後，取數字的後兩碼由小排到大，如果數值相同，就以偶數位依照 ASCII code 編碼相加，取數字的後兩碼由大排到小。完成排序後，取倒數第三個單字，把單字每個位元依照字母序每個相乘(a -> 1, z->26, 大小寫皆相同)，取得出來的數字的前四碼(不足四位，就在數字前面補 0)，即為大門的密碼。

輸入
共一行，給定一字串(單字數大於 3 )

輸出
輸出包含一整數

輸入範例 1
Lead him, I pray, not in the path of ease and comfort.

輸出範例 1
0240

輸入範例 2
I have a dream that my four little children will one day live in a nation where they will not be judged by the color of their skin, but by the content of their character. I have a dream today

輸出範例 2
0050
"""