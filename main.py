import json
import os

def menu():
    print()
    print("1. Add task")
    print("2. View/delete tasks")
    print("3. Mark done/undone")
    print("0. Exit")
    print()
    choice = input("Enter your choice: ")
    while choice not in ('1','2','3','0'):
        print("Please enter 1, 2, 3 or 0")
        choice = input("Enter your choice: ")
    return int(choice)

def save_tasks(tasks):
    tasklistfile = 'tasks.json'
    with open(tasklistfile, 'w') as tasklist:
        json.dump(tasks, tasklist, indent=4)

def taskfunc(tasks):
    checkmark = '[X]'
    nomark = '[ ]'
    print(' --- TASK LIST --- ')
    for n, i in enumerate(tasks, 1):
        thistask = i['task']
        if i['done']:

            print(f"{n}. {checkmark} {thistask}")
        else:
            print(f"{n}. {nomark} {thistask}")

tasklistfile = 'tasks.json'
tasks = []

if os.path.isfile(tasklistfile):
    try:
        with open(tasklistfile, 'r') as tasklist:
            tasks = json.load(tasklist)
    except:
        tasks = []

while True:
    choice = menu()
    if choice == 1:
        newtask = input("Enter new task: ")
        taskentry = {"task" : newtask, "done" : False}
        tasks.append(taskentry)
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
                    newtask = input("Enter new task: ")
                    tasks[taskchoice-1]["task"] = newtask
                    print('Task updated')
                    save_tasks(tasks)
                    taskfunc(tasks)
                    print()
                elif taskaction == '2':
                    print("")
                    print(f"\nDeleting task {tasks[taskchoice-1]['task']}")
                    tasks.pop(taskchoice-1)
                    print('Task deleted')
                    save_tasks(tasks)
                    taskfunc(tasks)
                    print()
                elif taskaction == '0':
                    print()

    elif choice == 3:
        print()
        if len(tasks) == 0:
            print("No tasks yet\n")
        else:
            taskfunc(tasks)
            print()

            taskdone = input("Enter task's number to change its status, or 0 to exit: ")
            while not taskdone.isnumeric():
                taskdone = input("Enter task's number to change its status, or 0 to exit: ")
            if taskdone == '0':
                continue
            else:
                taskdone = int(taskdone)
                while taskdone > len(tasks) or taskdone < 1:
                    print("\nInvalid task")
                    taskfunc(tasks)
                    print()
                    taskdone = input("Enter task's number to change its status, or 0 to exit: ")
                    while not taskdone.isnumeric():
                        taskdone = input("Enter task's number to change its status, or 0 to exit: ")
                    taskdone = int(taskdone)
                tasks[taskdone-1]["done"] = not tasks[taskdone-1]["done"]
                save_tasks(tasks)
                taskfunc(tasks)
                print()

    elif choice == 0:
        print("\nExiting")
        break
