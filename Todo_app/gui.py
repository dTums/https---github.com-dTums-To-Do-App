import functions
import PySimpleGUI as sg
import time

sg.theme("DarkGreen4")

label_time = sg.Text('', key='clock')
label = sg.Text("Enter a To-Do")
input_box = sg.InputText(tooltip="Enter To Do", key="todo")
add_button = sg.Button("Add")

list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Close")

window = sg.Window ('Tums To-Do app',  
                    layout=[[label_time],
                            [label], 
                            [input_box, add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button]], 
                    font =('Helvetika', 20))


while True:
    event, values = window.read(timeout=500)
    window['clock'].update(value=time.strftime("%d %b %Y %H:%M:%S"))
    #print(1, event)
    #print(2, values)
    #print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            if values['todo'] != '':
                new_todo = values['todo'] + '\n'
                todos.append(new_todo)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            else:
                sg.popup("Please enter a todo item",title="Note!", font=('Helvetika', 20))
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select item to edit.", title="Note!", font=('Helvetika', 20))
        case "Complete":
            try:
                todos_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todos_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select a completed item.", title="Note!", font=('Helvetika', 20))
        case "Close":
            break
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()