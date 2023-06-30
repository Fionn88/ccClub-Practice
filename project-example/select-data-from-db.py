import pymysql

# 連結 SQL
import pymysql

# 連結 SQL
connect_db = pymysql.connect(host='{replace_me}', port=3306, user='{replace_me}', passwd='{replace_me}', charset='utf8', db='{replace_me}')

with connect_db.cursor() as cursor:
    sql = """
    SELECT * from book
    """
    
    # 執行 SQL 指令
    cursor.execute(sql)
    
    # 取出全部資料
    data = cursor.fetchall()
    print(data)

# 關閉 SQL 連線
connect_db.close()