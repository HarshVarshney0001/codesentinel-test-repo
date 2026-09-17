import json

def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as f:
        json.dump(tasks, f)

def load_tasks(filename="tasks.json"):
    # BUG: no error handling if file doesn't exist
    with open(filename, "r") as f:
        return json.load(f)

def delete_task_file(filename="tasks.json"):
    import os
    # BUG: no check if file exists before deleting
    os.remove(filename)
