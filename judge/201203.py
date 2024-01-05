"""
小明找大腿

描述
剛開學的時候，課程往往會要求同學先分組方便以後進行活動，但小明沒有朋友，他只好使用大腿雷達來尋找大腿。大腿雷達可以感知到附近大腿的座標以及戰力，所以首先小明會知道附近有 n 個大腿，接著會知道大腿們的 [名字] [x座標] [y座標] [戰力]。小明想要從厲害的大腿開始找起，但是在教室裡大腿距離小明的位置也很重要，所以在他心目中大腿的排序方式如下：
先用戰力 / (距離^2)這個公式得出的數值來對大腿們進行排序，距離的平方算法是(x座標差)^2 + (y座標差)^2，以小明所在的位置為原點 (0,0)
如果有兩個大腿的 1. 數值相同，先選擇戰力高的
可以保證大腿們的戰力都不同，請寫一個程式幫小明根據大腿們的距離跟戰力進行排序，讓小明可以安心地依賴大腿們歐趴。

輸入
輸入包含 n+1 行，第一行為數字n，代表附近的大腿個數
以下 n 行分成四個部分，包含一個字串以及三個整數，以空白分開，其格式為 [名字] [x座標] [y座標] [戰力]

輸出
輸出包含 n 行，各包含一個字串（名字），為排序大腿以後的結果，優先度高的在前。

輸入範例 1
3
小習 3 4 20
小川 4 3 25
小英 8 6 100

輸出範例 1
小英
小川
小習

輸入範例 2 
5
1 3 8 127
2 6 2 220
3 2 4 817
4 1 8 169
5 1 7 712

輸出範例 2
3
5
2
4
1

提示
參考資料 (複數條件排序):
https://docs.python.org/3/howto/sorting.html
https://medium.com/ccclub/ccclub-python-for-beginners-tutorial-f3148ebb33a4

來源
ccClub Judge
"""

# ========================================== 此解法花了 24ms ====================================
# n = int(input())
# temp = {}
# ans = {}
# ansReal = {}
# for i in range(n):
#   s = input().split()
  
#   distance = int(s[1]) ** 2 + int(s[2]) ** 2
#   war = int(s[3]) / distance
#   ans[s[0]] = war
#   temp[s[0]] = int(s[3])

# sorted_temp = sorted(temp.items(), key=lambda x:x[1],reverse=True)

# for i in range(n):
#   anGet = ans.get(list(dict(sorted_temp))[i])
#   ansReal[list(dict(sorted_temp))[i]] = anGet


# sorted_ansReal = sorted(ansReal.items(), key=lambda x:x[1],reverse=True)
  
# for i in list(dict(sorted_ansReal)):
#   print(i)

# ========================================== 此解法花了 23ms，更簡潔的寫法 ====================================
def dist_sort(s):
    distance = int(s[1]) ** 2 + int(s[2]) ** 2
    average = int(s[3]) / distance
    return average

def war_sort(s):
    return s[3]

n = int(input())
s = [input().split() for i in range(n)]
s.sort(key=war_sort)
s.sort(key=dist_sort,reverse=True)

for i in s:
  print(i[0])
  