Feature:

    @add_task
    Scenario: Add a new undone task to the tasklist
        Given a tasklist
        Buy Groceries: True
        Take dog out: False
        Given the user enters a new task "Read book"
        Then the tasklist should contain task "Read book"
        And the task "Read book" should be False




