from functions import add_break, rem_break, get_todos, write_todos
import time

print("Hello, here's a way to orgainse your tasks more efficiently! Begin by typing either of the following commands...")
print("===================================================")
print("Please bear in mind the syntax for entering your request.")
print("'add <task name>' adds a new task with the name <task name>.")
print("'show' displays all your current tasks to do.")
print("'edit <task id>' edits the task with the id <task id>.")
print("'complete <task id>' removes the task with the id <task id>.")
print("'exit' quits the program.")
print("===================================================")

todos = get_todos()
if todos:
    print("Here are your existing todos.")
    for index, item in enumerate(todos):
        print(f"{index+1}. {rem_break(item)}")
    print("===================================================")

now = time.strftime("%b %d, %Y, %H:%M:%S")
print(f"It is {now}.")

while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.lower()
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = add_break(user_action[4:])
        todos = get_todos()
        todos.append(todo)
        write_todos(todos)
        for index, item in enumerate(todos):
            print(f"{index+1}. {rem_break(item)}")
        print(f"The item '{rem_break(todo)}' was added to your to do list. You now have {len(todos)} thing(s) left to do.")
    
    elif user_action.startswith("show"):
        todos = todos = get_todos()
        for index, item in enumerate(todos):
            print(f"{index+1}. {rem_break(item)}")
        print(f"You have {len(todos)} thing(s) left to do.")
    
    elif user_action.startswith("edit"):
        for index, item in enumerate(todos):
            print(f"{index+1}. {rem_break(item)}")
        try:
            edit_position = int(user_action[5:])
            edit_position = edit_position - 1
            edited_todo = add_break(input(f"What do you want to replace '{rem_break(todos[edit_position])}' with? "))
            todos = get_todos()
            previous_value = todos[edit_position]
            todos[edit_position] = edited_todo
            write_todos(todos)

            print(f"The item '{rem_break(previous_value)}' was updated to '{rem_break(edited_todo)}'!")
        except:
            todos = get_todos()
            data_verify = add_break(user_action[5:])
            if data_verify in todos:
                edited_todo = input(f"What do you want to replace '{rem_break(user_action[5:])}' with? ") + "\n"
                edit_position = todos.index(data_verify)
                todos = get_todos()
                previous_value = rem_break(user_action[5:])
                todos[edit_position] = edited_todo
                
                write_todos(todos)

                print(f"The item '{rem_break(previous_value)}' was updated to '{rem_break(edited_todo)}'!")
            else:
                print("Did not find that task in your list. Consider using the 'add' command.")

    
    elif user_action.startswith("complete"):
        try:
            complete = int(user_action[9:])
            complete = complete - 1
            todos = get_todos()
            task_completed = todos[complete]
            todos.pop(complete)

            write_todos(todos)

            for index, item in enumerate(todos):
                print(f"{index+1}. {rem_break(item)}")
            print(f"The task '{rem_break(task_completed)}' was removed from your list! You now have {len(todos)} thing(s) left to do.")
        except:
            with open("user_data.txt", "w") as file:
                file.truncate()
            todos = get_todos()
            print(f"All the tasks were removed from your list! You now have {len(todos)} thing(s) left to do.")
        
    
    elif user_action.startswith("exit"):
        break
    
    else:
        print("Sorry, your input was invalid. Please try again!")

print("Until next time!")