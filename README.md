# To-Do List CLI App (Python)

A simple command-line To-Do List application written in Python. This program allows users to **add, view, edit, delete, and mark tasks as completed**, with all data saved to a file so tasks persist between sessions.

* * *

## Features

-   Add new tasks
-   View all tasks with numbered list and status indicators (`[ ]` / `[X]`)
-   Edit existing tasks
-   Delete tasks
-   Mark tasks as done / undone (toggle)
-   Input validation (prevents invalid selections)
-   Persistent storage using a JSON file
-   Automatic saving after every change

* * *

## How It Works

1.  On startup, the program checks if a task file (`tasks.json`) exists.
2.  If it exists, tasks are loaded into memory.
3.  The user is presented with a menu:
    -   **1** → Add task
    -   **2** → View / Edit / Delete tasks
    -   **3** → Mark done / undone
    -   **0** → Exit
4.  When viewing tasks:
    -   Tasks are displayed with numbers and completion status
    -   User selects a task
    -   Then chooses to:
        -   Edit the task
        -   Delete the task
        -   Cancel
5.  All changes are automatically saved to the file.

* * *

## Data Storage

Tasks are stored in a JSON file:

    [{"task": "Buy milk", "done": false},{"task": "Study Python", "done": true}]

Each task is stored as a dictionary with:

-   `"task"` → task description
-   `"done"` → completion status (true/false)

* * *

## How to Run

Run the program from the terminal:

    python main.py

* * *

## Concepts Used

-   Functions and modular design
-   Loops and control flow
-   Input validation
-   File I/O (JSON read/write)
-   Lists and dictionaries
-   Boolean logic (state toggling)

* * *

## Author

Built as part of learning Python fundamentals and progressing into intermediate-level programming.
