"""
反應時間
描述

嘻嘻幼幼班為了測量班上孩子們的反應速度，設計了一個實驗：讓班上的寶寶們排成一列，給一人一個碼表的計次鈕，讓他們依序按下按鈕來記錄時間戳，在根據時間戳之間的差來測驗他們的反應時間。舉例來說，如果寶寶們留下的時間戳分別為：

9 29 49 50

小明 小華 小國 小鐘

那麼，小明的反應時間是 9 ms，小華的反應時間是 29 - 9 = 20 ms，小國的反應時間是 49 - 29 = 20 ms，小鐘的反應時間是 50 - 49 = 1 ms。

現在，給定一列反應時間，請輸出反應最快的寶寶的名字。


輸入
共兩行，

第一行，包含若干整數，中間以空白隔開

第二行，包含若干字串，中間以空白隔開


輸出
共一行，輸出一字串


輸入範例 1 
9 29 49 50
小明 小華 小國 小鐘

輸出範例 1
小鐘

輸入範例 2 
1 8
A B

輸出範例 2
A
"""