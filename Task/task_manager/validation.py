from datetime import datetime


def validate_task_title(title):
    if title == "" or title.strip() == "":
        raise ValueError("Title cannot be empty.")
    if len(title.strip()) < 3:
        raise ValueError("Title must be at least 3 characters long.")
    if len(title.strip()) > 100:
        raise ValueError("Title cannot exceed 100 characters.")
    return title.strip()


def validate_task_description(description):
    if description == "" or description.strip() == "":
        raise ValueError("Description cannot be empty.")
    if len(description.strip()) > 500:
        raise ValueError("Description cannot exceed 500 characters.")
    return description.strip()


def validate_due_date(due_date):
    if due_date == "" or due_date.strip() == "":
        raise ValueError("Due date cannot be empty.")

    try:
        parsed_date = datetime.strptime(due_date.strip(), "%Y-%m-%d")
    except ValueError:
        raise ValueError("Due date must be in YYYY-MM-DD format (e.g. 2026-12-31).")

    today = datetime.today().date()
    if parsed_date.date() < today:
        raise ValueError("Due date cannot be in the past.")

    return due_date.strip()
