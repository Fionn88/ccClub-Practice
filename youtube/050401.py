"""
[5-4] n 倍的數字與字串
Description

輸入為整數 n 及整數 number，請輸出 number 數值上 n 倍的值，與字串上 n 倍的值。

舉例來說，若 n 為 3，number 為 10，則 number 數值上的 n 倍為 10*3=30，字串上的 n 倍為 101010。


Input
輸入為兩行，第一行為整數 n ，第二行為整數 number。


Output
輸出為兩行。

第一行為數字 number 數值上的 n 倍，此輸出的資料型態將為 int。

第二行為數字 number 字串上的 n 倍，此輸出的資料型態將為 string。


Sample Input 1 
3
777

Sample Output 1
2331
777777777

Sample Input 2 
2
9527

Sample Output 2
19054
95279527

Hint
使用 input() 輸入的資料，型態皆為字串，若要當作數字使用請使用 int(字串) 轉換資料型態
第一個輸出，請讓 number 的資料型態為 int，再乘上 n 倍
第二個輸出，請讓 number 的資料型態為 string，再乘上 n 倍

Source
ccClub Judge
"""
n = int(input())
number = input()
# 請接續作答
print(int(number)*n)
print(number*n)

