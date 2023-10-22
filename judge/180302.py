"""
數字串列處理器
描述

在之前的練習中，我們實作過「奇偶個數差(odd_even_count_sub)」、「冠亞軍分數差(top2_max_sub)」和「最大奇偶相差(max_odd_even_sub)」。

現在，我們需要實作一個數字串列處理器，這個處理器擁有以上三個功能。

讓使用者輸入若干個數以及需要的功能，接著輸出對應的結果。



備註：

在這題，你只需要完成odd_even_count_sub、top2_max_sub、max_odd_even_sub這三個函式，不需要自行處理 input()。


輸入
函式有一個參數：

lst：型態為 list，串列中每個元素的型態為 int

輸出
函式有一個回傳值：

型態為 int

輸入範例 1 
1 2 3
odd_even_count_sub

輸出範例 1
1

輸入範例 2 
1 3 9 7 11
top2_max_sub

輸出範例 2
2

輸入範例 3 
1 2 7 5 6 3
max_odd_even_sub

輸出範例 3
1

提示
請直接複製以下內容，並實作這三個函式，並將答案使用return回傳

def odd_even_count_sub(lst):
    #start your code here for odd_even_count_sub

    return ans

def top2_max_sub(lst):
    #start your code here for top2_max_sub

    return ans

def max_odd_even_sub(lst):
    #start your code here for max_odd_even_sub

    return ans

來源
ccClub Judge
"""

def odd_even_count_sub(lst):
    #start your code here for odd_even_count_sub
    even = 0
    odd = 0
    for i in lst:
      if i % 2 == 0:
        even += 1
      else:
        odd += 1
    return abs(even-odd)

def top2_max_sub(lst):
    #start your code here for top2_max_sub
    sortS = sorted(lst)
    
    return abs(sortS[-1]-sortS[-2])

def max_odd_even_sub(lst):
    #start your code here for max_odd_even_sub
    maxOdd = 0
    maxEven = 0
    for i in lst:
      if i % 2 == 0:
        if maxEven < i:
          maxEven = i
      else:
        if maxOdd < i:
          maxOdd = i

    return abs(maxEven-maxOdd)
