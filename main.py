
def add_task():
    title = input("Enter task title: ").strip()

    if not title:
        print("Error: Task title cannot be empty!")
        return

    tasks.append({"title": title, "completed": False})
    print(f"Task '{title}' added successfully!")
