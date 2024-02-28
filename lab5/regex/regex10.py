def camel_to_snake(camel_case):
    snake_case = ''
    for char in camel_case:
        if char.isupper():
            snake_case += '_' + char.lower()
        else:
            snake_case += char
    return snake_case.lstrip('_')
f = open("row.txt", "r")
def main():
    camel_case = f.read()
    snake_case = camel_to_snake(camel_case)
    print("Snake case string:", snake_case)

if __name__ == "__main__":
    main()
