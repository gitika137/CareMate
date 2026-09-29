from analytics import completed_tasks
from analytics import total_expenses
from analytics import pending_reminders


def show_dashboard(tasks, expenses, periods, care):

    print("\n==========", "DASHBOARD", "="*10)

    completed = completed_tasks(tasks)

    print("Tasks completed:", completed, "/", len(tasks))

    print("Total expenses: Rs.",
          total_expenses(expenses))

    print("Pending care reminders:",
          pending_reminders(care))

    if len(periods) > 0:
        print("Last period recorded:",
              periods[-1]["start_date"])
    else:
        print("No period record.")

    print("="*30)