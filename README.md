# CLI Task Manager

A simple and efficient Command Line Interface (CLI) Task Manager built with Python. This tool allows users to manage their daily tasks directly from the terminal with features like adding, listing, deleting, and updating task statuses.

## 🚀 Features

- **Add Tasks**: Quickly add new tasks with a name, description, and due date.
- **List Tasks**: View all your tasks in a clean, formatted grid.
- **Update Status**: Easily toggle task statuses between "Pending" and "Completed".
- **Delete Tasks**: Remove tasks you no longer need.
- **Data Persistence**: All tasks are saved in a `task.json` file, so your data persists across sessions.

## 🛠️ Prerequisites

To run this project, you need to have Python installed on your system along with the following libraries:

- `pandas`: For data handling.
- `tabulate`: For beautiful terminal tables.

You can install the dependencies using pip:

```bash
pip install pandas tabulate
```

## 📂 Project Structure

- `main.py`: The entry point for the CLI application.
- `task_function.py`: Contains the core logic for task management (CRUD operations).
- `task.json`: Stores the task data in JSON format.

## 🏁 Getting Started

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd CLI-Task-Manager
   ```

2. **Run the application**:
   ```bash
   python main.py
   ```

## 📖 Usage

Once the application is running, follow the on-screen prompts:

- Type `list` to see all current tasks.
- Type `add` to create a new task.
- Type `status` to change a task's progress.
- Type `delete` to remove a task by its ID.
- Type `exit` to close the application.

---
Built with ❤️ for better productivity!