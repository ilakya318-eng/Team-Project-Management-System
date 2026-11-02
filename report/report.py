# Project Report Module

def generate_report():
    print("===== PROJECT REPORT =====")
    print("1. Total Tasks")
    print("2. Completed Tasks")
    print("3. Pending Tasks")
    print("4. Back to Dashboard")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Total Tasks: 10")
    elif choice == "2":
        print("Completed Tasks: 6")
    elif choice == "3":
        print("Pending Tasks: 4")
    elif choice == "4":
        print("Returning to Dashboard")
    else:
        print("Invalid Choice")

generate_report()