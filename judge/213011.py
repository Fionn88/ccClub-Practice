"""
小仔刪好友

描述
小仔最近覺得自己臉書好友好像有些都不是很熟，所以想要刪除一些好友，給定小仔好友數目 N 和要刪除好友的數目 T，與一行小仔與每個好友的互動程度(以數字代表程度)，小仔刪除的方法如下：
由前往後一個一個看互動程度，如果現在所在位置好友的互動度比下一個位置好友的互動度低，就把現在在位置的好友刪除，刪除後再從頭開始，直到刪除達 T 人，若是看完所有好友後刪除人數仍不足 T，就從後面刪除好友直到補足 T 人。
結束輸出剩餘好友每人的互動程度。
請你以依照 template 實作 linked-list ，先處理輸入且將題目給定數字轉換成 linked-list 做處理，並依照題目要求刪除，最後將處理過後的 linked-list 的第一個節點設成 head 這個變數名稱，不需有輸出，要求的時間複雜度為 O(n)

輸入
共兩行，第一行包含兩個整數，分別為 N 和 T，中間以空格隔開，代表好友數目和要刪除好友的數目，第二行包含 N 個整數，代表每個好友的互動程度

輸出
不需處理輸出，sample 為刪除後 linked-list 各節點資料中的數字(請自行寫函式測試 linked-list 結果是否正確)

輸入範例 1
6 2
18 93 10 31 12 20

輸出範例 1
93 31 12 20

輸入範例 2
10 3
19 12 8 18 46 5 25 34 5 17

輸出範例 2
19 46 5 25 34 5 17
"""

# 用這解法，順序不一樣答案就會因此不同
class LinkedListNode:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node

allFriend, deleted = map(int,input().split())
impression = input().split()
for index,element in enumerate(impression):
    if index == 0:
        node = LinkedListNode(element)
    elif index == 1:
        node = LinkedListNode(element,node)

for _ in range(6):
    print(node.value)
    node = node.next_node
