import mysql.connector

# Database connection
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
        
        query = "INSERT INTO student(id, name, std, marks) VALUES (%s, %s, %s, %s)"
        val = (id, name, std, marks)
        cursor.execute(query, val)
        conn.commit()
        print('✅ Student Record Added Successfully.\n')
    except ValueError:
        print("❌ Invalid input. Please enter numbers for ID, class, and marks.\n")

def getAllStudent():
    cursor.execute("SELECT * FROM student")
    results = cursor.fetchall()
    print_results(results)

def updateStudent():
    try:
        current_id = int(input('Enter the Student ID you want to update: '))
        new_id = int(input('Enter New ID: '))
        name = input('Enter New Student Name: ')
        std = int(input("Enter New Student Class: "))
        marks = int(input('Enter New Student Marks: '))

        query = "UPDATE student SET id=%s, name=%s, std=%s, marks=%s WHERE id=%s"
        val = (new_id, name, std, marks, current_id)

        cursor.execute(query, val)
        conn.commit()
        print('✅ Student Record Updated Successfully.\n')
    except ValueError:
        print("❌ Invalid input. Please enter numbers for ID, class, and marks.\n")

def deleteStd():
    try:
        id = int(input('Enter the Student ID you want to Delete: '))
        query = "DELETE FROM student WHERE id=%s"
        cursor.execute(query, (id,))
        conn.commit()
        print('✅ Student Record Deleted Successfully.\n')
    except ValueError:
        print("❌ Invalid input. ID must be a number.\n")

def getDataById():
    try:
        id = int(input('Enter Id you want to get data: '))
        query = "SELECT * FROM student WHERE id=%s"
        cursor.execute(query, (id,))
        results = cursor.fetchall()
        print_results(results)
    except ValueError:
        print("❌ Invalid input. ID must be a number.\n")

def getStudentByName():
    name = input("Enter Student Name to search: ")
    query = "SELECT * FROM student WHERE name=%s"
    cursor.execute(query, (name,))
    results = cursor.fetchall()
    print_results(results)

def getAllStudentsAscending():
    query = "SELECT * FROM student ORDER BY name ASC"
    cursor.execute(query)
    results = cursor.fetchall()
    print_results(results)

def print_results(results):
    if results:
        for row in results:
            print(row)
    else:
        print("⚠ No records found.\n")

# Main Menu Loop
ans = "Y"
while ans.upper() == 'Y':
    print('\n\t\t\t Student Portal')
    print("*" * 100)
    print('\t1. Add new student')
    print('\t2. Get All Students')
    print('\t3. Update Student')
    print('\t4. Delete Student')
    print('\t5. Get Data student by ID')
    print('\t6. Get Data student by Name')
    print('\t7. Get All Students in Ascending Order')
    print("*" * 100)

    try:
        choice = int(input('Enter your choice: '))
        if choice < 1 or choice > 7:
            print('⚠ Please enter choice between 1 to 7\n')
            continue
    except ValueError:
        print("❌ Invalid input. Please enter a number.\n")
        continue

    if choice == 1:
        addStudent()
    elif choice == 2:
        getAllStudent()
    elif choice == 3:
        updateStudent()
    elif choice == 4:
        deleteStd()
    elif choice == 5:
        getDataById()
    elif choice == 6:
        getStudentByName()
    elif choice == 7:
        getAllStudentsAscending()

    ans = input("Do you want to continue? (Y/N): ")

else:
    print('👋 Thanks for using this program!')

cursor.close()
conn.close()
