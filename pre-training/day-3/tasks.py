"""
Task Tracker CLI
Sample:
Usage:
    python tasks.py add "Prepare Demo for Client"
    python tasks.py done 3
    python tasks.py delete 2
    python tasks.py list
    python tasks.py list --filter done
    python tasks.py list --filter todo
"""

import json
import sys
import os
from datetime import datetime


DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tasks.json")


class Task:
    def __init__(self, id, title, status="todo", created_at=None):
        self.id = id
        self.title = title
        self.status = status
        self.created_at = created_at or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status,
            "created_at": self.created_at,
        }

    def __str__(self): # dunder method; essential for making custom objects behave like native Python objects
        marker = "[x]" if self.status == "done" else "[ ]"
        return f"  {self.id:>3}  {marker}  {self.title}  ({self.created_at})"


class TaskManager:
    def __init__(self, filepath):
        self.filepath = filepath
        self.tasks = []
        self._load()

    def _load(self):
        if not os.path.exists(self.filepath):
            self.tasks = []
            return

        try:
            with open(self.filepath, "r") as f:
                data = json.load(f)
        except (json.JSONDecodeError, ValueError):
            print(f"Warning: {self.filepath} is corrupt or empty. Starting fresh.")
            self.tasks = []
            return

        self.tasks = []
        for entry in data:
            t = Task(
                id=entry["id"],
                title=entry["title"],
                status=entry.get("status", "todo"),
                created_at=entry.get("created_at"),
            )
            self.tasks.append(t)

    def _save(self):
        data = [t.to_dict() for t in self.tasks]
        with open(self.filepath, "w") as f:
            json.dump(data, f, indent=2)

    def _next_id(self):
        if not self.tasks:
            return 1
        return max(t.id for t in self.tasks) + 1

    def add_task(self, title):
        new_task = Task(id=self._next_id(), title=title)
        self.tasks.append(new_task)
        self._save()
        print(f"Added: #{new_task.id} — {title}")

    def complete_task(self, task_id):
        task = self._find(task_id)
        if task is None:
            print(f"Error: no task with id {task_id}")
            return
        if task.status == "done":
            print(f"Task #{task_id} is already done.")
            return
        task.status = "done"
        self._save()
        print(f"Completed: #{task_id} — {task.title}")

    def delete_task(self, task_id):
        task = self._find(task_id)
        if task is None:
            print(f"Error: no task with id {task_id}")
            return
        self.tasks.remove(task)
        self._save()
        print(f"Deleted: #{task_id} — {task.title}")

    def list_tasks(self, status_filter=None):
        filtered = self.tasks
        if status_filter:
            filtered = [t for t in self.tasks if t.status == status_filter]

        if not filtered:
            if status_filter:
                print(f"No tasks with status '{status_filter}'.")
            else:
                print("No tasks yet. Add one with: python tasks.py add \"your task\"")
            return

        print(f"\n{'ID':>5}  {'':4}  {'Title':<30}  {'Created'}")
        print("-" * 60)
        for t in filtered:
            print(t)
        print()

    def _find(self, task_id):
        for t in self.tasks:
            if t.id == task_id:
                return t
        return None


def print_usage():
    print("Usage:")
    print("  python tasks.py add \"task title\"")
    print("  python tasks.py done <id>")
    print("  python tasks.py delete <id>")
    print("  python tasks.py list [--filter done|todo]")


def main():
    args = sys.argv[1:]

    if len(args) == 0:
        print_usage()
        return

    manager = TaskManager(DATA_FILE)
    command = args[0].lower()

    if command == "add":
        if len(args) < 2:
            print("Error: provide a title. Example: python tasks.py add \"Fix bug\"")
            return
        title = " ".join(args[1:])
        manager.add_task(title)

    elif command == "done":
        if len(args) < 2:
            print("Error: provide a task id. Example: python tasks.py done 3")
            return
        try:
            task_id = int(args[1])
        except ValueError:
            print(f"Error: '{args[1]}' is not a valid id.")
            return
        manager.complete_task(task_id)

    elif command == "delete":
        if len(args) < 2:
            print("Error: provide a task id. Example: python tasks.py delete 2")
            return
        try:
            task_id = int(args[1])
        except ValueError:
            print(f"Error: '{args[1]}' is not a valid id.")
            return
        manager.delete_task(task_id)

    elif command == "list":
        status_filter = None
        if "--filter" in args:
            idx = args.index("--filter")
            if idx + 1 < len(args):
                status_filter = args[idx + 1]
                if status_filter not in ("todo", "done"):
                    print(f"Error: filter must be 'todo' or 'done', got '{status_filter}'")
                    return
            else:
                print("Error: --filter needs a value (todo or done)")
                return
        manager.list_tasks(status_filter)

    else:
        print(f"Unknown command: {command}")
        print_usage()


if __name__ == "__main__":
    main()
