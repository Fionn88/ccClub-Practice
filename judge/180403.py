"""
密碼強度
Description

定義密碼的強度為： 字串長度 * (大寫字母個數*2 + 小寫字母個數*1.5 + 數字字母個數) + 其它字元個數^2 

舉例來說：

1. 密碼 ccClub2018 的密碼強度為 10 * (1*2 + 5*1.5 + 4) + 0^2 = 135，
2. 密碼 ccClub@2018_09_10 的密碼強度為 17 * (1*2 + 5*1.5 + 8) + 3^2 =306.5


給定若干個密碼，依照其密碼強度由高至低排序後輸出（若密碼強度相同，則依照給定的順序輸出）。


Input
輸入有 n + 1 行，第一行為正整數 n，代表總共有 n 組密碼。

接下來 n 行分別為 n 組密碼。


Output
輸出有 n 行，為依照密碼強度排序後的結果。


輸入範例 1 
2
ccClub2018
ccClub@2018_09_10

輸出範例 1
ccClub@2018_09_10
ccClub2018

輸入範例 2 
5
g34l[v4
Xm@7[y8iD7g]G()Dez
604uRzmBRy)(1L
bGYop/86C/fW2T
Di(0\_g7ebK5PXvY{

輸出範例 2
Xm@7[y8iD7g]G()Dez
Di(0\_g7ebK5PXvY{
bGYop/86C/fW2T
604uRzmBRy)(1L
g34l[v4

來源
ccClub Judge
"""
def string_password(s):
  upper,lower,digit,other = 0,0,0,0
  for i in s:
    if i.isupper():
      upper += 1
    elif i.islower():
      lower += 1
    elif i.isdigit():
      digit += 1
    else:
      other += 1
  return len(s)*(upper*2 + lower*1.5 + digit)+other**2

n = int(input())
s = [i for i in range(n)]
print(string_password(s))
