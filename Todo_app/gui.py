import functions

import PySimpleGUI as sg

label = sg.Text("Enter a To-Do")
input_box = sg.InputText(tooltip="Enter To Do")
add_button = sg.Button("Add")

window = sg.Window ('Tums To-Do app',  layout=[[label], [input_box, add_button]])
window.read()
window.close()