class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.description}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task}")

    def update_task(self, index, new_description=None, completed=None):
        if 0 <= index < len(self.tasks):
            if new_description:
                self.tasks[index].description = new_description
            if completed is not None:
                self.tasks[index].completed = completed
        else:
            print("Invalid task number.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            print("Invalid task number.")

    def save_tasks(self, filename):
        with open(filename, 'w') as file:
            for task in self.tasks:
                file.write(f"{task.description},{task.completed}\n")

    def load_tasks(self, filename):
        try:
            with open(filename, 'r') as file:
                self.tasks = []
                for line in file:
                    description, completed = line.strip().split(',')
                    task = Task(description)
                    task.completed = completed == 'True'
                    self.tasks.append(task)
        except FileNotFoundError:
            print("File not found. Starting with an empty to-do list.")

def main():
    todo_list = ToDoList()
    todo_list.load_tasks('tasks.txt')

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter the task description: ")
            todo_list.add_task(description)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            index = int(input("Enter the task number to update: ")) - 1
            new_description = input("Enter the new description (or leave blank to keep current): ")
            completed = input("Is the task completed? (yes/no): ").lower() == 'yes'
            todo_list.update_task(index, new_description or None, completed)
        elif choice == '4':
            index = int(input("Enter the task number to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == '5':
            todo_list.save_tasks('tasks.txt')
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
