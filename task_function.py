import json
import os
import pandas as pd
from tabulate import tabulate

FILE_NAME = "task.json"


def load_data():
    """Helper function to load JSON data."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {"Tasks": {}}
    return {"Tasks": {}}


def save_data(data):
    """Helper function to save data to JSON."""
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)


def add_or_update(task_id, details):
    data = load_data()
    data["Tasks"][f"Task {task_id}"] = details
    save_data(data)


def delete_task(task_num):
    data = load_data()
    key = f"Task {task_num}"
    if key in data["Tasks"]:
        del data["Tasks"][key]
        save_data(data)
        return True
    return False


def list_tasks():
    data = load_data()
    tasks_dict = data.get("Tasks", {})
    if not tasks_dict:
        print("\nNo tasks to show!")
        return

    rows = []
    for tid, details in tasks_dict.items():
        row = details.copy()
        row["task_id"] = tid
        rows.append(row)

    
    print("\n" + tabulate(rows, headers="keys", tablefmt="grid"))

def status_update():
    with open("task.json", "r") as f:
        data = json.load(f)

    task_num = input("Change status for task ID number: ")
    task_key = f"Task {task_num}"

    if task_key in data["Tasks"]:
        current_status = data["Tasks"][task_key]["status"]
        print(f"Current status is: {current_status}")

        new_status = input("Enter new status (Pending/Completed): ")
        data["Tasks"][task_key]["status"] = new_status

        with open("task.json", "w") as f:
            json.dump(data, f, indent=4)
        print("Status updated successfully!")
    else:
        print(f"Sorry, {task_key} was not found.")
