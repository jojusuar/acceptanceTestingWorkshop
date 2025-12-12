Feature:

    @add_task
    Scenario: Add a new undone task to the tasklist
        Given the tasklist is empty
        When the user enters a new task "Read book"
        Then the tasklist should contain task "Read book"
        And the task "Read book" should be not done

    @list_tasks
    Scenario: List all tasks in the tasklist
        Given the tasklist contains the following tasks:
            | task        | done  |
            | Read book   | false |
            | Buy milk    | true  |
        When the user requests to list all tasks
        Then the tasklist should show:
            | task        | done  |
            | Read book   | false |
            | Buy milk    | true  |

    @delete_task
    Scenario: Delete a specific task from the list

        Given the tasklist contains the following tasks:
        | task      | done  |
        | Read book | false |
        | Buy milk  | true  |

        When the user deletes the task "Buy milk"
        And the user requests to list all tasks

        Then the tasklist should show:
        | task      | done  |
        | Read book | false |
    @mark_completed
    Scenario: Mark a task as completed
        Given the tasklist contains the following tasks:
            | task          | done  |
            | Buy groceries | false |
        When the user marks task "Buy groceries" as completed
        Then the tasklist should show task "Buy groceries" as completed
        
