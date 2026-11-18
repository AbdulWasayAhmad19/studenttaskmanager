
tasks = []

def add_task():
    title = input("Enter task title: ")
    tasks.append({"title": title, "completed": False})
    print("Task added successfully!")

def display_tasks():
    if not tasks:
        print("No tasks available.")
        return

    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(i, task["title"], "-", status)
        
        
def complete_task():
    display_tasks()

    try:
        task_id = int(input("Enter task ID to complete: "))

        if 1 <= task_id <= len(tasks):
            tasks[task_id - 1]["completed"] = True
            print(f"Task {task_id} marked as completed!")
        else:
            print("Invalid task ID!")

    except ValueError:
        print("Please enter a valid number!")

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
            complete_task()
        elif choice == "4":
         break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
