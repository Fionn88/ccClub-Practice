"""
[11-1] 強強背單字
Description

強強的英文不太好，所以他把常見的單字列出來，然後想要從最短的單字開始背。給定一串字串，請將這些字串根據長度從短到長排序並輸出。如果有單字一樣長，就保持輸入時的順序。


Input
輸入為 1 行，為待排序的單字，單字之間以逗號分隔。


Output
輸出為 n 行，n為單字的數量，每行為從短到長排序完的單字。


Sample Input 1 
Ponka,Tankan,Murcott,Minneola tangelo

Sample Output 1
Ponka
Tankan
Murcott
Minneola tangelo

Sample Input 2 
Chiin Hwang,Irwin,Haden,Zill,Kent,Keitt

Sample Output 2
Zill
Kent
Irwin
Haden
Keitt
Chiin Hwang

Source
ccClub Judge
"""
numbers = input().split(',')
for i in sorted(numbers, key = len):
  print(i)