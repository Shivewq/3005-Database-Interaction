#Using psycopg Postgre SQL adapter https://www.psycopg.org/
import psycopg

#Database information
hostname = 'localhost'
database = 'assignment3'
port_id = 5432
username = 'postgres'
pswd = 'postgres'

#retrieve and display all records from the students table
def getAllStudents(conn):
    try:
        with conn.cursor() as cur:
            #select all entries in students table
            cur.execute("SELECT * FROM students")
            rows = cur.fetchall()
            print("ID    | First Name  | Last Name   | Email                      | Enrollment Date")
            print("-" * 75)  # Separator line
            for row in rows:
                #just reformatting the date display for each row (YYYY-MM-DD)
                enrollment_date_formatted = row[4].strftime('%Y-%m-%d')
                print(f"{row[0]:<5} | {row[1]:<11} | {row[2]:<10} | {row[3]:<27} | {enrollment_date_formatted}")
    except Exception as e:
        print("Error:", e)

#insert a new student record into the students table
def addStudent(conn, first_name, last_name, email, enrollment_date):
    try:
        with conn.cursor() as cur:
            #insert into students, provided the input parameters
            cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                        (first_name, last_name, email, enrollment_date))
            print("Student added successfully!")
            conn.commit()
    except Exception as e:
        print("Error:", e)
        conn.rollback()

# update the email address for a student with the specified student_id
def updateStudentEmail(conn, student_id, new_email):
    try:
        with conn.cursor() as cur:
            #use UPDATE sql command and SET for email attribute
            #find the student WHERE student_id = student_id(parameter)
            cur.execute("UPDATE students SET email = %s WHERE student_id = %s",
                        (new_email, student_id))
            if cur.rowcount > 0:
                print("Email updated successfully!")
            else:
                print("No student found with the provided student_id.")
            conn.commit()
    except Exception as e:
        print("Error:", e)
        conn.rollback()

# delete the record of the student with the specified student_id
def deleteStudent(conn, student_id):
    try:
        with conn.cursor() as cur:
            #use DELETE sql command where the student_id = student_id(parameter)
            cur.execute("DELETE FROM students WHERE student_id = %s",
                        (student_id,))
            if cur.rowcount > 0:
                print("Student deleted successfully!")
            else:
                print("No student found with the provided student_id.")
            conn.commit()
    except Exception as e:
        print("Error:", e)
        conn.rollback()

# Attempt to connect to database with provided information. 
# You may need to change data info to test on your own database 
try:
    with psycopg.connect(host = hostname, dbname = database, user = username,password = pswd, port = port_id) as conn:
        while True:
            # Request user input
            print("\nPlease Select an operation:\n ")
            print("1. Retrieve and display all records\n")
            print("2. Add a new student\n")
            print("3. Update the email of a student\n")
            print("4. Delete a student\n")
            print("5. Exit\n")
            
            choice = input("enter your choice (1-5): \n")
            #pick an operation by user
            if choice == '1':
                    getAllStudents(conn)
            elif choice == '2':
                #input the additional information for adding a new student
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                email = input("Enter email: ")
                enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")
                addStudent(conn, first_name, last_name, email, enrollment_date)
            elif choice == '3':
                student_id = int(input("Enter student ID: "))
                new_email = input("Enter new email: ")
                updateStudentEmail(conn, student_id, new_email)
            elif choice == '4':
                student_id = int(input("Enter student ID: "))
                deleteStudent(conn, student_id)
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
            
except Exception as error:
    print(error)


