class TodoList:

    def __init__(self):
        self.tasklist = {}

    def add_task(self, task: str):
        self.tasklist[task] = False

    def all_tasks(self):
        for i, (task, done) in enumerate(self.tasklist.items()):
            print(f"Task {i}: {task} -> Completed: {done}")

    def mark_task_completed(self, task: str):
        if task in self.tasklist:
            self.tasklist[task] = True
            return True
        return False

    def clear_list(self):
        self.tasklist.clear()
        return True
