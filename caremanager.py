def add_reminder(care):
    title = input("Reminder: ")
    day = input("Day / date: ")

    reminder = {
        "title": title,
        "day": day,
        "done": False
    }

    care.append(reminder)

    print("Reminder added.")


def view_reminders(care):
    if len(care) == 0:
        print("No reminders.")
        return

    print("\n----- CARE REMINDERS -----")

    for i in range(len(care)):
        reminder = care[i]

        if reminder["done"]:
            status = "Done"
        else:
            status = "Pending"

        print(i + 1, ".", reminder["title"],
              "-", reminder["day"],
              "-", status)


def complete_reminder(care):
    view_reminders(care)

    if len(care) > 0:
        number = int(input("Enter reminder number: "))

        if number >= 1 and number <= len(care):
            care[number - 1]["done"] = True
            print("Reminder completed.")
        else:
            print("Invalid reminder number.")


def care_menu(care):
    while True:
        print("\n----- CARE REMINDERS -----")
        print("1. Add Reminder")
        print("2. View Reminders")
        print("3. Complete Reminder")
        print("4. Back")

        choice = input("Choose: ")

        if choice == "1":
            add_reminder(care)

        elif choice == "2":
            view_reminders(care)

        elif choice == "3":
            complete_reminder(care)

        elif choice == "4":
            break

        else:
            print("Invalid choice.")