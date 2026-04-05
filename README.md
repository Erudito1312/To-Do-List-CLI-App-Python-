# To-Do List CLI App (Python)

A simple command-line To-Do List application written in Python. This program allows users to **add, view, edit, and delete tasks**, with all data saved to a file so tasks persist between sessions.

---

## Features

- Add new tasks
- View all tasks with numbered list
- Edit existing tasks
- Delete tasks
- Input validation (prevents invalid selections)
- Persistent storage using a text file
- Automatic saving after every change

---

## How It Works

1. On startup, the program checks if a task file (`Tasks.txt`) exists.
2. If it exists, tasks are loaded into memory.
3. The user is presented with a menu:
   - **1** → Add task
   - **2** → View / Edit / Delete tasks
   - **3** → Exit
4. When viewing tasks:
   - Tasks are displayed with numbers
   - User selects a task
   - Then chooses to:
     - Edit the task
     - Delete the task
     - Cancel
5. All changes are automatically saved to the file.

---

## Data Storage

Tasks are stored in a simple text file:

```
Buy milk
Study Python
Go to gym
```

Each line represents one task.

---

## How to Run

Run the program from the terminal:

```bash
python main.py
```

---

## Example Usage

```
1. Add task
2. View tasks
3. Exit

> 1
Enter new task: Buy milk

> 2
1. Buy milk

Type a number to edit task, or 0 to exit: 1
Type 1 to edit, 2 to delete, or 0 to exit: 1
Enter new task: Buy almond milk
```

---

## Concepts Used

- Functions and modular design
- Loops and control flow
- Input validation
- File I/O (read/write)
- Lists and indexing

---

## Future Improvements

- Mark tasks as completed (✔ / ✖)
- Use dictionaries for structured task data
- Store data in JSON format
- Add search and filtering
- Improve user interface

---

## Author

Built as part of learning Python fundamentals and progressing into intermediate-level programming.
