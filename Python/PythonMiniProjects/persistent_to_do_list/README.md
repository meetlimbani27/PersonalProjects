# Task Manager

This is a simple task manager program written in Python. It allows you to add, delete, mark tasks as complete, and retrieve a list of tasks from a file.

## Getting Started

To use the task manager, you'll need to have Python installed on your computer. You can download it from the [official Python website](https://www.python.org/downloads/).

## How to Use

1. **Run the Program**
   - Open a terminal or command prompt window.
   - Navigate to the directory where the `task_manager.py` file is located.
   - Run the program by typing `python task_manager.py` and pressing Enter.

2. **Menu Options**
   - Once the program is running, you'll see a menu with several options:
     - Retrieve previous tasks list
     - Add a new task
     - Delete a task
     - List all tasks
     - Mark task as complete
     - Quit

3. **Select an Option**
   - Enter the number corresponding to the action you want to perform.
   - You can enter `-1` at any time to return to the main menu.

4. **Adding Tasks**
   - To add a new task, select option `2`.
   - Enter the task when prompted. If you want to stop adding tasks, enter `-1`.

5. **Deleting Tasks**
   - To delete a task, select option `3`.
   - Enter the number of the task you want to delete. Enter `-1` to cancel.

6. **Marking Tasks as Complete**
   - To mark a task as complete, select option `5`.
   - Enter the number of the task you want to mark as complete. Enter `-1` to cancel.

7. **Viewing Tasks**
   - To view the current list of tasks, select option `4`.

8. **Saving Tasks**
   - Your tasks are automatically saved to a file named `tasks.txt` when you quit the program.

## Important Notes

- If you need to quit the program, select option `6`.
- Any tasks marked as complete will be prefixed with "COMPLETED:" in the task list.
- You can always restart the program to continue managing your tasks.
