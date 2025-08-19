import mysql.connector

conn =mysql.connector.connect(
    host='localhost',
    username='root',
    password='9970353770',
    database='db_7263'
)


pid=int(input('enter the person id:'))
pname=input('Enter person name:')
age=int(input('Enter the age:'))
role=input('Enter employee role:')

cursor=conn.cursor()
query="insert into person(pid,pname,age,role) values(%s,%s,%s,%s)"
val=(pid,pname,age,role)

cursor.execute(query,val)

conn.commit()
print(cursor.rowcount,"row is added")
conn.close()