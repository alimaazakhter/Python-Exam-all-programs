class ListOperations:
    def __init__(self):
        self.lst = []

    # a. Create dynamic list
    def create_list(self):
        try:
            n = int(input("Enter number of elements: "))
            self.lst = []
            for i in range(n):
                val = int(input(f"Enter element {i+1}: "))
                self.lst.append(val)
            print("List created successfully.")
        except ValueError:
            print("Please enter valid numbers.")

    # b. Display list
    def display_list(self):
        print("Current List:", self.lst)

    # c. Remove duplicates
    def remove_duplicates(self):
        self.lst = list(set(self.lst))
        print("List after removing duplicates:", self.lst)

    # d. Multiply all items
    def multiply_items(self):
        if not self.lst:
            print("List is empty.")
            return
        result = 1
        for i in self.lst:
            result *= i
        print("Multiplication of all items:", result)

    # e. Retrieve negative numbers
    def negative_numbers(self):
        neg = [i for i in self.lst if i < 0]
        print("Negative numbers:", neg)

    # f. Sort list
    def sort_list(self):
        self.lst.sort()
        print("Sorted List:", self.lst)

    # g. Find and update element
    def find_update(self):
        try:
            find = int(input("Enter element to find: "))
            if find in self.lst:
                new = int(input("Enter new value: "))
                index = self.lst.index(find)
                self.lst[index] = new
                print("Element updated successfully.")
            else:
                print("Element not found.")
        except ValueError:
            print("Invalid input.")

    # h. Delete whole list
    def delete_list(self):
        self.lst.clear()
        print("List deleted successfully.")

    # i. Largest and smallest
    def largest_smallest(self):
        if not self.lst:
            print("List is empty.")
            return
        print("Largest:", max(self.lst))
        print("Smallest:", min(self.lst))

    # j. Check list empty
    def check_empty(self):
        if not self.lst:
            print("List is empty.")
        else:
            print("List is not empty.")

    # k. Append element
    def append_element(self):
        try:
            val = int(input("Enter element to append: "))
            self.lst.append(val)
            print("Element appended.")
        except ValueError:
            print("Invalid input.")

    # l. Check existence and delete
    def check_delete(self):
        try:
            val = int(input("Enter element to check: "))
            if val in self.lst:
                self.lst.remove(val)
                print("Element found and deleted.")
            else:
                print("Element not found.")
        except ValueError:
            print("Invalid input.")


# -------- MAIN PROGRAM --------
obj = ListOperations()

while True:
    print("\n------ MENU ------")
    print("1. Create List")
    print("2. Display List")
    print("3. Remove Duplicates")
    print("4. Multiply All Items")
    print("5. Show Negative Numbers")
    print("6. Sort List")
    print("7. Find and Update Element")
    print("8. Delete Whole List")
    print("9. Largest and Smallest Element")
    print("10. Check List Empty")
    print("11. Append Element")
    print("12. Check & Delete Element")
    print("13. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            obj.create_list()
        elif choice == 2:
            obj.display_list()
        elif choice == 3:
            obj.remove_duplicates()
        elif choice == 4:
            obj.multiply_items()
        elif choice == 5:
            obj.negative_numbers()
        elif choice == 6:
            obj.sort_list()
        elif choice == 7:
            obj.find_update()
        elif choice == 8:
            obj.delete_list()
        elif choice == 9:
            obj.largest_smallest()
        elif choice == 10:
            obj.check_empty()
        elif choice == 11:
            obj.append_element()
        elif choice == 12:
            obj.check_delete()
        elif choice == 13:
            print("Program Exited.")
            break
        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter a valid number.")

