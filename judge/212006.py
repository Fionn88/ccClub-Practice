"""
最長集合

描述
====
請至 Judge 上查看題目
====

輸入
輸入為一組正整數，以「,」分隔。


輸出
輸出為一個正整數，表示所有起始索引中能找出的最長數字集合之長度


輸入範例 1 
1,3,2,4,0

輸出範例 1
4

輸入範例 2 
7,1,2,5,4,6,3

輸出範例 2
3
"""

lst = [int(i) for i in input().split(",")]
max_len = 0
for i in lst:
    index_set = {i}
    while True:
        try:
            i = lst[i]
        except:
            break
        else:
            if i in index_set:
                break
            else:
                index_set.add(i)
    max_len = max(len(index_set),max_len)
print(max_len)
