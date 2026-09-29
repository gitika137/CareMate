def add_period(periods):
    start_date = input("Period start date (DD/MM): ")
    cycle_length = int(input("Usual cycle length in days: "))

    period = {
        "start_date": start_date,
        "cycle_length": cycle_length
    }

    periods.append(period)

    print("Period record added.")


def view_periods(periods):
    if len(periods) == 0:
        print("No period records yet.")
        return

    print("\n----- PERIOD TRACKER -----")

    for period in periods:
        print("Start date:", period["start_date"])
        print("Cycle length:",
              period["cycle_length"], "days")
        print("Prediction is only an estimate.")
        print()


def period_menu(periods):
    while True:
        print("\n----- PERIOD TRACKER -----")
        print("1. Add Period Record")
        print("2. View Records")
        print("3. Back")

        choice = input("Choose: ")

        if choice == "1":
            add_period(periods)

        elif choice == "2":
            view_periods(periods)

        elif choice == "3":
            break

        else:
            print("Invalid choice.")