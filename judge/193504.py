"""
球員成績分析

描述
吾郎是一個很認真的棒球選手，每天認真的訓練希望自己有招一日可以登上美國職棒大聯盟的投手丘。
他每天都會將訓練的數據做量化，並交給電腦進行分析，得到當天表現的分數。
為了了解他過去訓練的成果，會需要分析他每天訓練的資料，計算每次訓練之後隔幾次之後分數是提升的，藉此修正訓練方式，讓自己的分數能越來越好。
請寫一個程式，協助他分析過去的訓練資料。

輸入
輸入有一行，包含數個整數，代表每次訓練的分數，數字之間用空格分割。

輸出
輸出有一行，包含數個整數，代表該次訓練後隔幾次後分數提升了（若之後分數都沒提升，則為 0），數字之間用空格分割。

輸入範例 1 
89 56 78 9 81 7

輸出範例 1
0 1 2 1 0 0

輸入範例 2 
76 3 60 57 11 72 73 86 27 91 56 58 21 2

輸出範例 2
7 1 3 2 1 1 1 2 1 0 1 0 0 0

提示
sample input 1 中，輸入的分數分別為 89 56 78 9 81 7：
89 之後都沒有比這次訓練更高的分數，因此輸出 0。
56 之後下一次就出現比這次訓練更高的分數，因此輸出 1。
78 之後下兩次才出現比這次訓練更高的分數，因此輸出 2。
9 之後下一次就出現比這次訓練更高的分數，因此輸出 1。
81 之後都沒有比這次訓練更高的分數，因此輸出 0。
7 之後都沒有比這次訓練更高的分數，因此輸出 0。

提示：
可先了解堆疊（stack）的運作，參考資料：http://alrightchiu.github.io/SecondRound/stack-introjian-jie.html。
關於堆疊在 Python 中的實作，可參考https://docs.python.org/zh-tw/3/tutorial/datastructures.html中 5.1.1 使用 python list 來實作 Stack。
解這題時不一定要從頭往後看，也可以考慮從尾巴往前看（以 sample input 1 為例的話，就是先看 7 => 81 => 9 => ... => 56 => 89）

來源
ccClub Judge
"""

# Time Limit Exceeded
score = list(map(int,input().split()))
stack = []
result = [0] * len(score)
for currentDay in range(len(score)):
    while stack and score[currentDay] > score[stack[-1]]:
        j = stack.pop()
        result[j] = currentDay - j
        
    stack.append(currentDay)
for i in result:
    print(i,end=' ')
    