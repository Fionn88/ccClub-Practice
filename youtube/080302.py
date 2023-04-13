"""
[8-3] 阿能寫作文II
Description

阿能太常亂敲鍵盤了，不小心敲壞了鍵盤中的幾個鍵。所以在打作文時，常常會有幾個單字打不出來。可以請你幫阿能提前判斷，能夠完整打出幾個英文單字嗎？


Input
輸入為兩行，第一行為一個字串，皆為小寫英文字母；

第二行為阿能作文中會用到的英文單字（單字可能會有大小寫），單字與單字間以空白為間隔。


Output
輸出為一行，為一個整數，請輸出阿能可以打出幾個英文單字。


Sample Input 1 
cs
Stay foolish stay humble

Sample Output 1
1

Sample Input 2 
grop
An apple a day keeps the doctor away

Sample Output 2
5

Source
ccClub Judge
"""
s1 = set(input())
s2 = input().lower().split()
n = 0
for i in s2:
  if s1 & set(i) == set():
    n += 1
print(n)
