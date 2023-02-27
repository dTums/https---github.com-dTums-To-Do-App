from functions import get_todos, write_todos
import time

now = time.strftime("%d %b %Y %H:%M:%S")
print("It is ", now)

while True:
    user_action = input ("Enter add, show, edit, complete or exit: ")
    user_action = user_action.lower()
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo  = user_action[4:]
  
        todos = get_todos()
        
        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith("show"):
   
        todos = get_todos()

        todos_no_spaces = [] #this line till line 23 removes the extra space between items on the terminal output
        for item in todos:
            new_item = item.strip('\n')
            todos_no_spaces.append(new_item)
        #doing the above with list comprehensions: todos_no_spaces = [new_item.strip('\n) for item in todos]
        for index, item in enumerate(todos_no_spaces):
            item = item.capitalize()
            print (f"{index+1} - {item}")
        
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1
            
            todos = get_todos()
                                                                                                                    
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos)
        except ValueError:
            print("Your command is not valid. Please enter a number")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            index = number - 1
            
            todos = get_todos()  
            todo_to_be_removed = todos[index].strip('\n')
            todos.pop(index)
            write_todos(todos)
            print(f"{todo_to_be_removed} has been removed! The remaining items are:  {todos}")
        except IndexError:
            print ("Number out of range. There is no item with that number.")
            continue
    elif user_action.startswith("exit"):
        break    

    else:
        print("Command is not valid")
   
print("Goodbye. Have a nice one")