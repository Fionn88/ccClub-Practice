"""
出題目
描述

作為一個小學老師，小美每周都要出練習題給班上同學練習，考考他們的小腦袋，但是出題目有個很微妙的點是需要自己先驗算過答案，不然到時候解不出來或是解出來解不合理那就慘惹。這一周的回家作業是經典的二元一次方程式問題：

東尼史塔克有很多套鋼鐵裝，每套鋼鐵裝有 8 個備用電池
布魯斯韋恩有很多套蝙蝠裝，每套蝙蝠裝有 4 個備用電池
請問給定他們共有 16 套服裝，40 顆備用電池，鋼鐵人跟蝙蝠俠各有幾套裝備？

像這樣子的問題就會出事，因為不會有非正整數或 0 的裝備數量。那這樣的話小美就會被小朋友們恥笑說，老師你懂不懂超級英雄阿？
為了避免這樣的情形出現，給定鋼鐵裝、蝙蝠裝的額定備用電池數以及兩人共有幾套服裝跟電池，你可以幫小美設計一個可以驗算這題目可不可以出的程式嗎？
鋼鐵人與蝙蝠俠的裝備數量都必須為正整數，也就是若驗算出的答案為非正整數、0、無解、無限多解，該題目都不合格，輸出 False。


輸入
輸入有四行，每行一個包含一個數字，依序為鋼鐵裝的額定備用電池數、蝙蝠裝的額定備用電池數、兩人服裝套數總和、兩人備用電池數總和。


輸出
輸出為一行。
若題目合格，輸出 True，反之則輸出 False。


輸入範例 1 
4
8
16
120

輸出範例 1
True

輸入範例 2 
4
8
16
40

輸出範例 2
False
"""