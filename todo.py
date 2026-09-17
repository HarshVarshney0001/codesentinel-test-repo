class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, index):
        # BUG: no check if index is out of range
        del self.tasks[index]

    def get_task(self, index):
        return self.tasks[index]

    def mark_complete(self, index):
        self.tasks[index]["done"] = True

    def get_first_task(self):
        # BUG: empty list not handled, will crash
        return self.tasks[0]

    def count_pending(self):
        count = 0
        for task in self.tasks:
            if task["done"] = False:  # BUG: should be == not =
                count += 1
        return count
