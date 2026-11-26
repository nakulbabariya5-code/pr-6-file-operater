
from datetime import datetime

class Journal:

    def __init__(self):
        self.file = "journal.txt"

    def add_entry(self):
        entry = input("Write your journal: ")

        date = datetime.now().strftime("%d-%m-%Y %H:%M")

        try:
            f = open(self.file, "a")
            f.write(date + " : " + entry + "\n")
            f.close()

            print("Entry saved successfully!")

        except:
            print("Something went wrong while saving.")

    def view_entry(self):
        try:
            f = open(self.file, "r")
            data = f.read()
            f.close()

            if data == "":
                print("Journal is empty.")
            else:
                print("\nYour Journal:")
                print(data)

        except FileNotFoundError:
            print("No journal found. Add an entry first.")

  
    def search_entry(self):
        keyword = input("Enter word to search: ")

        try:
            f = open(self.file, "r")
            data = f.readlines()
            f.close()

            found = False

            for line in data:
                if keyword.lower() in line.lower():
                    print(line)
                    found = True

            if found == False:
                print("Entry not found.")

        except FileNotFoundError:
            print("Journal file not found.")

    def delete_entry(self):
        confirm = input("Do you want to delete all entries? (yes/no): ")

        if confirm.lower() == "yes":
            try:
                f = open(self.file, "w")
                f.close()

                print("All entries deleted.")

            except:
                print("Something went wrong.")

        else:
            print("Delete cancelled.")

    
    def menu(self):

        while True:
            print("\n===== PERSONAL JOURNAL =====")
            print("1. Add Entry")
            print("2. View Entries")
            print("3. Search Entry")
            print("4. Delete All Entries")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_entry()

            elif choice == "2":
                self.view_entry()

            elif choice == "3":
                self.search_entry()

            elif choice == "4":
                self.delete_entry()

            elif choice == "5":
                print("Thank you! Goodbye.")
                break

            else:
                print("Invalid choice. Try again.")



obj = Journal()


obj.menu()


