"""
[7-1] 誰家的寵物
Description

小明家養了3隻兔子，分別叫殘暴戰狼、伏特加、白金之星，這些兔子都知道自己的名字，所以他們只會在主人叫自己名字的時候有反應。


Input
輸入為 1 行，為主人叫的名字。


Output
輸出為 1 行，為有反應的兔子，如果都沒有反應就輸出「沒反應」。


Sample Input 1 
伏特加

Sample Output 1
伏特加

Sample Input 2 
殺手皇后

Sample Output 2
沒反應

Source
ccClub Judge
"""
l = ['伏特加','殘暴戰狼','白金之星']
s = input()
if s in l:
  print(s)
else:
  print('沒反應')