# Task Management Module

tasks = []

def create_task():
    task = input("Enter Task Name: ")
    tasks.append(task)
    print("Task Created Successfully!")

def view_tasks():
    print("===== TASK LIST =====")
    if not tasks:
        print("No Tasks Available")
    else:
        for i, task in enumerate(tasks, 1):
            print(i, task)

def manage_tasks():
    print("===== TASK MANAGEMENT =====")
    print("1. Create Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        print("Exiting Task Module")
    else:
        print("Invalid Choice")

manage_tasks()