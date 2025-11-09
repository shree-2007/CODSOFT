# CodSoft Internship Task 1:TO-DO LIST Application 
# Name: Harinishree
# Domain: Python Programming
# Batch: [October to November batch B57]
# Description: A simple command-line To-Do List to add, view, update, and delete tasks.

import json
import os

FILENAME = "todo_data.json"

# Load existing tasks (if available)
def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Display all tasks
def show_tasks(tasks):
    print("\n📋 Your To-Do List:")
    if not tasks:
        print("No tasks yet! Use option 1 to add your first task.")
    else:
        for index, task in enumerate(tasks, start=1):
            status = "✅ Done" if task["completed"] else "🕓 Pending"
            print(f"{index}. {task['title']} — {status}")
    print("--------------------------------------------")

# Add a new task
def add_task(tasks):
    title = input("Enter task title: ").strip()
    if title:
        tasks.append({"title": title, "completed": False})
        print(f"✨ Task '{title}' added successfully!")
    else:
        print("⚠️ Task title cannot be empty!")

# Mark a task as completed
def complete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= index < len(tasks):
            if not tasks[index]["completed"]:
                tasks[index]["completed"] = True
                print(f"🎉 Task '{tasks[index]['title']}' marked as completed!")
            else:
                print("⚠️ Task already completed.")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

# Delete a task
def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"🗑️ Task '{removed['title']}' deleted successfully.")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

# Main menu
def main():
    tasks = load_tasks()
    while True:
        print("\n====== 🗒️ TO-DO LIST MENU ======")
        print("1️⃣  Add Task")
        print("2️⃣  View Tasks")
        print("3️⃣  Mark Task as Completed")
        print("4️⃣  Delete Task")
        print("5️⃣  Exit")
        print("===============================")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("\n💾 All changes saved successfully.")
            print("👋 Goodbye Harini! Stay organized and productive 💪")
            break
        else:
            print("⚠️ Invalid choice! Please enter a number between 1 and 5.")

        # Save after every action
        save_tasks(tasks)

# Run the program
if __name__ == "__main__":
    main()
