def snake_to_camel(snake_case):
    # Split the snake case string into words
    words = snake_case.split('_')
    
    # Capitalize the first letter of each word except for the first word
    camel_case = words[0] + ''.join(word.capitalize() for word in words[1:])
    
    return camel_case
f = open("row.txt", "r")
def main():
    snake_case = f.read()
    camel_case = snake_to_camel(snake_case)
    print("Camel case string:", camel_case)

if __name__ == "__main__":
    main()
