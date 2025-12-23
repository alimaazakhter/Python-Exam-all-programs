class StringOperations:

    def input_string(self):
        try:
            self.s = input("Enter a string: ")
            print("String is:", self.s)
        except Exception as e:
            print("Error:", e)

    def check_substring(self):
        try:
            sub = input("Enter substring to check: ")
            if sub in self.s:
                print("Substring exists in main string")
            else:
                print("Substring does not exist")
        except Exception as e:
            print("Error:", e)

    def count_consonants(self):
        try:
            count = 0
            for ch in self.s.lower():
                if ch.isalpha() and ch not in "aeiou":
                    count += 1
            print("Number of consonants:", count)
        except Exception as e:
            print("Error:", e)

    def lowercase_to_uppercase(self):
        try:
            if self.s.islower():
                print("String is in lowercase")
                print("Uppercase string:", self.s.upper())
            else:
                print("String is not completely lowercase")
        except Exception as e:
            print("Error:", e)

    def check_digit(self):
        try:
            if self.s.isdigit():
                print("String contains only digits")
            else:
                print("String does not contain only digits")
        except Exception as e:
            print("Error:", e)

    def count_character(self):
        try:
            ch = input("Enter a character to count: ")
            count = 0
            for c in self.s:
                if c == ch:
                    count += 1
            print(f"Character '{ch}' repeated {count} times")
        except Exception as e:
            print("Error:", e)

    def find_length(self):
        try:
            length = 0
            for _ in self.s:
                length += 1
            print("Length of string:", length)
        except Exception as e:
            print("Error:", e)

    def reverse_string(self):
        try:
            rev = ""
            for ch in self.s:
                rev = ch + rev
            print("Reverse string:", rev)
        except Exception as e:
            print("Error:", e)

    def replace_substring(self):
        try:
            old = input("Enter substring to replace: ")
            new = input("Enter new substring: ")
            if old in self.s:
                self.s = self.s.replace(old, new)
                print("Updated string:", self.s)
            else:
                print("Substring not found")
        except Exception as e:
            print("Error:", e)

    def check_palindrome(self):
        try:
            rev = self.s[::-1]
            if self.s == rev:
                print("String is Palindrome")
            else:
                print("String is not Palindrome")
        except Exception as e:
            print("Error:", e)


# -------- Main Program --------
def main():
    obj = StringOperations()

    while True:
        print("\n------ MENU ------")
        print("1. Input and display string")
        print("2. Check substring")
        print("3. Count consonants")
        print("4. Lowercase to Uppercase")
        print("5. Check digit string")
        print("6. Count character repetition")
        print("7. Find length without len()")
        print("8. Reverse string")
        print("9. Replace substring")
        print("10. Check palindrome")
        print("11. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except:
            print("Invalid input! Enter a number.")
            continue

        if choice == 1:
            obj.input_string()
        elif choice == 2:
            obj.check_substring()
        elif choice == 3:
            obj.count_consonants()
        elif choice == 4:
            obj.lowercase_to_uppercase()
        elif choice == 5:
            obj.check_digit()
        elif choice == 6:
            obj.count_character()
        elif choice == 7:
            obj.find_length()
        elif choice == 8:
            obj.reverse_string()
        elif choice == 9:
            obj.replace_substring()
        elif choice == 10:
            obj.check_palindrome()
        elif choice == 11:
            print("Program Exit... Thank You 😊")
            break
        else:
            print("Invalid choice, try again")


# Run the program
main()
1
