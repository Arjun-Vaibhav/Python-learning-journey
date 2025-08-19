import mysql.connector as mc

con = mc.connect(
    host="localhost",
    user="root",
    password="9970353770",
    database="db_7263"   
)

cur = con.cursor()
print("Connected..")
