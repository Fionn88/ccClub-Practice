"""
3-4：自己回文
Description

輸入一個字串 s ，輸出為 s 自己串接 s 的倒序，使其成為一個回文字串。


Input
輸入為一行，包含一個字串s


Output
輸出為一行，內容為s的回文字串


Sample Input 1 
Hello

Sample Output 1
HelloolleH

Sample Input 2 
123

Sample Output 2
123321

Source
ccClub Judge
"""

s = input()
print(s,s[::-1], sep="")
