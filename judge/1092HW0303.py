"""
買飲料

描述
為了答謝朋友們的幫忙，小丹決定買飲料請大家喝。假設小丹的位置在 (0, 0)，給定飲料店的店名、位置、各品項價格資訊，請你根據以下規則幫他找出適合的飲料店：
如果飲料店直線距離超過小丹願意走的最遠距離，則絕對不考慮。
在所有距離內的飲料店中，把最貴的品項刪掉，計算出剩餘品項的平均價格，輸出平均價格第二低的店（保證算出來的各店平均價格不會相同）。
若在距離內的飲料店只有一家，則輸出該店；若沒有在距離內的店家，則輸出 no drink。

輸入
輸入有 n+1 行。
第一行包含兩個正整數 n, d，分別代表飲料店家數及小丹願意走的最遠距離。
接下來 n 行，每行包含店名，飲料店 x 坐標，y 坐標，以及該店各品項價格。

輸出
輸出有一行，請印出適合的飲料店店名，若無則印出 no drink。

輸入範例 1
3 10
小古 6 8 55 50 70
嘻嘻 3 4 30 30 40
小賴 10 10 40 30 45 40

輸出範例 1
小古

輸入範例 2
3 8
老麻 12 12 55 50 70
不可 3 4 30 30 100
大米 4 8 40 30 45 40

輸出範例 2
不可
"""