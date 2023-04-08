"""
[5-2] 認真的阿緯
Description

此題為填空題。

阿緯是個認真的高中生，每天都會認真準備課後的作業與考試。

如果作業份數超過 3 份或明天有很多小考的話，阿緯就得 11 點後才能睡覺了。


Input
輸入為 2 行，

第一行為一個整數，代表作業份數

第二行為一個字串， "OMG! 明天有好多考試!" 或 "開心! 明天沒有小考!"


Output
輸出為 1 行，如果阿緯得 11 點後才能睡輸出 True，可以 11 點前睡的話輸出 False


Sample Input 1 
1
OMG! 明天有好多考試!

Sample Output 1
True

Sample Input 2 
2
開心! 明天沒有小考!

Sample Output 2
False

Hint
請於作答區底線處，填入正確內容，完成題目要求。
作答時請將底線移除，替換成正確內容。
請運用比較運算子判斷作業數量是否大於3，以及明天是否有小考
請使用邏輯運算子判斷，以上兩個條件是否有任一個達成

Source
ccClub Judge
"""
# 輸入
homeworks = int(input())
quizzes = input()

# 輸出
# print(homeworks __ 3 ___ quizzes ___ "開心! 明天沒有小考!")
print(homeworks > 3 or quizzes != "開心! 明天沒有小考!")
