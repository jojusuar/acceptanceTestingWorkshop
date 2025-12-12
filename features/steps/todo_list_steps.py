from models.todo_list import TodoList
from behave import given, when, then

todo_list = TodoList()

@given("the tasklist is empty")
def step_impl(context):
    global todo_list
    todo_list = TodoList()


@when('the user enters a new task "{task}"')
def step_impl(context, task):
    global todo_list
    todo_list.add_task(task)


@then('the tasklist should contain task "{task}"')
def step_impl(context, task):
    global todo_list
    assert task in todo_list.tasklist, f'Task {task} not present in tasklist'


@then('the task "{task}" should be not done')
def step_impl(context, task):
    global todo_list
    assert todo_list.tasklist.get(task) is False, f"Task {task} is done"


@given('the tasklist contains the following tasks:')
def step_impl(context):
    global todo_list
    todo_list = TodoList()
    for row in context.table:
        task = row['task']
        done = row['done'].lower() == 'true'
        todo_list.tasklist[task] = done


@when('the user requests to list all tasks')
def step_impl(context):
    global todo_list
    context.listed_tasks = todo_list.all_tasks()


@then('the tasklist should show:')
def step_impl(context):
    expected_tasks = {row['task']: row['done'].lower() == 'true' for row in context.table}
    assert context.listed_tasks == expected_tasks, f"Expected {expected_tasks}, got {context.listed_tasks}"


@when('the user deletes the task "{task}"')
def step_impl(context, task):
    global todo_list
    todo_list.delete_task(task)


@when('the user marks task "{task}" as completed')
def step_impl(context, task):
    global todo_list
    result = todo_list.mark_task_completed(task)
    context.mark_result = result


@then('the tasklist should show task "{task}" as completed')
def step_impl(context, task):
    global todo_list
    assert task in todo_list.tasklist, f"Task {task} not found in tasklist"
    assert todo_list.tasklist[task] is True, f"Task {task} is not marked as completed"


@when('the user clears the list')
def step_impl(context):
    global todo_list
    assert todo_list.clear_list() == True, "The list failed to be cleared"


@then('the tasklist should now be empty')
def step_impl(context):
    global todo_list
    list_length = len(todo_list.all_tasks())
    assert list_length == 0, f'Expected list length = 0, but got length = {list_length}'