from models import Task


def add_task(tasks):
    name = input("Task name: ")
    subject = input("Subject: ")
    priority = input("Priority (High/Medium/Low): ")

    task = Task(name, subject, priority)

    tasks.append(task)
    print("Task added.")


def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks added.")
        return

    print("\n----- TASKS -----")

    for i in range(len(tasks)):
        task = tasks[i]

        if task.completed:
            status = "Done"
        else:
            status = "Pending"

        print(i + 1, ".", task.name,
              "|", task.subject,
              "|", task.priority,
              "|", status)


def complete_task(tasks):
    view_tasks(tasks)

    if len(tasks) > 0:
        number = int(input("Enter task number to complete: "))

        if number >= 1 and number <= len(tasks):
            tasks[number - 1].complete()
            print("Task marked as complete.")
        else:
            print("Invalid task number.")


def task_menu(tasks):
    while True:
        print("\n----- TASK MANAGER -----")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Back")

        choice = input("Choose: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            break

        else:
            print("Invalid choice.")