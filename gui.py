import functions
import PySimpleGUI as sg
import time

sg.theme("BlueMono")

time_lab = sg.Txt("", key='time')
label = sg.Txt("type in a To-Do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[44, 8])
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')


window = sg.Window("My To-Do App", layout=[[time_lab], [label], [input_box, add_button],
                                           [list_box, edit_button, complete_button],
                                           [exit_button]], font=("Helvetica", 20))

while True:
    event, value = window.read(timeout=500)
    window['time'].update(value=time.strftime("%b-%d-%Y   %H:%M:%S"))

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
            window['todo'].update(value='')
        case "Edit":
            try:
                todo_to_edit = value['todos'][0]
                new_todo = value['todo'] + "\n"
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup('Please select item first', font=("Helvetica", 20), text_color='red')
                continue
        case "Complete":
            try:
                completed_todo = value['todos'][0]
                todos = functions.get_todos()
                todos.remove(completed_todo)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup('Please select item first', font=("Helvetica", 20), text_color='red')
                continue
        case "Exit":
            exit()
        case sg.WINDOW_CLOSED:
            break
window.close()
