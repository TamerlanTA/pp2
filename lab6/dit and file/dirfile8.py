import os

def delete(path):
    if os.path.exists(path):
        print("Файл существует")

        if os.access(path, os.W_OK):
            os.remove(path)
            print("Файл успшно удален")
        else:
            print("Нет доступа к удалению")
    else:
        print("файла не существует")

path = input("File to delete: ")
delete(path)
