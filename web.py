import streamlit as st
import functions as fun

todos = fun.get_todos()


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    # print(new_todo)
    todos.append(new_todo)
    fun.write_todos(todos)


st.title("My Todo App - day 19")
st.subheader("this is My Todo App")

st.write("my lovely app")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        fun.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo",
              on_change=add_todo,
              key="new_todo")

st.session_state
