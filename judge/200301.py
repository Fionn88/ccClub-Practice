"""
十人十色

描述
在日文當中，「十人十色」代表的含義是每個人都有自己的個性。
換句話說，我們也可以想成每個人都有自己的代表顏色。今天在給定一組人名，以及這組人對應到的顏色的前提之下，請實作一個函式，
用來查找使用者輸入的顏色所對應到的人名，並將這些人名放入串列中作為函式的回傳值，
直到輸入的顏色不是任何人的代表色（不在我們的顏色清單當中）為止。
一個顏色可能對應到的人名不只一個，此時請依照在列表中的順序加入串列。
備註：這題你需要寫一個名為 ten_color 的函式，在當中處理使用者的輸入並進行查找，然後將結果回傳。你不需要自己處理輸出。

輸入
輸入行數不定，每一行皆包含一個字串，為一個顏色，會一直輸入直到該顏色不在列表中

輸出
回傳值為一個串列，串列中的每個元素皆為字串

輸入範例 1
orange
black
grey

輸出範例 1
['Me', 'Sa', 'Ra']

輸入範例 2
yellow
orange
orange
brown

輸出範例 2
['Ai', 'A', 'Ky', 'Me', 'Me']

提示
預設的列表如下（非實際測資）：
names = ['Ni', 'On', 'Sa', 'Ai', 'Ma', 'Fu',
         'Sk', 'Wa', 'Mi', 'I', 'A', 'Mu', 'Me', 
         'Ra', 'Je', 'Ky', 'Mt', 'Ko', 'Ta', 'Mo']
colors = ['red', 'pink', 'black', 'yellow', 
          'blue', 'green', 'purple', 'pink', 
          'blue', 'red', 'yellow', 'green','orange', 
          'black', 'white', 'yellow', 'blue', 'red', 'green', 'purple']
請實作一個名為ten_color(name_lst, color_lst)的函式，預設的參數是姓名以及對應顏色的列表。

來源
ccClub Judge
"""