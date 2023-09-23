# Define an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added successfully!")

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks to display.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Function to remove a task by index
def remove_task():
    view_tasks()
    try:
        index = int(input("Enter the number of the task to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"Task '{removed_task}' removed successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

# Main loop
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please select a valid option.")
