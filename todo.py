tasks = []

def show_menu():
    print("\n--- TODO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == '1':
        item = input("What do you need to do? ")
        tasks.append(item)
        print("Task added!")
    elif choice == '2':
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")