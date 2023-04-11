"""
[6-綜合] 複製串列
Description

給定一個串列 lst = ['a', 'b', 'c', 'd']。

請複製串列 lst 並命名為 lst_copy，並將 lst 中的第一個及最後一個物件依序加入 lst_copy 的最後方。

最後輸出為兩行，第一行為原串列 lst，第二行為經過上述處理後的串列 lst_copy。


Input
此題無輸入。


Output
輸出為兩個串列。


Sample Input 1 

 
Sample Output 1
['a', 'b', 'c', 'd']
['a', 'b', 'c', 'd', 'a', 'd']

Hint
請注意"複製串列"與"指定至同個串列"的差別，複製串列應使用 lst_copy = lst[:]。
將物件加入串列時，請使用 lst.append(element)。

Source
ccClub Judge
"""
lst = ['a', 'b', 'c', 'd']
lst_copy = lst_copy = lst[:]
# your code here
lst_copy.append(lst[0])
lst_copy.append(lst[-1])

print(lst)
print(lst_copy)
