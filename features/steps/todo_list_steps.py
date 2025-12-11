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
