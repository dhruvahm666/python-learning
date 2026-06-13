# Final Project: To-Do List Manager
# Step 1: Basic menu and adding tasks

tasks = []  # This will store all your tasks

def show_menu():
    print("\n📝 MY TO-DO LIST")
    print("================")
    print("1. Add new task")
    print("2. View all tasks")
    print("3. Delete a task")
    print("4. Save & Exit")
    print()

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print(f"✓ Task added: {task}")

# Main program loop
while True:
    show_menu()
    choice = input("Choose an option (1-4): ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        print("\nYour tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    elif choice == "3":
        print("Delete feature coming in Step 2!")
    elif choice == "4":
        print("Saving... (coming in Step 2)")
        print("Goodbye! 👋")
        break
    else:
        print("Invalid option! Please choose 1-4.")
        