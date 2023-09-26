"""
小葉喝可樂
描述

大賣場預告即將推出行銷活動，消費者無論購買幾瓶可樂，只要喝完並集滿規定數量的空瓶後，就可以再兌換一瓶新的可樂；如果新兌換的可樂喝完，而消費者手上也還有空瓶，就可以再依照規定數量去換可樂。

愛喝可樂的小葉聽到了很興奮，可是他不知道最後大賣場會規定要集滿幾個空瓶，才能換全新可樂。為了讓小葉快速算出他最後可以喝到的可樂數量，請你幫他寫一個程式，讓他在活動推出後，能快速依照他想買的可樂數量，算出最終他可以喝到的可樂數量吧！


輸入
輸入有兩行

一個是小葉初始購買可樂的數量

一個是賣場規定需集滿的空瓶數量


輸出
一行，小葉可以喝到的可樂總數


輸入範例 1 
9
3

輸出範例 1
13

輸入範例 2 
40
6

輸出範例 2
47

提示
Sample input 1 的情況：最終大賣場規定活動為集滿 3 個空瓶可換一瓶全新可樂
而小葉一開始買了 9 瓶可樂，則 input 1 = 9，input 2 = 3。
小葉喝完可樂後，可再換 3 瓶可樂，而這 3 瓶可樂喝完後，又可以再換一瓶可樂。
因此小葉可以喝到的可樂數量為 9 + 3 + 1 = 13
"""
init = int(input())
free_to_change = int(input())

total_colas = init  
empty_bottles = init 

while empty_bottles >= free_to_change: 
    new_colas = empty_bottles // free_to_change  
    total_colas += new_colas
    empty_bottles = new_colas + (empty_bottles % free_to_change) 

print(total_colas)
