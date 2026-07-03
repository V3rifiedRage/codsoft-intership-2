todo = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        todo.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(todo) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(todo, start=1):
                print(i, ".", task)

    elif choice == "3":
        if len(todo) == 0:
            print("No tasks to remove.")
        else:
            for i, task in enumerate(todo, start=1):
                print(i, ".", task)
            n = int(input("Enter task number to remove: "))
            if 1 <= n <= len(todo):
                removed = todo.pop(n - 1)
                print(removed, "removed successfully!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
 
