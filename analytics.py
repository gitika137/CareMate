def completed_tasks(tasks):
    count = 0

    for task in tasks:
        if task.completed:
            count = count + 1

    return count


def total_expenses(expenses):
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    return total


def pending_reminders(care):
    count = 0

    for reminder in care:
        if not reminder["done"]:
            count = count + 1

    return count