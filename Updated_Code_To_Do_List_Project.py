
# Simple CLI To-Do List Manager

todo = []  # Each item: {"task": str, "done": bool}

def view_tasks(todo_list):
    """Display all tasks with their statuses."""
    if not todo_list:
        print("No tasks pending.")
        return
    print("\nYour Tasks:")
    for index, task in enumerate(todo_list, start=1):
        status = "✔️" if task["done"] else "⏳"
        print(f"{index}. {task['task']} [{status}]")

def add_task(todo_list, task_description):
    """Add a new task to the list."""
    task_description = task_description.strip()
    if not task_description:
        print("Task description cannot be empty.")
        return
    todo_list.append({"task": task_description, "done": False})
    print(f"Task '{task_description}' added.")

def mark_done(todo_list, task_number):
    """Mark a task as completed by its 1-based number."""
    if 1 <= task_number <= len(todo_list):
        todo_list[task_number - 1]["done"] = True
        print(f"Task {task_number} marked as completed.")
    else:
        print("Invalid task number.")

def delete_task(todo_list, task_number):
    """Delete a task by its 1-based number."""
    if 1 <= task_number <= len(todo_list):
        removed = todo_list.pop(task_number - 1)
        print(f"Deleted: {removed['task']}")
    else:
        print("Invalid task number.")

def get_int(prompt):
    """Prompt until a valid integer is entered."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        print("\n--- To-Do List Manager ---")
        print("\t1. View Tasks")
        print("\t2. Add Task")
        print("\t3. Mark Task as Done")
        print("\t4. Delete Task")
        print("\t5. Exit")

        choice = get_int("Enter your choice (1-5): ")

        if choice == 1:
            view_tasks(todo)

        elif choice == 2:
            task = input("Enter the task description: ")
            add_task(todo, task)

        elif choice == 3:
            if not todo:
                print("No tasks to mark as done.")
                continue
            view_tasks(todo)
            task_number = get_int("Enter the task number to mark as done: ")
            mark_done(todo, task_number)

        elif choice == 4:
            if not todo:
                print("No tasks to delete.")
                continue
            view_tasks(todo)
            task_number = get_int("Enter the task number to delete: ")
            delete_task(todo, task_number)

        elif choice == 5:
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
