import os

path = input("Введите путь: ")

if os.path.exists(path):
    print("Path exists.")

    directory, filename = os.path.split(path)

    print("Directory:", directory)
    print("Filename:", filename)
else:
    print("Путь не существует.")
    