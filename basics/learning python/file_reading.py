
try:
    path="C:\\text_folder\\New Text Document.txt"

    with open(path) as file:
        print(file.read())
except FileNotFoundError as e:
    print(e)