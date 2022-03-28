file_name = "data.txt"


def save(value: int):
    file = open(file_name, "w+")
    file.write(str(value))
    file.close()


def load():
    file = open(file_name, "r")
    contents = file.read()
    return contents

