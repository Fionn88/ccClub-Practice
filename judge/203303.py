"""
S型分班

描述
cc 國中要開學了，老師們正為了如何分配新生而煩惱。在開學前，透過開學考，老師們已經幫新生們分成 a - z 等 26 個等第。
然而，根據十二年國教的精神，要盡可能地讓同一個班的同學成分盡量多元。於是老師們打算採行所謂的 S 型分班，而做到這件事之前，得先把學生們按能力 S 形排列才行。
現在，給定學生們的編號及等第，你可以幫 cc 國中的老師輸出一個 S 形排列的序列嗎？

舉例來說，若輸入為：

1 2 3 4 5 6
c c c l u b
代表編號 1、2、3 的學生被分為 c 等第，編號 4 的學生為 l 等第，以此類推。
我們將等第從最小排到最大是 b c l u，因此輸出 6 1 4 5，其中 1 是 c 等第中第一個出現的學生編號。
接著，再從等第最大排到最小，但此時只剩下 c，所以輸出第二個出現的 c ，其編號是 2。
同理，最後輸出 3。
因此完整的 S 行排列為 6 1 4 5 2 3。

輸入
輸入為兩行。
第一行包含 n 個數字，以空白分隔。
第二行包含 n 個小寫字母，以空白分隔。

輸出
輸出為一行，包含 n 個數字，為經過 S 形排列的序列。

輸入範例 1 
4 3 2 1
b b a c

輸出範例 1
2 4 1 3

輸入範例 2 
1 2 3 4 5 6
c c c l u b

輸出範例 2
6 1 4 5 2 3

輸入範例 3
8 7 6 5 4 3 2 1 9 10 11 12
a a a b b b c c c d d d

輸出範例 3
8 5 2 10 11 1 4 7 6 3 9 12

輸入範例 4
3 1 2 4 5 6 7 8
c c a f f z a c

輸出範例 4
2 3 4 6 5 1 7 8
"""

# ======================== 解法一 =======================
# student = input().split()
# grade = input().split()
# lst = [[k,v] for k, v in zip(student, grade)]

# ans = []
# def sort_up(l):
#     sorted_up_lst = sorted(l, reverse = False, key = lambda item:item[1])
#     return sorted_up_lst

# def sort_down(l):
#     sorted_down_lst = sorted(l, reverse = True, key = lambda item:item[1])
#     return sorted_down_lst

# def find_duplicate_item(l, temp_l):
#     for i in range(len(l)-1):
#         try:
#             while ord(l[i][1]) ==  ord(l[i+1][1]):
#                 temp_l.append(l.pop(i+1))
#         except:
#             continue
#     return temp_l

# def append_to_ans(l):
#     for item in l:
#         ans.append(item)
#     l.clear()
#     return(l)

# lst_sort_up = sort_up(lst)
# lst_sort_down = []
# while(len(lst_sort_up) != 0 or len(lst_sort_down) != 0):
#     lst_sort_down = sort_down(find_duplicate_item(lst_sort_up,lst_sort_down))
#     append_to_ans(lst_sort_up)
#     lst_sort_up = sort_up(find_duplicate_item(lst_sort_down,lst_sort_up))
#     append_to_ans(lst_sort_down)

# for answer in ans:
#     print(answer[0], end=" ")


# ======================== 解法二 =======================
from collections import defaultdict

student_dict = defaultdict(list)
ans_list = []

id_lst = [_ for _ in input().split()]
grade_lst = [_ for _ in input().split()]

for student_id,grade in zip(id_lst,grade_lst):
    student_dict[grade].append(student_id)

reverse = False
while len(student_dict) > 0:
    order = sorted(student_dict.keys(), reverse=reverse)
    for grade in order:
        ans_list.append(student_dict[grade].pop(0))
        if len(student_dict[grade]) == 0:
            del student_dict[grade]

    reverse = not reverse

print(' '.join(ans_list))
