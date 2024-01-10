"""
小仔整理書架

描述
小仔想要重新編排書架上書的擺放位置和清除書架的隔板，他會從最內層的隔板開始清除，每當清除一個隔板他會反轉隔板內書的擺放位置，持續操作直到沒有隔板後，輸出書的擺放順序。書架的上下隔板分別為”\”, “/”，所有的書以字母表示。

輸入
共一行，包含一字串，代表現在書架上的情況(以 "\" "/" 代表成對的隔板)

輸出
共一行，包含一字串，代表移除隔板且重新整理後，書的擺放順序

輸入範例 1
\asd\qwe/rt/

輸出範例 1
trqwedsa

輸入範例 2
qwer\sdf\gghj/xbb/

輸出範例 2
qwerbbxgghjfds

提示
sample 1
\asd\qwe/rt/ -> \asdewqrt/ -> trqwedsa
"""

books = [i for i in input()]
while '\\' in books:
    start, end = 0, 0
    for i in range(len(books)):
        if books[i] == '\\':
            start = i
        elif books[i] == '/' and i > start:
            end = i
            break

    books[start+1:end] = books[end-1:start:-1]
    books.pop(end) 
    books.pop(start)

print(''.join(books))
