import pickle
import os

class Employee:
    def __init__(self):
        self.file = "emp.dat"

    def add(self):
        try:
            emp_code = int(input("Enter Employee Code: "))
            name = input("Enter Name: ")
            dept = input("Enter Department: ")
            desg = input("Enter Designation: ")
            sal = float(input("Enter Salary: "))

            rec = [emp_code, name, dept, desg, sal]

            with open(self.file, "ab") as f:
                pickle.dump(rec, f)

            print("Record Added Successfully.\n")

        except ValueError:
            print("Invalid input.\n")

    def load(self):
        if not os.path.exists(self.file):
            return []

        data = []
        with open(self.file, "rb") as f:
            while True:
                try:
                    data.append(pickle.load(f))
                except EOFError:
                    break
        return data

    def show_all(self):
        data = self.load()
        if not data:
            print("No records found.\n")
            return

        for r in data:
            print(r)
        print()

    def show_by_dept(self):
        d = input("Enter Department: ")
        data = self.load()
        found = False

        for r in data:
            if r[2].lower() == d.lower():
                print(r)
                found = True

        if not found:
            print("No employee found in this department.")
        print()

    def show_by_sal(self):
        data = self.load()
        found = False

        for r in data:
            if r[4] > 5000:
                print(r)
                found = True

        if not found:
            print("No employee with salary greater than 5000.")
        print()


# ---------- MENU ----------
s = Employee()

while True:
    print("1. Add Employee")
    print("2. Show All Employees")
    print("3. Search By Department")
    print("4. Search By Salary (>5000)")
    print("5. Exit")

    ch = input("Enter your Choice: ")

    if ch == '1':
        s.add()
    elif ch == '2':
        s.show_all()
    elif ch == '3':
        s.show_by_dept()
    elif ch == '4':
        s.show_by_sal()
    elif ch == '5':
        print("Program Exited.")
        break
    else:
        print("Invalid Choice\n")

