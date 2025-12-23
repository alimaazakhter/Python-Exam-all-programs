class StringOperations:
    def __init__(self):
        self.s = ""   # store the input string

    # a. Take a string as input from user
    def take_input(self):
        try:
            self.s = input("Enter a string: ")
            print("String stored successfully!")
        except Exception as e:
            print("Error:", e)

    # b. Check whether substring exists in main string
    def check_substring(self):
        try:
            sub = input("Enter substring to search: ")
            if sub in self.s:
                print(f"Substring '{sub}' FOUND in the string.")
            else:
                print(f"Substring '{sub}' NOT FOUND.")
        except Exception as e:
            print("Error:", e)

    # c. Count consonants in string
    def count_consonants(self):
        try:
            vowels = "aeiouAEIOU"
            count = 0
            for ch in self.s:
                if ch.isalpha() and ch not in vowels:
                    count += 1
            print("Total Consonants:", count)
        except Exception as e:
            print("Error:", e)

    # d. Convert lowercase string to uppercase
    def check_lower(self):
        try:
            if self.s.islower():
                print("String is in lowercase.")
                print("Converted to UPPERCASE:", self.s.upper())
            else:
                print("String is NOT in lowercase.")
        except Exception as e:
            print("Error:", e)

    # e. Check if string is digit
    def check_digit(self):
        try:
            if self.s.isdigit():
                print("String contains digits only.")
            else:
                print("String does NOT contain digits only.")
        except Exception as e:
            print("Error:", e)

    # f. Count occurrences of character
    def count_character(self):
        try:
            ch = input("Enter a character to check: ")
            if len(ch) != 1:
                print("Please enter a single character only.")
                return
            count = 0
            for c in self.s:
                if c == ch:
                    count += 1
            print(f"Character '{ch}' appears {count} times.")
        except Exception as e:
            print("Error:", e)

    # g. Length of string without using len()
    def find_length(self):
        try:
            count = 0
            for _ in self.s:
                count += 1
            print("Length of string:", count)
        except Exception as e:
            print("Error:", e)

    # h. Display string in reverse
    def reverse_string(self):
        try:
            rev = ""
            for ch in self.s:
                rev = ch + rev
            print("Reversed String:", rev)
        except Exception as e:
            print("Error:", e)

    # i. Find substring and replace
    def find_and_replace(self):
        try:
            old = input("Enter substring to find: ")
            if old in self.s:
                new = input("Enter new substring to replace: ")
                self.s = self.s.replace(old, new)
                print("Updated String:", self.s)
            else:
                print("Substring NOT found.")
        except Exception as e:
            print("Error:", e)

    # j. Check palindrome
    def check_palindrome(self):
        try:
            if self.s == self.s[::-1]:
                print("String is a PALINDROME.")
            else:
                print("String is NOT a palindrome.")
        except Exception as e:
            print("Error:", e)


# ---------------- MAIN MENU ----------------
def main():
    obj = StringOperations()

    while True:
        print("\n----- MENU -----")
        print("1. Take Input String")
        print("2. Check Substring")
        print("3. Count Consonants")
        print("4. Check Lowercase & Convert")
        print("5. Check Digit")
        print("6. Count Character Occurrence")
        print("7. Find String Length (without len())")
        print("8. Reverse String")
        print("9. Find & Replace Substring")
        print("10. Check Palindrome")
        print("11. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except:
            print("Invalid input! Enter a number.")
            continue
                
        if choice == 1:
            obj.take_input()
        elif choice == 2:
            obj.check_substring()
        elif choice == 3:
            obj.count_consonants()
        elif choice == 4:
            obj.check_lower()
        elif choice == 5:
            obj.check_digit()
        elif choice == 6:
            obj.count_character()
        elif choice == 7:
            obj.find_length()
        elif choice == 8:
            obj.reverse_string()
        elif choice == 9:
            obj.find_and_replace()
        elif choice == 10:
            obj.check_palindrome()
        elif choice == 11:
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid Choice! Try again.")

# Run the program
main()