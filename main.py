
tasks = []

def add_task():
    title = input("Enter task title: ").strip()

    if not title:
        print("Error: Task title cannot be empty!")
        return

    tasks.append({"title": title, "completed": False})
    print(f"Task '{title}' added successfully!")

def display_tasks():
    if not tasks:
        print("No tasks available.")
        return

    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(i, task["title"], "-", status)

def main():
    while True:
        print("\n1. Add Task")
        print("2. Display Tasks")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            display_tasks()
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
