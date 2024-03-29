"""
答案產生器

描述
因為連續幾天都在玩拼圖，導致小丹沒空寫作業，走投無路的他只好向朋友們要來作業解答。然而小丹的朋友們不是很可靠，大家回傳的答案有些微的出入，使他非常苦惱。給定朋友們的作業，你能幫小丹找出每題最有可能的正確答案嗎？
舉例來說：
這次作業有兩題，小丹的朋友們分別回傳了 "AA", "AB", "CA" 三份答案。第一題有兩個朋友答 A, 只有一個朋友答 C，因此正確答案是 A 的可能性較高。同理，第二題答案是 A 的可能性較高。輸出 "AA" 作為答案。
如果不同答案的出現次數相同，則輸出較早出現的答案。以另一個例子來說，如果作業只有一題，五個朋友分別回傳 "A", "C", "B", "C", "B"，此時雖然 C 和 B 都出現兩次，但因 C 較早出現，因此輸出的答案為 "C"。

輸入
輸入有 n+1 行。
第一行包含兩個正整數，為 n 和 m，分別代表小丹的朋友數及作業的題目數。
接下來 n 行，每行包含 m 個大寫英文字母，代表該位朋友回傳的答案。

輸出
輸出有一行，包含 m 個大寫英文字母，代表各題最可能的答案。


輸入範例 1
4 6
ABBCDB
ABCBDB
ACCCDB
ABCCCB

輸出範例 1
ABCCDB

輸入範例 2
5 2
AB
AC
AA
BA
BC

輸出範例 2
AC
"""

n, m = [int(i) for i in input().split()]
ans = [input() for _ in range(n)]
ans_trans = ['' for _ in range(m)]

for j in range(m):
    for i in range(n):
        ans_trans[j] += ans[i][j]

for i in range(len(ans_trans)):
    bag, counter = [], []
    for j in ans_trans[i]:
        if j not in bag:
            bag.append(j)
            counter.append([ans_trans[i].count(j), j])
        
        else:
            continue

    counter = sorted(counter, reverse=True, key=lambda x: x[0])
    ans_trans[i] = counter[0][1]

print(''.join(ans_trans))
