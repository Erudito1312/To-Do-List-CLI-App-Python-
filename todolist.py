import os


def menu():
    print()
    print("1. Add task")
    print("2. View tasks")
    print("3. Exit")
    print()
    choice = input("Enter your choice: ")
    while choice not in ('1', '2', '3'):
        print("Please enter 1, 2 or 3")
        choice = input("Enter your choice: ")
    return int(choice)


def save_tasks(tasks):
    tasklistfile = 'Tasks.txt'
    with open(tasklistfile, 'w') as tasklist:
        content = '\n'.join(tasks)
        tasklist.write(content)


def taskfunc(tasks):
    for n, i in enumerate(tasks, 1):
        print(f"{n}. {i}")


tasklistfile = 'Tasks.txt'
tasks = []

if os.path.isfile(tasklistfile):
    with open(tasklistfile, 'r') as tasklist:
        content = tasklist.read()
        for entry in content.split('\n'):
            entry = entry.strip()
            if entry != '':
                tasks.append(entry)


while True:
    choice = menu()

    if choice == 1:
        newtask = input("Enter new task: ")
        tasks.append(newtask)
        save_tasks(tasks)
        print()

    elif choice == 2:
        print()

        if len(tasks) == 0:
            print("No tasks yet\n")

        else:
            taskfunc(tasks)
            print()

            taskchoice = input("Type a number to edit task, or 0 to exit: ")
            while not taskchoice.isnumeric():
                taskchoice = input("Type a number to edit task, or 0 to exit: ")

            if taskchoice == '0':
                continue
            else:
                taskchoice = int(taskchoice)

                while taskchoice > len(tasks) or taskchoice < 1:
                    print("\nInvalid task")
                    taskfunc(tasks)
                    print()
                    taskchoice = input("Type a number to edit task, or 0 to exit: ")
                    while not taskchoice.isnumeric():
                        taskchoice = input("Type a number to edit task, or 0 to exit: ")
                    taskchoice = int(taskchoice)

                taskaction = input("Type 1 to edit task, 2 to delete task, or 0 to exit: ")
                while taskaction not in ('1', '2', '0'):
                    print('\nInvalid option')
                    taskaction = input("Type 1 to edit task, 2 to delete task, or 0 to exit: ")

                if taskaction == '1':
                    tasks[taskchoice - 1] = input('Enter new task')
                    save_tasks(tasks)
                    taskfunc(tasks)
                    print()

                elif taskaction == '2':
                    print("")
                    print(f"\nDeleting task {tasks[taskchoice - 1]}")
                    tasks.pop(taskchoice - 1)
                    save_tasks(tasks)
                    taskfunc(tasks)
                    print()

                elif taskaction == '0':
                    print()

    elif choice == 3:
        print("\nExiting")
        break