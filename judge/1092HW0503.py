"""
消消樂

描述
嘻嘻工廠推出一款新遊戲叫嘻凹嘻凹樂。遊戲開始時，畫面上會隨機出現一排不同顏色的寶石。玩家可以點擊寶石，將相鄰且同樣顏色的兩個寶石消掉，消掉之後左右的寶石會粘起來，空隙消失。遊戲目標就是不斷將相鄰且相同顏色的兩個寶石消除，在越短的時間內將所有寶石消完，就可以獲得越高積分。
然而小嘻玩了幾關後，發現有些關卡無論如何都無法將寶石消完。他決定搜集遊戲資料向嘻嘻工廠投訴。給定初始的寶石串列，你能幫小嘻找到剩下無法消掉的寶石們嗎？

輸入
輸入有一行，代表初始的寶石列。

輸出
輸出有一行，代表剩下無法消去的寶石列，若可以剛好消完，則不用輸出。

輸入範例 1 
紫藍藍紅紅紫綠

輸出範例 1
綠

輸入範例 2 
黑紫紫紅紅紅黑

輸出範例 2
黑紅黑

提示
範例一：紫藍藍紅紅紫綠 -> 紫紅紅紫綠 -> 紫紫綠 -> 綠
範例二：黑紫紫紅紅紅黑 -> 黑紅紅紅黑 -> 黑紅黑
"""

the_string_input = input()
res = []

for index, value in enumerate(the_string_input):
    if not res or value != res[-1]: 
        res.append(value)
    else:
        res.pop()

print(''.join(res))
