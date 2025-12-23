class DictionaryOperations:
    def __init__(self):
        self.d = {}   # Empty dictionary initially

    # a. Take dictionary key-value as input
    def take_input(self):
        try:
            n = int(input("How many items you want to add? "))
            for i in range(n):
                key = input(f"Enter key {i+1}: ")
                value = input(f"Enter value for '{key}': ")
                self.d[key] = value
            print("Dictionary stored successfully!")
            print("Current Dictionary:", self.d)
        except Exception as e:
            print("Error:", e)

    # b. Add a specified item
    def add_item(self):
        try:
            key = input("Enter key to add: ")
            value = input("Enter value: ")
            self.d[key] = value
            print("Item added successfully!")
            print("Updated Dictionary:", self.d)
        except Exception as e:
            print("Error:", e)
       

    # c. Sort dictionary by key
    def sort_by_key(self):
        try:
            sorted_dict = dict(sorted(self.d.items()))
            print("Dictionary sorted by keys:")
            print(sorted_dict)
        except Exception as e:
            print("Error:", e)

    # d. Check key and remove item
    def remove_item(self):
        try:
            key = input("Enter key to remove: ")
            if key in self.d:
                del self.d[key]
                print(f"Key '{key}' removed successfully!")
            else:
                print("Key NOT found!")
            print("Updated Dictionary:", self.d)
        except Exception as e:
            print("Error:", e)

    # e. Print only values
    def print_values(self):
        try:
            print("Values in Dictionary:")
            for value in self.d.values():
                print(value)
        except Exception as e:
            print("Error:", e)

    # f. Print all keys
    def print_keys(self):
        try:
            print("Keys in Dictionary:")
            for key in self.d.keys():
                print(key)
        except Exception as e:
            print("Error:", e)

    # g. Check key exists and update value
    def update_value(self):
        try:
            key = input("Enter key to update value: ")
            if key in self.d:
                new_value = input("Enter new value: ")
                self.d[key] = new_value
                print("Value updated successfully!")
            else:
                print("Key does NOT exist!")
            print("Updated Dictionary:", self.d)
        except Exception as e:
            print("Error:", e)

    # h. Count number of items
    def count_items(self):
        try:
            print("Number of items in dictionary:", len(self.d))
        except Exception as e:
            print("Error:", e)

    # i. Search item by key
    def search_item(self):
        try:
            key = input("Enter key to search: ")
            if key in self.d:
                print(f"Value for '{key}' is:", self.d[key])
            else:
                print("Key NOT found!")
        except Exception as e:
            print("Error:", e)


# ---------------- MAIN MENU ----------------
def main():
    obj = DictionaryOperations()

    while True:
        print("\n------ MENU ------")
        print("1. Take Dictionary Input")
        print("2. Add Item")
        print("3. Sort Dictionary by Key")
        print("4. Remove Item by Key")
        print("5. Print Values")
        print("6. Print Keys")
        print("7. Update Value if Key Exists")
        print("8. Count Items")
        print("9. Search Item by Key")
        print("10. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except:
            print("Invalid input! Enter a number.")
            continue

        if choice == 1:
            obj.take_input()
        elif choice == 2:
            obj.add_item()
        elif choice == 3:
            obj.sort_by_key()
        elif choice == 4:
            obj.remove_item()
        elif choice == 5:
            obj.print_values()
        elif choice == 6:
            obj.print_keys()
        elif choice == 7:
            obj.update_value()
        elif choice == 8:
            obj.count_items()
        elif choice == 9:
            obj.search_item()
        elif choice == 10:
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid Choice! Try again.")


# Run the program
main()