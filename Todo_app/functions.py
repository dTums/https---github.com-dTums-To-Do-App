FILEPATH = "todo_app/todos.txt"

def get_todos(filepath=FILEPATH):
    """Read a text file and return the list of to-do items"""
    with open(filepath, 'r') as file_read:
        todos_read = file_read.readlines() #using the with function, you don't have to close the file.
    return todos_read
    
def write_todos(arg, filepath=FILEPATH):
    """Write the to-do item list in the text file."""
    with open(filepath, 'w') as file_write:
        file_write.writelines(arg) #using the with function, you don't have to close the file.

print('hello from functions')

if __name__ == "__main__":
    print("Hello")
    print(get_todos())