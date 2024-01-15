import functions
import PySimpleGUI as sg


label = sg.Txt("type in a To-Do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

list_box = sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=[45, 10])
edit_button = sg.Button('Edit')
window = sg.Window("My To-Do App", layout=[[label], [input_box, add_button],
                                           [list_box, edit_button]], font=("Helvetica", 20))

while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case "todos":
            box1 = value['todos'][0].strip('\n')
            window['todo'].update(value=box1)
        case "Add":
            todos = functions.get_todos()
            todo = value['todo'] + "\n"
            todos.append(todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = value['todos'][0]
            new_todo = value['todo'] + "\n"
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case sg.WINDOW_CLOSED:
            break
window.close()
