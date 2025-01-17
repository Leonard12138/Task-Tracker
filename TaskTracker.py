import json
import sys
import os
from datetime import datetime

class TaskTracker:
    def __init__(self):
        self.tasks_file = "tasks.json"
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.tasks_file):
            return []
        try:
            with open(self.tasks_file, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    def save_tasks(self):
        with open(self.tasks_file, 'w') as f:
            json.dump(self.tasks, f, indent=2)

    def get_new_id(self):
        return max([task['id'] for task in self.tasks], default=0) + 1

    def add_task(self, description):
        task = {
            'id': self.get_new_id(),
            'description': description,
            'status': 'todo',
            'createdAt': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'updatedAt': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task added successfully (ID: {task['id']})")

    def update_task(self, task_id, new_description):
        for task in self.tasks:
            if task['id'] == task_id:
                task['description'] = new_description
                task['updatedAt'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.save_tasks()
                print("Task updated successfully")
                return
        print(f"Error: Task with ID {task_id} not found")

    def delete_task(self, task_id):
        initial_length = len(self.tasks)
        self.tasks = [task for task in self.tasks if task['id'] != task_id]
        if len(self.tasks) < initial_length:
            self.save_tasks()
            print("Task deleted successfully")
        else:
            print(f"Error: Task with ID {task_id} not found")

    def mark_task(self, task_id, status):
        for task in self.tasks:
            if task['id'] == task_id:
                task['status'] = status
                task['updatedAt'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.save_tasks()
                print(f"Task marked as {status}")
                return
        print(f"Error: Task with ID {task_id} not found")

    def list_tasks(self, status=None):
        if not self.tasks:
            print("No tasks found")
            return

        filtered_tasks = self.tasks
        if status and status != 'all':
            filtered_tasks = [task for task in self.tasks if task['status'] == status]

        if not filtered_tasks:
            print(f"No tasks found with status: {status}")
            return

        print("\nTasks:")
        for task in filtered_tasks:
            print(f"#{task['id']}: {task['description']} [{task['status']}]")

def print_usage():
    print("Usage:")
    print("  task-cli add \"<description>\"")
    print("  task-cli update <id> \"<new description>\"")
    print("  task-cli delete <id>")
    print("  task-cli mark-in-progress <id>")
    print("  task-cli mark-done <id>")
    print("  task-cli list [all|todo|in-progress|done]")

def main():
    if len(sys.argv) < 2:
        print_usage()
        return

    tracker = TaskTracker()
    command = sys.argv[1].lower()

    try:
        if command == "add" and len(sys.argv) >= 3:
            tracker.add_task(sys.argv[2])

        elif command == "update" and len(sys.argv) >= 4:
            tracker.update_task(int(sys.argv[2]), sys.argv[3])

        elif command == "delete" and len(sys.argv) >= 3:
            tracker.delete_task(int(sys.argv[2]))

        elif command == "mark-in-progress" and len(sys.argv) >= 3:
            tracker.mark_task(int(sys.argv[2]), "in-progress")

        elif command == "mark-done" and len(sys.argv) >= 3:
            tracker.mark_task(int(sys.argv[2]), "done")

        elif command == "list":
            status = sys.argv[2] if len(sys.argv) > 2 else "all"
            if status not in ["all", "todo", "in-progress", "done"]:
                print(f"Error: Invalid status '{status}'")
                return
            tracker.list_tasks(status)

        else:
            print("Error: Invalid command or missing arguments")
            print_usage()

    except ValueError:
        print("Error: Task ID must be a number")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
