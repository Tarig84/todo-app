# from functions import get_todos, write_todos
import functions
import time
date = time.strftime("%b-%d-%Y  %H:%M:%S")
print(date)

while True:
    user_action = input("Enter add, show, edit, , complete, exit,: ")
    user_action = user_action.strip()
    if user_action.startswith("add"):
        todos = functions.get_todos()
        todo = user_action[4:] + "\n"
        todos.append(todo)
        functions.write_todos(todos)
    elif user_action.startswith("show"):
        todos = functions.get_todos()
        for n, i in enumerate(todos):
            i = i.strip("\n")
            print(f"{n + 1}- {i.title()}")
    elif user_action.startswith("edit"):
        try:
            todos = functions.get_todos()
            edit_index = int(user_action[5:])
            edit_index = edit_index - 1
            print("todo to Edit is", todos[edit_index].strip("\n"))
            new_todo = input("Enter new todo: ")
            todos[edit_index] = new_todo + "\n"
            functions.write_todos(todos)
        except ValueError:
            print("Your Command Is Not Valid")
            continue
        except IndexError:
            print("There is no item with that number")
            continue
    elif user_action.startswith("complete"):
        try:
            todos = functions.get_todos()
            edit_index = int(user_action[9:])
            edit_index = edit_index - 1
            removed_todo = todos.pop(edit_index)
            print(f"removed todo is {removed_todo.capitalize()}")
            functions.write_todos(todos)
        except IndexError:
            print("There is no item with that number")
            continue
        except ValueError:
            print("Your Command Is Not Valid")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command Is Not Valid")

print("Bye!")
