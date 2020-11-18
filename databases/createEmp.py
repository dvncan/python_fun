import mysql.connector;

conn = mysql.connector.connect(host = 'localhost', database='mydb', user='root', password='3@&wOnVLnWF^VG+KH-w.')

if conn.is_connected():
    print("connected to mysql db")

cursor = conn.cursor()

try:
    cursor.execute("insert into emp values(3, 'Abby', 300000)")
    conn.commit()
    print("employee added")
except:
    conn.rollback()



print('end')
cursor.close()
conn.close()
