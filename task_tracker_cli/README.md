The list of commands and their usage is given below:

bash

# Adding a new task
add "\<description\>"

python task_tracker_cli.py add "Buy groceries"
# Updating and deleting tasks
update \<ID\> "\<description\>"

python task_tracker_cli.py update 1 "Buy groceries and cook dinner"

delete \<ID\>

python task_tracker_cli.py delete 1
# Marking a task as in progress or done
mark-\<status\> \<ID\>

python task_tracker_cli.py mark-in-progress 1

python task_tracker_cli.py mark-done 1
# Listing all tasks
python task_tracker_cli.py list
# Listing tasks by status
python task_tracker_cli.py list done

python task_tracker_cli.py list todo

python task_tracker_cli.py list in-progress