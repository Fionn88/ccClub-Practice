"""
凱凱打棒球 II

描述
凱凱是個棒球鐵粉，時常跟著職棒場上的球星巡迴各地球場，不同於多數球迷，凱凱進場看球時不會跟著啦啦隊一起應援，而是緊盯著場上的打擊者，記錄著他們擊球的方向，以歸類每位打擊者的擊球習慣。
在棒球場上，若從捕手（C）、投手（P）、中外野手（CF）的連線切一刀，如下圖所示，可以將球場分成左半邊（SS、3B、LF）和右半邊（RF、2B、1B）。
擊球習慣則大致可以分成拉打（順向攻擊）和推打（反向攻擊）兩種，慣用手為右手的右打者將球打到左半邊（SS、3B、LF）為拉打，打到右半邊（RF、2B、1B）則為推打。
反之，慣用手為左手的左打者將球打到左半邊（SS、3B、LF）為推打，打到右半邊（RF、2B、1B）則為拉打。
凱凱統計了每位球員的擊球狀況，並決定帶回家整理他們的擊球習慣，你能寫一個程式幫他嗎？

輸入
輸入有 2+N 行。
第一行為該打擊者的慣用手，R 代表右手，L 代表左手。
第二行為該打擊者本賽季上場打擊的次數 N。
第 3 ~ N+2 行，每一行為一個字串，代表該次打擊的結果。

輸出
輸出有一行，為一個字串。
請跟據計算結果，分析該打擊者的擊球習慣為拉打或推打。

輸入範例 1
L
6
SS
LF
3B
SS
2B
1B

輸出範例 1
推打

輸入範例 2
R
9
3B
LF
SS
2B
3B
RF
SS
SS
2B

輸出範例 2
拉打

輸入範例 3
R
13
1B
LF
1B
1B
1B
1B
LF
1B
1B
1B
2B
RF
3B

輸出範例 3
推打

提示
1. Sample input 1 中，該名右打者共打了 6 次，其中 4 次為拉打，2 次為推打，因此判斷該打擊者的擊球習慣為拉打。
2. 保證不會有剛好拉打數和推打數相同的情況
"""