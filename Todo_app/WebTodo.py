import streamlit as st #new intuitive library for creating web apps and integrate well with graphs. also easy to deploy
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("Tums ToDo App")
st.subheader("This is my Todo App.")
st.write("This app hopes to increase your productivity")

#edit_button = st.button("Edit") 
complete_button = st.button("Completed")


#removing a compteled todo after, this happens when the user clicks the checkbox automatically
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        if complete_button:
            todos.pop(index)
            functions.write_todos(todos)
            del st.session_state[todo]
            st.experimental_rerun()
        #if edit_button:
            #todo_to_edit =  checkbox[todo]
            #new_todo = st.text_input(label="", placeholder= "Edit todo... ", on_change=add_todo, key="new_todo")

         #   functions.write_todos(todos)
          #  del st.session_state[todo]
           # st.experimental_rerun()



st.text_input(label="text", label_visibility="hidden", placeholder= "Add new todo... ", on_change=add_todo, key="new_todo")
st.text_input = st.empty()

st.session_state  


#value = "default"
#if st.button('reset textarea'):
#    value = ''