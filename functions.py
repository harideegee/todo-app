FILEPATH = "user_data.txt"


def add_break(text):
    """Appends a break character to the end of a string input."""
    result = text + '\n'
    return result

def rem_break(text):
    """Removes the break character in the end of a string input."""
    result = text.strip('\n')
    return result

def get_todos(filepath=FILEPATH):
    """Returns the data in a text file in the form of a list."""
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos

def write_todos(context, filepath=FILEPATH):
    """Writes the given lines into a text file by replacing the existing values."""
    with open(filepath, "w") as file:
        file.writelines(context)
