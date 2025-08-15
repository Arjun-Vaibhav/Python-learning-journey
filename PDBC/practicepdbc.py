import mysql.connector

conn =mysql.connector.connect(
    host='localhost',
    username='root',
    password='9970353770',
    database='db_7263'

)

print(conn)



cursor=conn.cursor()

#1. create new table "account" and add custid, custname, balance, acct_type fields

# query="CREATE TABLE account (custid int, custname varchar(30), balance int,account_type varchar(30))"
# cursor.execute(query)
# print('Table created succefully..')

#2. Add 4 to 5 dynamic records in account table

cusid=int(input('Enter customer id:'))
custname=input('Enter the customer name:')
balance=int(input('Enter balance:'))
account_type=input('Enter the account type:')

addquery="INSERT INTO account VALUES (%s,%s,%s,%s)"
val=(cusid,custname,balance,account_type)
cursor.execute(addquery,val)
conn.commit()
print(cursor.rowcount,"row is created")
conn.close()
#3. select specific customer details by customer name


#4. get details by acct_type


#5. update record dynamically (any one as per cond)




#6. select all records and show on terminal in proper format


#7. delete record by balance (write dynamic query)