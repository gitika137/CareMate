from models import Task
from analytics import completed_tasks, total_expenses, pending_reminders


def test_task():
    task = Task("Math homework", "Maths", "High")

    assert task.name == "Math homework"
    assert task.subject == "Maths"
    assert task.priority == "High"
    assert task.completed == False

    task.complete()

    assert task.completed == True
    print("Task test passed")


def test_expenses():
    expenses = [
        {"amount": 100, "category": "Food"},
        {"amount": 50, "category": "Travel"}
    ]

    assert total_expenses(expenses) == 150
    print("Expense test passed")


def test_completed_tasks():
    tasks = [
        Task("Math homework", "Maths", "High"),
        Task("Python work", "Python", "Medium")
    ]

    tasks[0].complete()

    assert completed_tasks(tasks) == 1
    print("Completed task test passed")


def test_reminders():
    care = [
        {"title": "Drink water", "day": "Monday", "done": False},
        {"title": "Submit assignment", "day": "Tuesday", "done": True}
    ]

    assert pending_reminders(care) == 1
    print("Reminder test passed")


test_task()
test_expenses()
test_completed_tasks()
test_reminders()

print("All tests passed!")