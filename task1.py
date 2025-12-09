tasks = []

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter new task: ")
    tasks.append({"task": task, "done": False})
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, t in enumerate(tasks, 1):
            status = "✔" if t["done"] else "✘"
            print(f"{i}. {t['task']} [{status}]")

def update_task():
    view_tasks()
    n = int(input("Enter task number to mark complete: "))
    if 1 <= n <= len(tasks):
        tasks[n-1]["done"] = True
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    n = int(input("Enter task number to delete: "))
    if 1 <= n <= len(tasks):
        tasks.pop(n-1)
        print("Task deleted.")
    else:
        print("Invalid task number.")

while True:
    show_menu()
    choice = input("Enter choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")
