import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file. Create it if it doesn't exist."""
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_tasks(tasks):
    """Write the list of tasks to the JSON file."""
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

def main():
    tasks = load_tasks()
    
    while True:
        print(f"\n--- TODO LIST (Saved in {FILE_NAME}) ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            item = input("Enter the task: ")
            tasks.append(item)
            save_tasks(tasks)
            print("✓ Task saved!")
        elif choice == '2':
            print("\nYOUR TASKS:")
            if not tasks:
                print("[No tasks found]")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
        elif choice == '3':
            print("Exiting... your tasks are safe!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()