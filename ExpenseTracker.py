import csv
import os

FILE_NAME = "expenses.csv"

# Create file if not exists
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Description", "Amount"])

# Add expense
def add_expense():
    desc = input("Enter expense description: ")
    amount = input("Enter amount: ")

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([desc, amount])

    print("✅ Expense added successfully!\n")

# View all expenses
def view_expenses():
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # skip header

        print("\n📋 All Expenses:")
        for row in reader:
            print(f"{row[0]} - ₹{row[1]}")
        print()

# Calculate total
def calculate_total():
    total = 0

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            total += float(row[1])

    print(f"\n💰 Total Spent: ₹{total}\n")

# Main menu
def menu():
    initialize_file()

    while True:
        print("==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Spent")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            calculate_total()
        elif choice == '4':
            print("👋 Exiting... Bye!")
            break
        else:
            print("❌ Invalid choice, try again.\n")

# Run program
menu()
