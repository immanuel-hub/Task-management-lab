from datetime import datetime

tasks = []


def validate_task_title(title):
    if len(title.strip()) == 0:
        raise ValueError("Title cannot be empty.")
    if len(title.strip()) < 3:
        raise ValueError("Title must be at least 3 characters long.")
    if len(title.strip()) > 100:
        raise ValueError("Title cannot exceed 100 characters.")
    return title.strip()


def validate_task_description(description):
    if len(description.strip()) == 0:
        raise ValueError("Description cannot be empty.")
    if len(description.strip()) > 500:
        raise ValueError("Description cannot exceed 500 characters.")
    return description.strip()


def validate_due_date(due_date):
    if len(due_date.strip()) == 0:
        raise ValueError("Due date cannot be empty.")
    try:
        parsed_date = datetime.strptime(due_date.strip(), "%Y-%m-%d")
    except ValueError:
        raise ValueError("Due date must be in YYYY-MM-DD format (e.g. 2026-12-31).")
    return due_date.strip()


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
    print("Task added successfully!")


def mark_task_as_complete(title):
    found = False

    try:
        index = int(title.strip()) - 1
        if 0 <= index < len(tasks):
            task = tasks[index]
            found = True
            if task["completed"] == True:
                print("Task '" + task["title"] + "' is already marked as complete.")
            else:
                task["completed"] = True
                print("Task marked as complete!")
    except ValueError:
        for task in tasks:
            if task["title"].lower() == title.strip().lower():
                found = True
                if task["completed"] == True:
                    print("Task '" + task["title"] + "' is already marked as complete.")
                else:
                    task["completed"] = True
                    print("Task marked as complete!")
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


def print_menu():
    print("\n========================================")
    print("       Task Management System")
    print("========================================")
    print("1. Add Task")
    print("2. Mark Task as Complete")
    print("3. View Pending Tasks")
    print("4. Track Progress")
    print("5. Exit")
    print("========================================")


def main():
    print("Welcome to the Task Management System!")

    while True:
        print_menu()
        choice = input("Select an option (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            try:
                add_task(title, description, due_date)
            except ValueError as e:
                print("Error: " + str(e))

        elif choice == "2":
            title = input("Enter the title of the task to mark as complete: ")
            mark_task_as_complete(title)

        elif choice == "3":
            view_pending_tasks()

        elif choice == "4":
            calculate_progress()

        elif choice == "5":
            print("Goodbye! See you next time.")
            break

        else:
            print("Invalid option. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
