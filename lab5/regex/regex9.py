import re

def insert_spaces(text):
    modified_text = re.sub(r'(?<!^)(?=[A-Z])', ' ', text)
    return modified_text
f = open("row.txt", "r")
def main():
    text = f.read()
    modified_text = insert_spaces(text)
    print("Modified string with spaces:", modified_text)

if __name__ == "__main__":
    main()
