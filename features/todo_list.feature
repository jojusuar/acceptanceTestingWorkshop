Feature:

    @add_task
    Scenario: Add a new undone task to the tasklist
        Given the tasklist is empty
        When the user enters a new task "Read book"
        Then the tasklist should contain task "Read book"
        And the task "Read book" should be not done



