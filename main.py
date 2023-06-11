import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    if st.session_state["new_todo"].strip(" ") != "":
        todo = st.session_state["new_todo"] + "\n"
        todos.append(todo)
        functions.write_todos(todos)
        st.session_state["new_todo"] = ""
    else:
        warning = "<p style='color:red'>Don't leave the input blank!</p>"
        st.markdown(warning, unsafe_allow_html=True)


st.title("To-Do App")
st.subheader("Keep track of all your todos using this app!")
st.write("Now you'll never forget what you wanted to do (unless you forget to note it down!)")

if len(todos) == 0:
    message = "<p style='color:green'>Wow! You have no more tasks left to do!</p>"
    st.markdown(message, unsafe_allow_html=True)
else:    
    for index, todo in enumerate(todos):
        checkbox = st.checkbox(todo, key=index)
        if checkbox:
            todos.pop(index)
            functions.write_todos(todos)
            del st.session_state[index]
            st.experimental_rerun()

st.text_input(label="Add a new todo", placeholder="Start typing here...", on_change=add_todo, key="new_todo")