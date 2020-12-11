import PySimpleGUI as sg
from file import file_read, file_write

fname = "Text.txt"

tasks = file_read(fname)

layout = [
    [sg.Text("ToDo List")],
    [sg.InputText("", key='todo_item'), sg.Button(button_text="Add", key='add_save')],
    [sg.Listbox(values=tasks, size=(40, 10), key="items"), sg.Button("Delete"), sg.Button("Edit"), sg.Button("Exit")]
]

window = sg.Window("ToDo App", layout)
while True:
    events, values = window.Read()
    if events == 'add_save':
        tasks.append(values['todo_item'])
        window.FindElement('items').Update(values=tasks)
        window.FindElement('add_save').Update("Add")
        window.FindElement('todo_item').Update('')

    elif events == "Delete":
        tasks.remove(values["items"][0])
        window.FindElement('items').Update(values=tasks)
        file_write(fname, tasks)

    elif events == "Edit":
        edit_val = values["items"][0]
        tasks.remove(values["items"][0])
        window.FindElement('items').Update(values=tasks)
        window.FindElement('todo_item').Update(value=edit_val)
        window.FindElement('add_save').Update("Save")
        file_write(fname, tasks)

    elif events == None or events == "Exit":
        break

window.Close()