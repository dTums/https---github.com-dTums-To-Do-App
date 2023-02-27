import functions

import PySimpleGUI as sg

label = sg.Text("Enter a To-Do")
input_box = sg.InputText(tooltip="Enter To Do", key="todo")
add_button = sg.Button("Add")

window = sg.Window ('Tums To-Do app',  
                    layout=[[label], [input_box, add_button]], 
                    font =('Helvetika', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break
window.close()