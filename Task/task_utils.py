import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from validation import validate_task_title, validate_task_description, validate_due_date

tasks = []


def add_task(title, description, due_date):
    valid_title = validate_task_title(title)
    valid_description = validate_task_description(description)
    valid_due_date = validate_due_date(due_date)

    task = {
        "title": valid_title,
        "description": valid_description,
        "due_date": valid_due_date,
        "completed": False
    }

    tasks.append(task)
    print("Task '" + task["title"] + "' added successfully!")


def mark_task_as_complete(title):
    found = False

    for task in tasks:
        if task["title"].lower() == title.strip().lower():
            found = True
            if task["completed"] == True:
                print("Task '" + task["title"] + "' is already marked as complete.")
            else:
                task["completed"] = True
                print("Task '" + task["title"] + "' has been marked as complete.")
            break

    if found == False:
        print("No task found with the title '" + title + "'.")


def view_pending_tasks():
    pending_tasks = []

    for task in tasks:
        if task["completed"] == False:
            pending_tasks.append(task)

    if len(pending_tasks) == 0:
        print("There are no pending tasks.")
    else:
        print("\n---------- Pending Tasks ----------")
        count = 1
        for task in pending_tasks:
            print(str(count) + ". " + task["title"])
            print("   Description: " + task["description"])
            print("   Due Date: " + task["due_date"])
            count = count + 1
        print("-----------------------------------")


def calculate_progress():
    total = len(tasks)

    if total == 0:
        print("No tasks have been added yet.")
        return

    completed_count = 0
    for task in tasks:
        if task["completed"] == True:
            completed_count = completed_count + 1

    percent = (completed_count / total) * 100
    print("\n--- Progress ---")
    print("Completed: " + str(completed_count) + " out of " + str(total) + " tasks")
    print("Progress: " + str(round(percent, 1)) + "%")

    filled = int(percent // 5)
    bar = "[" + "#" * filled + "." * (20 - filled) + "]"
    print(bar)
