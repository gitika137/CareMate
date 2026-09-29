def add_expense(expenses):
    amount = float(input("Amount: "))
    category = input("Category: ")

    expense = {
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    print("Expense added.")


def view_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses added.")
        return

    print("\n----- EXPENSES -----")

    total = 0

    for expense in expenses:
        print("Rs.", expense["amount"],
              "-", expense["category"])

        total = total + expense["amount"]

    print("--------------------")
    print("Total spending: Rs.", total)


def expense_menu(expenses):
    while True:
        print("\n----- EXPENSE MANAGER -----")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Back")

        choice = input("Choose: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            break

        else:
            print("Invalid choice.")