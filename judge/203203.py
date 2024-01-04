"""
小明在哪裡

描述
小明是個喜歡的全世界跑的孩子，孝順的他每次到一個地方，一定會找一個知名景點拍照，寄一張客製化的明信片回家，讓爸爸媽媽知道他旅行的意義不只是離開家鄉。隨著老爸老媽年紀變大，要在人山人海的地方找出小明也越來越困難，現在，給定一張小明的拍的明信片，你可以幫小明爸媽準確地指出小明位在明信片上的哪個座標嗎？

輸入
輸入有若干行。
若明信片的長寬分別為 h 與 w，則總共有 h 行，每行包含 w 個元素，以空白區隔。
題目不會提供 h 及 w，請在讀取測資時自行判斷。

輸出
輸出有一行，代表小明的位子，格式請依照 (row_index, column_index) 輸出。

輸入範例 1 
小美 小華 小楷
小明 小杜 小周
小云 小雨 小彤

輸出範例 1
(1, 0)

輸入範例 2 
X X X X X X
O O O O O O
| | | | 小明 |
~ ~ ~ ~ ~ ~

輸出範例 2
(2, 4)
"""

x = 0
found = False
while not found:
    try:
        n = input().split()
        if '小明' in n:
            y = 0
            for index,name in enumerate(n):
                if name == '小明':
                    y = index
                    found = True
                    break
        if not found:
            x += 1
    except:
        break

print((x,y))
