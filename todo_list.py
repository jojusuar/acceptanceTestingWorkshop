tasklist = {}


def add_task(task: str):
    tasklist[task] = False


def all_tasks():
    for i, (task, done) in enumerate(tasklist.items()):
        print(f"Task {i}: {task} -> Completed: {done}")

# implementar lcada requerimiento como función
def mark_task_completed(task: str):
    if task in tasklist:
        tasklist[task] = True
        return True
    return False
