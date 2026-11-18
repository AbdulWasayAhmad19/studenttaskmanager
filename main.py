
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
