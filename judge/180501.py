"""
電影選片
Description

今天我們給定某一個人（讓我們姑且叫他凱文）的電影偏好，請用計分的方式幫他比較兩部電影的喜好順序，請輸出分數較高者：

可能出現的分類一共有："Fantasy"、"Drama"、"Action"、"Thriller"、"Comedy"、"Crime"、"History"、"Romance"、"Adventure"、"Biography" 十個類別，請依照這個順序，若此影片的類型包含 "Fantasy" 加 10 分、"Drama" 加 9 分、"Action" 加8分......以此類推，保證每一部電影都會給三個在這當中的類型
除了類別以外，凱文還很重視IMDb這個網站的給分，因此，請替他加上IMDb的分數
如果兩部電影得到的總分相同，請將兩部電影名稱都輸出

Input
輸入包含六行（代表兩部電影）。

第一行及第四行為電影名稱，第二行及第五行為該電影的 IMDB 評價分數，第三行及第六行為該電影的分類。


Output
輸出包含一或兩行，各包含一個字串


輸入範例 1 
The Shape of Water
IMDb:7.4
Adventure Drama Fantasy
The King's Speech
IMDb:8.0 
Biography Drama

輸出範例 1
The Shape of Water

輸入範例 2 
Fight Club
IMDb:8.8
Drama Thriller
Léon
IMDb:8.8
Drama Thriller

輸出範例 2
Fight Club
Léon

來源
ccClub Judge
"""
grouped_data,data,flag = [],[],True
label = {"Fantasy":10,"Drama":9,"Action":8,"Thriller":7,"Comedy":6,"Crime":5,"History":4,"Romance":3,"Adventure":2,"Biography":1}
while True:
  try:
    data.append(input())
  except:
    break
for i in range(0, len(data), 3):
    group = data[i:i+3]
    grouped_data.append(group)

for index,raw in enumerate(grouped_data):
  count = 0
  for j in raw[2].split():
    count += int(label[j])
  if index == 0:
    prev = count
  elif index == 1 and prev == count:
    flag = False
  elif index == 1 and prev > count:
    print(grouped_data[0][0])
  elif index == 1 and prev < count:
    print(grouped_data[1][0])

if not flag:
  for index,raw in enumerate(grouped_data):
    if index == 0:
      prev = raw[1].split(':')[1]
    elif index == 1 and prev == raw[1].split(':')[1]:
      print(grouped_data[0][0])
      print(grouped_data[1][0])
    elif index == 1 and prev > raw[1].split(':')[1]:
      print(grouped_data[0][0])
    elif index == 1 and prev < raw[1].split(':')[1]:
      print(grouped_data[1][0])
