import json
from pathlib import Path

DATA_FILE = Path("tasks.json")


def load_tasks():
    """Load saved tasks, or return an empty list if no file exists yet."""
    if not DATA_FILE.exists():
        return []
    try:
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        print("Could not read tasks.json. Starting with an empty task list.")
        return []


def save_tasks(tasks):
    """Save tasks to a JSON file."""
    DATA_FILE.write_text(json.dumps(tasks, indent=2), encoding="utf-8")


def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet. Add one to get started!")
        return
    print("\n--- Your Tasks ---")
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else " "
        print(f"{index}. [{status}] {task['title']}")


def add_task(tasks):
    title = input("Enter task: ").strip()
    if not title:
        print("Task cannot be empty.")
        return
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added!")


def complete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        number = int(input("Task number to mark complete: "))
        if not 1 <= number <= len(tasks):
            raise ValueError
    except ValueError:
        print("Please enter a valid task number.")
        return
    tasks[number - 1]["done"] = True
    save_tasks(tasks)
    print("Task marked complete!")


def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        number = int(input("Task number to delete: "))
        if not 1 <= number <= len(tasks):
            raise ValueError
    except ValueError:
        print("Please enter a valid task number.")
        return
    removed = tasks.pop(number - 1)
    save_tasks(tasks)
    print(f"Deleted: {removed['title']}")


def main():
    tasks = load_tasks()
    while True:
        print("\n=== Python To-Do List ===")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task complete")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
