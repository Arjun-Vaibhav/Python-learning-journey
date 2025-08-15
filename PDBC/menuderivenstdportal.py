import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',              
    password='9970353770',
    database='db_7263'
)

cursor = conn.cursor()       

def addStudent():
    try:
        id = int(input('Enter Student Id: '))
        name = input('Enter Student Name: ')
        std = int(input("Enter Student class: "))
        marks = int(input('Enter Student Marks: '))
    except ValueError:
        print("dont Enter any symbol,alpnumeric value..")    
        query = "INSERT INTO student VALUES (%s, %s, %s, %s)"
        val = (id, name, std, marks)
        cursor.execute(query, val)
        conn.commit()
        print('Student Record Added Successfully..\n')
def GetAllStudent():
    cursor.execute("SELECT * FROM student")
    results = cursor.fetchall()
    for row in results:
        print(row)
def UpdateStudent():
    current_id = int(input('Enter the Student ID you want to update: '))    
    new_id = int(input('Enter New ID: '))
    name = input('Enter New Student Name: ')
    std = int(input("Enter New Student Class: "))
    marks = int(input('Enter New Student Marks: '))

    query = "UPDATE student SET id=%s, name=%s, std=%s, marks=%s WHERE id=%s"
    val = (new_id, name, std, marks, current_id)

    cursor.execute(query, val)
    conn.commit()
    print('✅ Student Record Updated Successfully..\n')
def DeleteStd():
    id = int(input('Enter the Student ID you want to Delete: '))
    query3="delete from student where id=%s"
    val=(id,)
    cursor.execute(query3,val)
    conn.commit()
    print('✅ Student Record Deleted Successfully..\n')
def GetdataByid():
    id=int(input('Enter Id you want to  get data:'))
    query="SELECT * FROM student WHERE id=%s"
    val=(id,)
    cursor.execute(query,val)
    idstddata=cursor.fetchall()
    for datas in idstddata:
        print(datas)
    conn.commit()
def getStudentByName():
    name = input("Enter Student Name to search: ")
    query = "SELECT * FROM student WHERE name = %s"
    val = (name,)
    cursor.execute(query,val)
    result = cursor.fetchall()
    for datas in result:
        print(datas)

def getAllStudentsAscending():
    query = "SELECT * FROM student ORDER BY name ASC"
    cursor.execute(query)
    result = cursor.fetchall()
    for i in result:
        print(i)
ans = "Y"
while ans.upper():    
    print('\t\t\t Student Portal')
    print("*" * 100)
    print('\t\t\t 1. Add new student')
    print('\t\t\t 2. Get All Students')
    print('\t\t\t 3. Update Student')
    print('\t\t\t 4. Delete Student')
    print('\t\t\t 5. Get Data student by id')
    print('\t\t\t 6. Get Data student by name')
    print('\t\t\t 7. Get All Students in Ascending Order')
    print("*" *100)

    try:
        choice = int(input('Enter your choice: '))
        if choice>=7:
            print('plz Enter choice between 1 to 7')        
    except ValueError:
        print("Invalid input. Please enter a number.\n")
        continue
    if choice == 1:
        addStudent()
    elif choice == 2:
        GetAllStudent()    
    elif choice==3:
        UpdateStudent()
    elif choice==4:
        DeleteStd()
    elif choice==5:
        GetdataByid()
    elif choice==6:
       getStudentByName()
    elif choice==7:
        getAllStudentsAscending()
    ans = input("Do you want to continue? (Y/N):  ")
conn.close()
