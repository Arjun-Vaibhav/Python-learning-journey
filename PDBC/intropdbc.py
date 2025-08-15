 

# 1.install mysql-connector-Python
# 2.import mysql.connector module
import mysql.connector
# 3.Create connection object
conn =mysql.connector.connect(
    host='localhost',
    username='root',
    password='',
    database='db_7263'

)

# 4.Check the connection is established to mysql or not
print(conn)
# 5) create cursor class instance for query execution
vaibhav=conn.cursor()
# 6) execution  query thro cursor class instace
query=  " CREATE TABLE person (pid int,pname varchar(30), age int, role varchar(30))"
vaibhav.execute(query)
# 7) print result on terminal
print('Table Created successfully')
# 8) close connection
conn.close()


