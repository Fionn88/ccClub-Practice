"""
綜合2-2：字母加權排序

描述
定義一個字串的加權值算法為，將字串中每個字元，依照 a~z 的加權分數（大小寫視為相同）分別為 1~26 進行加權。
舉例來說：banana = 2 + 1 + 14 + 1 + 14 + 1 = 33。
給一個內容皆為字串的 list ，依照每個字串的加權值由小到大排列（若加權值相同，則依照原串列的順序即可）

輸入
輸入為一行，包含數個字串，以空白分隔

輸出
輸出為一行，包含一個經過排序後的串列


輸入範例 1 
Egg ccClub baNaNa

輸出範例 1
['Egg', 'baNaNa', ‘ccClub']

輸入範例 2 
a AA b !@#$%^&*()_+

輸出範例 2
['!@#$%^&*()_+', 'a', 'AA', ‘b']

來源
ccClub Judge
"""

weight_dic = {} #建立字母加權字典
c1 = 1
for c in range(97,123):
    weight_dic[chr(c)] = c1
    c1 += 1

s = input().split()

# 計算每個字串的加權分數
weight_sum = {}
for s1 in s:
    weight_i = 0 
    for i in range(len(s1)):
        s2 = s1[i].lower()
        if ord(s2) in range(97,123):
            weight_i += weight_dic[s2]
        else:
            weight_i += 0 
    weight_sum[s1] = weight_i 

# 根據加權分數排序
s_dict = sorted(weight_sum.items(), key = lambda d: d[1])

# 將排序好的字串依照出現次數重新排序
s_list = []
count_dict = {}
for k in s_dict:
    if k[0] not in count_dict:
        count_dict[k[0]] = s.count(k[0])
for k in sorted(count_dict.items(), key=lambda x: x[1], reverse=True):
    s_list.extend([k[0]] * k[1])
    
print(s_list)
