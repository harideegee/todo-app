import streamlit as st
import functions

todos = functions.get_todos()

st.title("To-Do App")
st.subheader("Keep track of all your todos using this app!")
st.write("Now you'll never forget what you wanted to do (unless you forget to note it down!)")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Add a new todo", placeholder="Start typing here...")