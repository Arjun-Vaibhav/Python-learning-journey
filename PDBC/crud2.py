import mysql.connector

conn =mysql.connector.connect(
    host='localhost',
    username='root',
    password='',
    database='db_7263'
)
# pid=int(input('select id you want to delete person:'))
cursor=conn.cursor()
# query1="insert into person values(%s,%s,%s,%s)"
# query2="update person set pname=%s where pid=%s"
# val=(pname,pid)
# query3="delete from person where pid=%s"
# val=[(7,"Tushar",45,"HR"),
#      (8,"Tushar",30,"CEO"),
#      (9,"Tushar",20,"data")]
# val=(pid,)
# cursor.execute(query3,val)
query="select * from person"
cursor.execute(query)

x=cursor.fetchall()
for i in x:
    print(f"{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}")
# conn.commit()

print(cursor.rowcount,"row is deleted")
conn.close()