import functions
import PySimpleGUI as sg


label = sg.Txt("type in a To-Do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
window = sg.Window("My To-Do App", layout=[[label], [input_box, add_button]], font=("Helvetica", 20))

while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case "Add":
            todos = functions.get_todos()
            todo = value['todo'] + "\n"
            todos.append(todo)
            functions.write_todos(todos)
        case sg.WINDOW_CLOSED:
            break
window.close()
