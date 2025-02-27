# TaskTracker CLI

A simple command-line task management application written in Python that helps you track and organize your tasks.
credit:https://roadmap.sh/projects/task-tracker

## Features

- Add new tasks
- Update existing tasks
- Delete tasks
- Mark tasks as in-progress or done
- List tasks with status filtering
- Persistent storage using JSON

## Requirements

- Python 3.6 or higher

## Installation

1. Clone this repository or download the `TaskTracker.py` file
2. Ensure you have Python installed on your system

## Usage

To use the TaskTracker CLI, run the `TaskTracker.py` file and follow the prompts. You can add, update, delete, and mark tasks as in-progress or done. The tasks are stored in a JSON file, so they persist between runs.

For more detailed usage instructions, run `python TaskTracker.py` and follow the prompts.

Enjoy managing your tasks with TaskTracker!

Available commands:

- `add "<description>"` - Add a new task
- `update <id> "<new description>"` - Update an existing task
- `delete <id>` - Delete a task
- `mark-in-progress <id>` - Mark a task as in-progress
- `mark-done <id>` - Mark a task as done
- `list [all|todo|in-progress|done]` - List tasks with optional status filter

## Examples

Add a new task
python TaskTracker.py add "Complete the project documentation"
Update a task
python TaskTracker.py update 1 "Update the project documentation"
Mark a task as in-progress
python TaskTracker.py mark-in-progress 1
Mark a task as done
python TaskTracker.py mark-done 1
List all tasks
python TaskTracker.py list
List only in-progress tasks
python TaskTracker.py list in-progress