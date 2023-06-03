"""
學習歷程
描述

小明要出國念書了，最近他在整理自己的備審文件，偶然看到自己的大學學習歷程，心中也是一陣感慨，想著自己在台大學習歷程，也是曲曲折折。
因此，他決定整理整理自己的修課歷程，讓以後的學弟妹們可以參考。為了保有學習的脈絡，他決定除了列出他修了哪些課之外，更要列出修這些課之前最好修過那些課比較好，這樣比較負責任。學弟妹們查課的時候除了查到該門課，還可以查到修該門課之前要依序學過那些課比較好。

說明：
以範例一為例，前四行每一行的第一個名詞是該課的課名，空格以後是修習該課需要的先備知識。如果該門課是基礎學科，也就是沒有先備知識的話，則該行只會有一個字串。最後一行則是學弟妹好奇的課。
由於學習 DataScience 要先學過 calculas 和 stats 比較好，而要學過 calculas 要先學過 counting 比較好，因此依序輸出 counting calculas stats DataScience。
同一個層次的課程按字首字母順序排列，若相同則繼續往下比較，以此類推。請輸出學弟妹所感興趣的課的學習歷程。


輸入
輸入為五行。
前四行每一行的第一個名詞是該課的課名，空格以後是修習該課需要的先備知識。
最後一行則是學弟妹好奇的課。


輸出
輸出為一行，以空白區隔，為推薦的學習歷程。


輸入範例 1 
DataScience calculas stats
calculas counting
stats
counting
DataScience

輸出範例 1
counting calculas stats DataScience

輸入範例 2
a b c
b e
c d
f
a

輸出範例 2
d e b c a
"""

# ============================== Keep Trying =========================
def get_learning_path(course, prerequisites):
    
    if course not in prerequisites:
        return [course]
    
    path = []
    for prerequisite in prerequisites[course]:
        sub_path = get_learning_path(prerequisite, prerequisites)
        path += sub_path
    
    return path + [course]

# 讀取輸入
prerequisites = {}
for _ in range(4):
    course, *prereqs = input().split()
    prerequisites[course] = prereqs

target_course = input().strip()

# 取得學習歷程和遞迴次數
learning_path = get_learning_path(target_course, prerequisites)

sort_full,ans = [],[]
for key,value in reversed(prerequisites.items()):
    if not value:
        sort_full.append(key)
    else:
        sort_full.extend(value)
if not prerequisites[target_course]:
    pass
else:
    sort_full.append(target_course)



# print(sort_full,learning_path)
for sort_full_value in sort_full:
    if sort_full_value in learning_path:
        ans.append(sort_full_value)
# 輸出結果
print(' '.join(ans))
