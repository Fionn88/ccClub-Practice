"""
數字組合最大值排序
描述

給定數個整數，請使用數字各位數重新排列以後，可以排出來的最大值來進行排序，並將排序後的串列直接輸出。


輸入
輸入為一行，包含數個整數


輸出
輸出為一行，包含一個串列


輸入範例 1 
709 499 875 796 614

輸出範例 1
['614', '875', '709', '796', '499']

輸入範例 2 
63852 58948 48046 61850 21209 68169 14761

輸出範例 2
['14761', '48046', '61850', '63852', '21209', '68169', '58948']

來源
ccClub Judge
"""

def max_sort_num(str1):
  inp = [s for s in str1]
  inp.sort(reverse = True)
  ans = ''.join(inp)
  return int(ans)
num_lst = [x for x in input().split()]
num_lst.sort(key = max_sort_num)
print(num_lst)
