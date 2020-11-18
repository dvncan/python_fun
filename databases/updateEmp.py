import mysql.connector;

def update(sal):
    conn = mysql.connector.connect(host = 'localhost', database='mydb', user='root', password='3@&wOnVLnWF^VG+KH-w.')

    if conn.is_connected():
        print("connected to mysql db")
        cursor = conn.cursor()
        str = "Select emp where id= SET sal=%'d'"
        args=(sal)

        try:
            cursor.execute(str % args)
            conn.commit()
            print("employee updated")
        except:
            conn.rollback()
            print("woops")

        finally:
            print('end')
            cursor.close()
            conn.close()
empId = int(input('Enter Emp Id:'))
sal = int(input('Enter new Emp salary:'))
update(sal)
