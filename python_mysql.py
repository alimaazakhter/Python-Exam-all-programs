import mysql.connector

class StudentDB:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
            port=3307
            )
            self.cur = self.conn.cursor()   
            print("MySQL Connected Successfully")
            self.create_db()
            self.create_table()
        except Exception as e:
            print("Connection Error:", e)


    # a. Create Database
    def create_db(self):
        try:
            self.cur.execute("CREATE DATABASE IF NOT EXISTS SVGU")
            self.cur.execute("USE SVGU")
            print("Database SVGU Ready")
        except Exception as e:
            print("DB Error:", e)

    # b. Create Table
    def create_table(self):
        try:
            self.cur.execute("""
                CREATE TABLE IF NOT EXISTS Students(
                    rno INT PRIMARY KEY,
                    name VARCHAR(50),
                    dept VARCHAR(30),
                    per FLOAT
                )
            """)
            print("Table Students Ready")
        except Exception as e:
            print("Table Error:", e)

    # c. Insert Records
    def insert_students(self):
        try:
            n = int(input("How many records you want to insert? "))
            for i in range(n):
                rno = int(input("Enter Roll No: "))
                name = input("Enter Name: ")
                dept = input("Enter Department: ")
                per = float(input("Enter Percentage: "))

                self.cur.execute(
                    "INSERT INTO Students VALUES(%s,%s,%s,%s)",
                    (rno, name, dept, per)
                )
                self.conn.commit()
            print("Records Inserted Successfully")
        except Exception as e:
            print("Insert Error:", e)

    # d. Delete Record by rno
    def delete_student(self):
        try:
            rno = int(input("Enter Roll No to delete: "))
            self.cur.execute("DELETE FROM Students WHERE rno=%s", (rno,))
            self.conn.commit()
            print("Record Deleted Successfully")
        except Exception as e:
            print("Delete Error:", e)

    # e. Update Record by rno
    def update_student(self):
        try:
            rno = int(input("Enter Roll No to update: "))
            name = input("Enter New Name: ")
            dept = input("Enter New Department: ")
            per = float(input("Enter New Percentage: "))

            self.cur.execute("""
                UPDATE Students 
                SET name=%s, dept=%s, per=%s 
                WHERE rno=%s
            """, (name, dept, per, rno))

            self.conn.commit()
            print("Record Updated Successfully")
        except Exception as e:
            print("Update Error:", e)

    # f. Select Students by Dept
    def select_by_dept(self):
        try:
            dept = input("Enter Department: ")
            self.cur.execute("SELECT * FROM Students WHERE dept=%s", (dept,))
            data = self.cur.fetchall()

            if not data:
                print("No records found.")
            else:
                for row in data:
                    print(row)
        except Exception as e:
            print("Select Error:", e)

obj = StudentDB()

while True:
    print("\n----- STUDENT MENU -----")
    print("1. Insert Student Records")
    print("2. Delete Student by Roll No")
    print("3. Update Student by Roll No")
    print("4. Display Students by Department")
    print("5. Exit")

    try:
        ch = int(input("Enter your choice: "))

        if ch == 1:
            obj.insert_students()
        elif ch == 2:
            obj.delete_student()
        elif ch == 3:
            obj.update_student()
        elif ch == 4:
            obj.select_by_dept()
        elif ch == 5:
            print("Program Exited.")
            break
        else:
            print("Invalid Choice")
    except ValueError:
        print("Enter valid number")
