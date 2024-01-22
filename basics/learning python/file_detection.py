import os

path="C:\\Users\\ADMIN\\PycharmProjects\\currency_converter_chatbot"

if os.path.exists(path):
    print("File is founded")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("File isn't found")