import functions
import PySimpleGUI as g
import time
import os

# Checking for user data existance
if not os.path.exists("user_data.txt"):
    with open("user_data.txt", "w") as file:
        pass

g.theme("DarkPurple4")

# Element declarations
clock = g.Text(key="time")
label = g.Text("Type in a to-do item:")
input_box = g.InputText(tooltip="Enter something here...", key="todo")
add_button = g.Button("Add")
list_box = g.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=[45, 10])
edit_button = g.Button("Edit")
complete_button = g.Button("Complete")
exit_button = g.Button("Exit")

message_label = g.Text(key="message")


# Window session
window = g.Window('To-Do App', 
                  layout=[[clock],
                          [label], 
                          [input_box, add_button],
                          [list_box, edit_button, complete_button],
                          [message_label],
                          [exit_button]], 
                  font=('Helvetica', 18))

# App execution
while True:
    action, value = window.read(timeout=200)
    window["time"].update(value=time.strftime("%b %d, %Y, %H:%M:%S"))
    match action:
        case "todos":
            window["todo"].update(value=value["todos"][0])
        case "Add":
            todos = functions.get_todos()

            new_todo = value["todo"] + "\n"
            todos.append(new_todo)
            
            functions.write_todos(todos)

            new_todo = new_todo.strip("\n")

            window["todos"].update(values=todos)
            window["message"].update(value=f"Successfully added '{new_todo}'.")
        case "Edit":
            try:
                selected_todo = value["todos"][0]
                edited_todo = value["todo"] + "\n"
                
                todos = functions.get_todos()
                index = todos.index(selected_todo)
                todos[index] = edited_todo
                
                functions.write_todos(todos)

                edited_todo = edited_todo.strip("\n")
                
                window["todos"].update(values=todos)
                window["message"].update(value=f"Successfully edited '{edited_todo}'.")
            except IndexError:
                g.popup("Please select a todo to edit!", font=("Helvetica", 20))
        case "Complete":
            try:
                completed_todo = value["todos"][0]

                todos = functions.get_todos()
                todos.remove(completed_todo)

                functions.write_todos(todos)

                completed_todo = completed_todo.strip("\n")

                window["todos"].update(values=todos)
                window["todo"].update(value="")
                window["message"].update(value=f"Marked '{completed_todo}' as completed.")
            except IndexError:
                g.popup("Please select a todo to mark as completed!", font=("Helvetica", 20))

        case "Exit":
            break

        case g.WIN_CLOSED:
            break    

# App termination
window.close()