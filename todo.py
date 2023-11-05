class Task:
    def __init__(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

tasks = []
completed_tasks = []

def add_task(description, due_date, priority):
    task = Task(description, due_date, priority)
    tasks.append(task)

def display_tasks():
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task.description} (Due: {task.due_date}, Priority: {task.priority}, Completed: {task.completed})")

def mark_task_as_completed(task_index):
    if 0 <= task_index < len(tasks):
        task = tasks[task_index]
        task.completed = True
        completed_tasks.append(task)
        del tasks[task_index]

def update_task(task_index, description, due_date, priority):
    if 0 <= task_index < len(tasks):
        task = tasks[task_index]
        task.description = description
        task.due_date = due_date
        task.priority = priority

def remove_task(task_index):
    if 0 <= task_index < len(tasks):
        del tasks[task_index]

while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Mark Task as Completed")
    print("4. Update Task")
    print("5. Remove Task")
    print("6. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        description = input("Enter task description: ")
        due_date = input("Enter due date: ")
        priority = input("Enter priority: ")
        add_task(description, due_date, priority)
    elif choice == "2":
        display_tasks()
    elif choice == "3":
        task_index = int(input("Enter the task number to mark as completed: ")) - 1
        mark_task_as_completed(task_index)
    elif choice == "4":
        task_index = int(input("Enter the task number to update: ")) - 1
        description = input("Enter updated description: ")
        due_date = input("Enter updated due date: ")
        priority = input("Enter updated priority: ")
        update_task(task_index, description, due_date, priority)
    elif choice == "5":
        task_index = int(input("Enter the task number to remove: ")) - 1
        remove_task(task_index)
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")

print("Goodbye!")
