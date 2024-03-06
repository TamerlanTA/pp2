def copy_file(source_file, destination_file):
    try:
        with open(source_file, "r") as source:
            contents = source.read()
        
        with open(destination_file, "w") as destination:
            destination.write(contents)
        
        print("Содержимое успешно скопированно с", source_file, "в", destination_file)
    except FileNotFoundError:
        print("Один из файлов не существует")
    except IOError:
        print("Error")

# Example usage:
source_file = input("От куда скопировать: ")
destination_file = input("Куда вставить: ")

copy_file(source_file, destination_file)
