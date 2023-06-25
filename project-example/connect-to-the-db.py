import pymysql


#資料庫連線設定
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='0624', db='fastapi', charset='utf8')
#建立操作游標
cursor = db.cursor()
#SQL語法

sql = "INSERT INTO book(id, title, author, publisher) VALUES (%s, %s, %s, %s);"
new_data = (4002,'title', 'author','publisher')

#執行語法
try:
  cursor.execute(sql,new_data)
  #提交修改
  db.commit()
  print('success')
except Exception as e:
  #發生錯誤時停止執行SQL
  db.rollback()
  print('error')
  print(e)

#關閉連線
db.close()