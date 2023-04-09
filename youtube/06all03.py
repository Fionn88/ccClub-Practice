"""
[6-綜合] 小明的牛排館
Description

想開牛排館的小明，正在準備他的菜單，你可以幫幫他嗎？

小明想用一個名為 menu 的串列，把所有餐點存起來，目前 menu 中已經有了 "bread" 和 "salad" 兩樣食物。

小明希望有豐富的前菜，請幫他在 "bread" 後加入 "soup"。
接著將 "steak" 放在 menu 串列的最後。
再將 dessert 串列中的所有食物都放進 menu 串列的最後。
小明仔細想想覺得 "chocolate" 不適合放在菜單裡，請幫他移除。

Input
此題無輸入。


Output
輸出為一個串列，為小明牛排館的菜單。


Sample Input 1 

 
Sample Output 1
['bread', 'soup', 'salad', 'steak', 'cake']

Hint
題目中的第三步驟是要將 dessert 串列中的兩個物件放進 menu 中，而非整個 dessert 串列。
完成所有步驟後，menu 串列中應該會有 5 個物件。

Source
ccClub Judge
"""
menu = ["bread", "salad"]
dessert = ["cake", "chocolate"]

# your code here

print(menu)
