import mysql.connector;

conn = mysql.connector.connect(host = 'localhost', database='mydb', user='root', password='3@&wOnVLnWF^VG+KH-w.')

if conn.is_connected():
    print("connected to mysql db")

cursor = conn.cursor()

cursor.execute('select * from emp')

rows = cursor.fetchall()
print ("Total number of rows: ", cursor.rowcount)

for row in rows:
    print(row)

#row = cursor.fetchone()
#while row is not None:
#    print(row)
#    row=cursor.fetchone()

print('end')
cursor.close()
conn.close()
