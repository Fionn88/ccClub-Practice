"""
[5-1] 阿能點宵夜
Description

此題為填空題。

阿能最近快段考了，每天都在熬夜抱佛腳。但每次讀一讀都會因為肚子餓就直接去睡了，今天覺得進度真的快趕不上了，所以決定點個鹽酥雞，以下為鹽酥雞的菜單：

雞排 65 / 份
鹽酥雞 60 / 份
甜不辣 30 / 份
百頁豆腐 30 / 份
四季豆 35 / 份

Input
輸入為 5 行，分別為雞排、鹽酥雞、甜不辣、百頁豆腐和四季豆點的份數


Output
輸出為 1 行，為阿能宵夜的總金額


Sample Input 1 
1
1
2
1
1

Sample Output 1
250

Hint
請於作答區底線處，填入正確內容，完成題目要求。
作答時請將底線移除，替換成正確內容。
將各項食品的數量乘以單價後加總，即為宵夜的總金額

Source
ccClub Judge
"""

# 輸入各餐點份數
chicken_fillet = int(input())
fried_chicken = int(input())
tempura = int(input())
tofu = int(input())
beans = int(input())

# 計算總金額
# total = ＿＿＿＿
total = chicken_fillet*65+fried_chicken*60+tempura*30+tofu*30+beans*35

# 輸出
print(total)
