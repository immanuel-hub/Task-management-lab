import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress


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
