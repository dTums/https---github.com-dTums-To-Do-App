import PySimpleGUI as sg

label1 = sg.Text('Enter Feet')
box1 = sg.InputText()

label2 = sg.Text('Enter Inches')
box2 = sg.InputText()

button = sg.Button('Convert')

window = sg.Window ('Convertor', layout=[[label1, box1],
                                         [label2, box2],
                                         [button]])

window.read()
window.close()