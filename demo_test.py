import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="ldx12138",
    auth_plugin='mysql_native_password',
    database="runoob_db",
)
mycursor = mydb.cursor() 
 
sql = "DROP TABLE IF EXISTS sites"  # 删除数据表 sites
 
mycursor.execute(sql)