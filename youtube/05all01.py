"""
[5-綜合] 乘法運算
Description

輸入一個乘法算式，其中兩個數皆為兩位數，且乘號兩邊各保留一個空格，請輸出計算後的結果。


Input
輸入為 1 行，為一個乘法算式，算式的格式如題目敘述。


Output
輸出為 1 行，為乘法運算後的結果。


Sample Input 1 
12 * 12

Sample Output 1
144

Sample Input 2 
94 * 87

Sample Output 2
8178

Hint
可以先用字串分割出兩個兩位數，經過型態轉換後再計算結果。

Source
ccClub Judge
"""
s = input().split()
print(int(s[0]) * int(s[2]))