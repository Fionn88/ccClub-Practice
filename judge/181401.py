"""
信箱名建議

描述
定義一個合法的信箱名為一串數字和英文字母混合的字串，後面接上 @ 和 domain name。
舉例來說：

kevin810214@ccclub.io 是個合法的信箱
而
kevin-81.02.14+ccclub@ccclub.io 是一個不合法的信箱。
請你寫一個程式，判斷用戶輸入的信箱，若信箱名包含+、-、.，則移除，並給予他一個更正過後的信箱名建議。

輸入
輸入有一行，包行一個字串。

輸出
輸出為一行，包含一個字串，即更正後的信箱。

輸入範例 1 
b01902137-wayne-huang@ntu.edu.tw

輸出範例 1
b01902137waynehuang@ntu.edu.tw

輸入範例 2 
kevin-81.02.14+ccclub@ccclub.io 

輸出範例 2
kevin810214ccclub@ccclub.io 

來源
ccClub Judge
"""

import re
s = input().split('@')
print(re.sub("[+-.]",'', s[0]),'@',s[1],sep='')
