"""
合法數獨

描述
小明是個數獨愛好者，常常喜歡在格子裡亂填一些數字，然後再自己解出來。但每次填完數字，又要再花時間檢查是不是一個合法的數獨問題很麻煩，請你幫小明用程式解決這個問題吧！
檢查9 * 9數獨是否合法的規則有下面三點：
每一行只能包含數字 1～9，且不能重複
每一列只能包含數字 1～9，且不能重複
每一宮（粗黑線圍起來3 * 3的區域）也只能包含數字 1～9，且不能重複

輸入
輸入有 9 行，每行都有 9 個數字，數字間以逗號作為間隔。數字 "1" ~ "9" 代表問題對應位置裡的數字，"0" 代表該格子沒有填任何數字

輸出
輸出一個布林值，是個合法的數獨問題輸出 True，反之則輸出 False

輸入範例 1
0,0,0,1,2,0,0,5,0
0,3,0,0,5,0,4,0,0
0,0,0,4,0,7,2,0,1
1,0,0,3,0,0,0,0,0
7,0,2,0,0,0,3,0,6
0,0,0,0,0,6,0,0,5
8,0,4,6,0,5,0,0,0
0,0,3,0,8,0,0,1,0
0,5,0,0,4,1,0,0,0

輸出範例 1
True

輸入範例 2
8,3,0,0,7,0,0,0,0
6,0,0,1,9,5,0,0,0
0,9,8,0,0,0,0,6,0
8,0,0,0,6,0,0,0,3
4,0,0,8,0,3,0,0,1
7,0,0,0,2,0,0,0,6
0,6,0,0,0,0,2,8,0
0,0,0,4,1,9,0,0,5
0,0,0,0,8,0,0,7,9

輸出範例 2
False

提示
Sample Input 1 就是上面示意圖的輸入喔！
"""

def isValidSudoku(board):
        # Check for duplicate numbers in the vertical
        for row in board:
            dup = {x for x in row if row.count(x) > 1}
            if '.' in dup:
                dup.remove('.')
            if dup:
                return False 

        # Check for duplicate numbers in the horizontal
        for col in range(9):
            column = [board[row][col] for row in range(9)]
            dup = {x for x in column if column.count(x) > 1}
            if '.' in dup:
                dup.remove('.')
            if dup:
                return False 

        # Check for duplicate numbers in the 3x3 grid
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                dup = {x for x in square if square.count(x) > 1}
                if '.' in dup:
                    dup.remove('.')
                if dup:
                    return False 
        return True

lst = []
for _ in range(9):
    lst_inner = input().replace("0",".").split(",")
    lst.append(lst_inner)

print(isValidSudoku(lst))
