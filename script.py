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
            cur.execute("SELECT * FROM students")
            rows = cur.fetchall()
            for row in rows:
                print(row)
    except Exception as e:
        print("Error:", e)

#insert a new student record into the students table
def addStudent(conn, first_name, last_name, email, enrollment_date):
    try:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                        (first_name, last_name, email, enrollment_date))
            print("Student added successfully!")
            conn.commit()
    except Exception as e:
        print("Error:", e)

# update the email address for a student with the specified student_id
def updateStudentEmail(conn, student_id, new_email):
    try:
        with conn.cursor() as cur:
            cur.execute("UPDATE students SET email = %s WHERE student_id = %s",
                        (new_email, student_id))
            if cur.rowcount > 0:
                print("Email updated successfully!")
            else:
                print("No student found with the provided student_id.")
            conn.commit()
    except Exception as e:
        print("Error:", e)

# delete the record of the student with the specified student_id
def deleteStudent(conn, student_id):
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM students WHERE student_id = %s",
                        (student_id,))
            if cur.rowcount > 0:
                print("Student deleted successfully!")
            else:
                print("No student found with the provided student_id.")
            conn.commit()
    except Exception as e:
        print("Error:", e)

# Attempt to connect to database with provided information. 
# You may need to change data info to test on your own database 
try:
    with psycopg.connect(host = hostname, dbname = database, user = username,password = pswd, port = port_id) as conn:
        while True:
            print("\nPlease Select an operation:\n ")
            print("1. Retrieve and display all records\n")
            print("2. Add a new student\n")
            print("3. Update the email of a student\n")
            print("4. Delete a student\n")
            print("5. Exit\n")
            
            choice = input("enter your choice (1-5): ")
            
            if choice == '1':
                    getAllStudents(conn)
            elif choice == '2':
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
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
            
except Exception as error:
    print(error)


