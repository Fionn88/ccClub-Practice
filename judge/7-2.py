"""
7-2：加減長方形
Description

輸入兩個正整數 l 和 w，交錯使用「+」和「-」輸出一個長寬分別為 l 和 w 的長方形。


Input
輸入有兩行，各包含一個整數


Output
輸出一個長寬分別為 l 和 w 的長方形


Sample Input 1 
3
2

Sample Output 1
+-+
-+-

Sample Input 2 
4
3

Sample Output 2
+-+-
+-+-
+-+-

Sample Input 3 
7
5

Sample Output 3
+-+-+-+
-+-+-+-
+-+-+-+
-+-+-+-
+-+-+-+

Sample Input 4 
1
1

Sample Output 4
+

Source
ccClub Judge
"""

point=int(input()) 
line=int(input()) 

if point%2!=0:
    for i in range (line):
        if i != 0:
          print(end="\n")     
        if i%2!=0:
            for x in range (point):
                if x%2!=0:
                    print("+",end="")
                elif x%2==0:
                    print("-",end="")
        elif i%2==0:
            for n in range (point):
                if n%2!=0:
                    print("-",end="")
                elif n%2==0:
                    print("+",end="")       
elif point%2==0:
    for i in range (line):
        if i != 0:
          print(end="\n")
        for a in range(point):
            if a%2!=0:
                print("-",end="")
            elif a%2==0:
                print("+",end="")
