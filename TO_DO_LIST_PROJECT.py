todo=[]

def view_task():
    """Display all tasks with their statuses."""
    print("hi")
    if not todo:
        return print("No Task pending.")
    print("\n Your Tasks:")
    for index,task in enumerate(todo,start=1):
        status = "✔️" if task["done"] else "⏳"
        # print(f"{index}.{task}")
        print(f"{index}. {task['task']} [{status}]")
def add_task():
    """Add a new task to the list."""
    task = input("Enter the task description: ")
    todo.append({'task':task,'done':False})
    print(f"Task '{task}' added.") 

# Mark a task as done
def mark_done():
    """Mark a task as completed."""
    view_task()
    try:
        task_number = int(input("Enter the task number to mark as complete: "))
        # if 1<=task_number <= len(todo):
        todo[task_number - 1] = "[Completed] " + todo[task_number - 1]
        print(f"Task {task_number} marked as completed.")
    
    except (ValueError, IndexError):
        print("Invalid task number.")
        
def delete_task():
     view_task()
     try:
          task_number= int(input("Enter task number to delete:"))
          if 1<= task_number <= len(todo):
               removed=todo.pop(task_number-1)
               print(f"Deleted:{removed['task']}")
          else:
               print("Invalid Number.") 
     except: 
          print("Please enter valid number.")

# Main menu
def main():
    while True:
        print("\n--- To-Do List Manager ---")
        print("\t1. View Tasks")
        print("\t2. Add Task")
        print("\t3. Mark Task as Done")
        print("\t4. Delete Task")
        print("\t5. Exit")
        choice = int(input("Enter your choice(1-5): "))
        if choice == 1:
             print("Hi")
             view_task()
        elif choice ==2:
            task = input("Enter the task: ")
            add_task()
        elif choice == 3:
             mark_done()
             try:
                    task_number = int(input("Enter task number to mark as done: "))
                    mark_done(task_number)
             except ValueError:
                    print("Please enter a valid number!")
        elif choice == 4:
                delete_task()
                try:
                    task_number = int(input("Enter task number to delete: "))
                    delete_task(task_number)
                except ValueError:
                    print("Please enter a valid number!")
        elif choice == 5:
                print("Goodbye!")
                # break
        else:
                print("Invalid choice! Please try again.")
if __name__ == "__main__":
    main()




