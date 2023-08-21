FILENAME = 'todos.txt'


def get_todos(filepath=FILENAME):
    """"READ a text file and return a
    list of todo items """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILENAME):
    """"WRITE a text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


print(__name__)
if __name__ == "__main__":
    print("hello from functions")
    print(get_todos())
