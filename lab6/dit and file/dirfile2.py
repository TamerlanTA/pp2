import os

path = input("Введите путь: ")

if os.path.exists(path):
    print("Путь существует.")

    if os.access(path, os.R_OK):
        print("Доступ на чтение есть.")
    else:
        print("Нет доступа на чтение.")

    if os.access(path, os.W_OK):
        print("Доступ на запись есть.")
    else:
        print("Нет доступа на запись.")

    if os.path.isdir(path):
        if os.access(path, os.X_OK):
            print("Доступ на исполнение есть.")
        else:
            print("Нет доступа на исполнение.")
else:
    print("Путь не существует.")
