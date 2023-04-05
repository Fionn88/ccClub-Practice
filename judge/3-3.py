"""
3-3：重複輸出
Description

輸入兩個數字 a 和 b，輸出有兩行，請輸出 b 個 a 以及 a 個 b


Input
輸入有兩行，分別為兩個數字


Output
輸入有兩行，各包含一串數字，分別為b 個 a 以及 a 個 b。


Sample Input 1 
5
6

Sample Output 1
555555
66666

Sample Input 2 
8
12

Sample Output 2
888888888888
1212121212121212

Source
ccClub Judge
"""
a = int(input())
b = int(input())
print(str(a)*b)
print(str(b)*a)