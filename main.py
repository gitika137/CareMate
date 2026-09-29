from taskmanager import task_menu
from expensemanager import expense_menu
from periodtracker import period_menu
from caremanager import care_menu
from dashboard import show_dashboard


def main():

    print("------------------------------")
    print("          CAREMATE")
    print("     Student Life Helper")
    print("------------------------------")

    p = input("Do you want to use Period Tracker? (y/n): ").lower()

    if p == "y":
        period = True
    else:
        period = False

    tasks = []
    expenses = []
    periods = []
    care = []

    while True:

        print("\n---------- MENU ----------")
        print("1. Tasks")
        print("2. Expenses")

        if period:
            print("3. Period Tracker")
            print("4. Care Reminders")
            print("5. Dashboard")
            print("6. Exit")
        else:
            print("3. Care Reminders")
            print("4. Dashboard")
            print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            task_menu(tasks)

        elif choice == "2":
            expense_menu(expenses)

        elif choice == "3" and period:
            period_menu(periods)

        elif choice == "4" and period:
            care_menu(care)

        elif choice == "5" and period:
            show_dashboard(tasks, expenses, periods, care)

        elif choice == "3" and not period:
            care_menu(care)

        elif choice == "4" and not period:
            show_dashboard(tasks, expenses, periods, care)

        elif (choice == "6" and period) or (choice == "5" and not period):
            print("Thank you for using CareMate!")
            break

        else:
            print("Wrong choice. Try again.")


main()