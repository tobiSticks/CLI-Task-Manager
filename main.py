import task_function as tf


def main():
    while True:
        print("\n--- TASK MANAGER ---")
        command = input("Choose: list, add, delete, status, or exit: ").lower()

        if command == "exit":
            break

        elif command == "list":
            tf.list_tasks()

        elif command == "add":
            t_id = input("ID: ")
            name = input("Name: ")
            desc = input("Description: ")
            date = input("Due Date: ")
            status = "pending"  # Default for new tasks

            details = {
                "task_name": name,
                "description": desc,
                "due_date": date,
                "status": status
            }
            tf.add_or_update(t_id, details)
            print("Task added!")

        elif command == "delete":
            t_id = input("Task ID number to delete: ")
            if tf.delete_task(t_id):
                print(f"Task {t_id} deleted.")
            else:
                print("Task not found.")

        elif command == "status":
            tf.status_update()

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()