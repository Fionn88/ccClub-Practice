"""
挑食寶寶
描述

嘻嘻幼幼班裡的咚咚是個每天會討厭吃不同東西的挑食寶寶，同時他也是一個眼光銳利的寶寶，他總是會在吃午餐之前快速掃過托盤裡面他不吃的東西，然後決定自己有多少東西不吃。舉例來說，他今天不想吃蛋跟肉，那麼肉蛋吐司裡面她就只會吃吐司，肉蛋這兩樣他就不吃。現在，給定一個代表他今天挑食不吃的字串，以及幼幼班今天發放的午餐，請輸出咚咚今天不吃的午餐總共不吃多少東西。


輸入
共兩行，

第一行，包含一字串

第二行，包含一字串


輸出
共一行，輸出一整數


輸入範例 1 
肉蛋吐司
肉蛋

輸出範例 1
2

輸入範例 2 
7788的肉肉果實
78肉

輸出範例 2
6
"""

full=list(input())
hate=list(input())

count=0

for num in full:
	if num in hate:
		count+=1

print(count)
