import os

FileName = "tasks.txt"

def load_tasks():
    if not os.path.exists(FileName):
        return []
    with open(FileName, "r") as file:
        return [line.strip() for line in file.readlines()]
    

def add_task(tasks):
    task = input("Enter your task: ").strip()
    if not task:
        print("Write something!")
    else:
        tasks.append(task)
        print("Task added successfully.\n")
        
        
def show_task(tasks):
    if not tasks:
        print("There are no tasks.")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
                
                
def save_task(tasks):
    with open(FileName, "w") as file:
        for task in tasks:
            file.write(task + "\n")
  

def delete_task(tasks):
    if not tasks:
        print("There is no task to delete.")
        return

    show_task(tasks)
    try:
        index = int(input("Enter the number of the task you want to delete: "))
        if 1 <= index <= len(tasks):
            removed_task = tasks.pop(index - 1)
            print(f"'{removed_task}' has been removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number!")
        
        
def main():
    tasks = load_tasks()
    
    while True:
        print("\n1. Add task")
        print("2. Show task")
        print("3. Save task")
        print("4. Delete task")
        print("5. Exit\n")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_task(tasks)
        elif choice == "3":
            save_task(tasks)
            print("Tasks saved successfully.")
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Wrong choice")

if __name__ == "__main__":
    main()
